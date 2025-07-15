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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 187b70b8-a037-33a9-8369-87ca74f99a6f | -7.09533 | -44.3905 | 2025-07-15 00:45:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f3b81e7d-9d7d-3315-b380-24ab4cab1d81 | -5.79186 | -45.12429 | 2025-07-15 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 33f72c0a-24ce-307a-9087-c06a4d33f263 | -7.21665 | -45.3306 | 2025-07-15 00:45:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3e9f9dfb-1914-33e3-bf87-69775537e7a7 | -8.60979 | -47.44033 | 2025-07-15 00:45:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9e7dc690-9fcd-396a-bd54-cfc182db3380 | -6.13322 | -42.96504 | 2025-07-15 00:45:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 71f2c04b-f858-3fc2-87b3-54eaad46ee35 | -7.19548 | -43.09528 | 2025-07-15 00:45:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 97cdfd75-d4db-3ab7-ba02-1082bc95831c | -8.38314 | -51.06816 | 2025-07-15 00:45:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c2745bad-5043-330a-9c76-ad2ffd346d8b | -6.91149 | -52.85015 | 2025-07-15 00:45:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dbfc196c-f4ac-3a7c-b9ed-585630236759 | -5.78658 | -45.09029 | 2025-07-15 00:45:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| a749dd81-c11a-3fa4-a1b8-ef660cb81f7b | -7.20592 | -45.32294 | 2025-07-15 00:45:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9aff15c7-a612-3cf8-b136-f6d53ea6f0a1 | -8.65539 | -47.75635 | 2025-07-15 00:45:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 89938e43-7b60-349e-8f3e-c50ae949b0ca | -6.99307 | -47.08691 | 2025-07-15 00:45:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3a7b46ae-d516-3da8-8bb4-b07fe0e2415b | -7.58209 | -44.7229 | 2025-07-15 00:45:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f2919f58-f096-3472-8b98-17aeb5013aaf | -6.38967 | -43.72707 | 2025-07-15 00:45:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9286951d-65aa-354a-8482-fbdfd6f05d67 | -3.58486 | -47.51027 | 2025-07-15 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 276ff596-5cee-3153-8bb1-e04ad3e6ff07 | -3.58666 | -47.52257 | 2025-07-15 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 40f78f28-e287-3c36-b2e2-f17db2241325 | -4.27646 | -48.18892 | 2025-07-15 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7c1f0ac0-699f-307a-931e-f9c7d8dc8876 | -3.75557 | -47.12318 | 2025-07-15 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| d49c1c1d-6954-3a58-82c7-418ce4ca71d1 | -3.38076 | -47.49476 | 2025-07-15 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c0cf5a56-7868-3625-a226-a68c129f4560 | -3.57831 | -47.51703 | 2025-07-15 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 886948c8-85bc-3467-8d55-5691b793a92c | -2.91435 | -48.25031 | 2025-07-15 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 87d4adcb-46fa-386b-9e50-4fa88d4d4d93 | -2.92428 | -48.24889 | 2025-07-15 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4d603756-f073-3a41-812d-d58813cab3b7 | -3.38865 | -47.50051 | 2025-07-15 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 86894d95-b794-3abb-9e1f-dc4fd65e4c2d | -3.38684 | -47.48818 | 2025-07-15 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 36b72b74-ef9f-34fd-bf35-cd842374c22a | -3.38501 | -47.47575 | 2025-07-15 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 5651eaaf-bcc0-39c3-8447-e12a252a44bb | -4.03289 | -48.05568 | 2025-07-15 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4b785e59-3bba-3090-a58b-4a13a22f0e13 | -3.37727 | -47.46992 | 2025-07-15 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 19037869-60e4-3120-aaf5-c0eee8154494 | -4.2749 | -48.17796 | 2025-07-15 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d5502156-16cd-3e22-b34b-b21064f5cd7e | -3.58003 | -47.52934 | 2025-07-15 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2acb6473-ace5-3197-b3c5-371324010b82 | -4.67778 | -48.86601 | 2025-07-15 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73c3a64e-be8e-379f-a681-cec8edf79077 | -2.91277 | -48.23904 | 2025-07-15 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| bf9667ba-0140-35e3-9f5b-f9b17982abd5 | -4.03453 | -48.06694 | 2025-07-15 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| c101ed94-7efd-30c9-83b7-7b6a281415e1 | -2.44328 | -47.33306 | 2025-07-15 00:48:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 333b4b8d-fcc1-3840-8bdf-fc8df89f8103 | -4.22693 | -47.77059 | 2025-07-15 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3a49e886-2475-3d48-98f0-72c9c530c2db | -2.9227 | -48.23761 | 2025-07-15 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| e96ea0bb-b760-3ec6-93c9-3705a184bb35 | -3.38316 | -47.46322 | 2025-07-15 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ff5a62d3-955e-3ae0-8a39-3cfbafd64724 | -5.5241 | -43.8878 | 2025-07-15 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e9be5d0a-d8a2-3778-9727-55e87e757521 | -11.4588 | -45.0895 | 2025-07-15 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 248.4 |
| 3574e2bc-fbc1-3a0e-8924-a743c3a0ecc9 | -9.2928 | -63.719 | 2025-07-15 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 116.8 |
| ca91be58-7dc7-3a70-82a2-4cbcdf70e3fb | -11.4592 | -45.0664 | 2025-07-15 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 74f3cd34-8ef9-3901-90b7-d7728482c49b | -11.4584 | -45.1126 | 2025-07-15 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| c85b650c-d75c-3722-9dba-d7a82e4f7d4d | -5.5429 | -43.8864 | 2025-07-15 00:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b904217e-fa5a-3736-b1f6-74b42a40ffaa | -5.7941 | -45.104 | 2025-07-15 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d2924996-205e-3d45-a99b-ff5d97072d22 | -11.4393 | -45.1154 | 2025-07-15 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a1c2ebce-98c4-36b0-87ed-4ea9025734a9 | -10.5586 | -49.1337 | 2025-07-15 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| dd8503bd-6a69-3862-919a-fae8c125766a | -11.478 | -45.0868 | 2025-07-15 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e9e3d339-62c9-343f-828a-d0e5c87c7c1f | -10.5776 | -49.1316 | 2025-07-15 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ee831180-89f3-3d2e-8b44-f61b0f4a341c | -11.4397 | -45.0923 | 2025-07-15 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 3f64e535-5412-3300-a3f6-5082ef87372c | -11.4588 | -45.0895 | 2025-07-15 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 258.8 |
| a538cd15-a724-3b84-b0f1-635a68481eb7 | -11.4397 | -45.0923 | 2025-07-15 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 0c4f0ca5-c8bc-36f5-8940-2648a4022e90 | -10.5776 | -49.1316 | 2025-07-15 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 2af674a5-6cee-3d56-9b29-b2ec87885231 | -5.7941 | -45.104 | 2025-07-15 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 721ea72e-84c1-3577-b288-1d9df714e591 | -11.4584 | -45.1126 | 2025-07-15 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 34f60da7-b5ca-33a4-82b5-ce37ebf2d200 | -11.4393 | -45.1154 | 2025-07-15 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 5e11a6ab-a385-3c01-a87c-8bc81c99e598 | -10.5586 | -49.1337 | 2025-07-15 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d5a03c1b-9be0-38b3-a18e-4ba5d2a40a96 | -5.5241 | -43.8878 | 2025-07-15 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 08a9fb87-72b4-398d-bf6f-7fd6f970fe5a | -11.478 | -45.0868 | 2025-07-15 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a8b98dc4-e9b9-3461-9639-38ed3b0d5189 | -9.2928 | -63.719 | 2025-07-15 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| dda32799-c84a-3bc4-8e74-3c7e5cb5f18c | -5.5429 | -43.8864 | 2025-07-15 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| fb45e834-0fd6-33e0-8009-3efc59397277 | -10.5776 | -49.1316 | 2025-07-15 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 1a053ee3-254e-3cd1-828a-064702911c31 | -11.4584 | -45.1126 | 2025-07-15 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 23ceaf6f-beec-3956-bf20-32d8694529ea | -11.4393 | -45.1154 | 2025-07-15 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 9d9fcc19-796b-3f8a-8ed5-dbb71f474ef2 | -11.4397 | -45.0923 | 2025-07-15 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b831f202-7dce-3576-9303-cb8c7a1f05ad | -11.4389 | -45.1385 | 2025-07-15 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 254c3228-2c33-31b4-a76a-21dd4e7cab90 | -9.2928 | -63.719 | 2025-07-15 01:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 60544a2f-0618-31c7-ab8f-5b6fe2d8eb73 | -5.7941 | -45.104 | 2025-07-15 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| b8064a4c-835d-3c36-b68f-833af6a47815 | -5.5429 | -43.8864 | 2025-07-15 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e46cff02-1d52-358c-9a4e-9908e55846fb | -11.478 | -45.0868 | 2025-07-15 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 518b8abd-0438-38bb-be6d-d0d2a1ad0f6e | -11.4592 | -45.0664 | 2025-07-15 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 64ae3eda-b95c-365c-a438-66ef1ab8df4a | -11.4588 | -45.0895 | 2025-07-15 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 292.9 |
| 04a00077-bf39-3fe8-883e-0da7c1c553d3 | -5.7754 | -45.1053 | 2025-07-15 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| dd816b7e-323d-3071-abee-47c20903cd62 | -11.4588 | -45.0895 | 2025-07-15 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 255.0 |
| f1a7f2ff-a75a-3a3c-9c19-04520a30cb8e | -10.5776 | -49.1316 | 2025-07-15 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 89ea0348-2e77-31c4-941e-03574248ecdd | -10.5586 | -49.1337 | 2025-07-15 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 779631a8-dc2c-3370-8e46-edbbe4fb6eb1 | -11.478 | -45.0868 | 2025-07-15 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| da541098-4fba-31b0-ac8b-fd86ffa0f3fd | -5.5429 | -43.8864 | 2025-07-15 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 32c034c0-242e-3199-99b2-2b03e134218a | -5.5241 | -43.8878 | 2025-07-15 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 394bd5c7-c5c4-3c62-919e-e808bba90260 | -11.4397 | -45.0923 | 2025-07-15 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7a284771-4f02-3ca2-a3c4-7c954287a599 | -9.2928 | -63.719 | 2025-07-15 01:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 8dd638a4-c2e8-3f9e-b687-8c32c08e8333 | -11.4584 | -45.1126 | 2025-07-15 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 5c2dee9d-0a45-39ba-a9fc-5e7314253be0 | -11.4393 | -45.1154 | 2025-07-15 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 824b00e4-7f35-341f-a391-341489326a8e | -11.4592 | -45.0664 | 2025-07-15 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 380c3111-70db-35a5-8102-765b8cdae2aa | -11.478 | -45.0868 | 2025-07-15 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| cee9b848-4198-3a66-8b67-d45650f8b915 | -10.5776 | -49.1316 | 2025-07-15 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| be6db986-4b68-3f77-9c16-aeabc0f2c861 | -11.4393 | -45.1154 | 2025-07-15 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 8e59b4b4-7553-3092-8f47-ba7871421c32 | -11.4588 | -45.0895 | 2025-07-15 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 4b9d3b69-8e61-38c8-aeda-90616063d735 | -5.5241 | -43.8878 | 2025-07-15 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| f0bbaca6-e143-3055-86d1-87c1ab8de31a | -11.4592 | -45.0664 | 2025-07-15 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 61a93268-2695-323a-ad81-74b81f1a0a8b | -11.4397 | -45.0923 | 2025-07-15 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 41ffe57c-203e-327f-b249-f30482bd3b15 | -5.5429 | -43.8864 | 2025-07-15 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| fb607e22-3fa3-3076-a9df-8d6e05802fec | -10.5586 | -49.1337 | 2025-07-15 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 3cd70c4c-2240-3f55-959b-d9d502587425 | -5.7754 | -45.1053 | 2025-07-15 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| dd6c6a28-606e-333b-be0f-22412cd07c6e | -11.4584 | -45.1126 | 2025-07-15 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 76e5117a-e542-3263-8668-1403001ae3e5 | -10.5586 | -49.1337 | 2025-07-15 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 5a3c3173-ebb1-3a28-8569-404074768731 | -10.5776 | -49.1316 | 2025-07-15 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5781c425-978f-3619-adcb-97b741e2dd83 | -23.121 | -50.0011 | 2025-07-15 01:40:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 427cdd96-0f3b-35fe-8e00-0d750f2be490 | -5.5429 | -43.8864 | 2025-07-15 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 93b62767-16c4-3415-8e43-5b9f324330af | -11.4397 | -45.0923 | 2025-07-15 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d2454dcc-6252-3175-b344-11d5342dae4d | -11.4393 | -45.1154 | 2025-07-15 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 2953c842-a41c-3689-a814-197f27fc4042 | -11.4588 | -45.0895 | 2025-07-15 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 280.8 |


[Clique aqui para ver as próximas entradas](README4.md)
