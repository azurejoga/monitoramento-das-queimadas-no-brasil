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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cbd05f2-f03c-3873-b39d-61e2ffacbd43 | -11.34847 | -42.28035 | 2024-11-21 12:50:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 32.6 |
| fd45ad40-cac9-3edb-ad43-3f78d4ac02b1 | -7.25396 | -48.42463 | 2024-11-21 12:50:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8fcdb056-1305-3f5f-9f07-dd7982e4b202 | -7.67092 | -47.8249 | 2024-11-21 12:50:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 302aa8f1-d792-3a6e-b9e3-48167796bd22 | -7.07306 | -48.77913 | 2024-11-21 12:50:00 | TERRA_M-T | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e6047a92-d97f-3d54-a7dd-515ca33625a3 | -10.42828 | -44.49149 | 2024-11-21 12:50:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c1376133-d99f-3d64-8da6-d12680dfc3be | -8.39477 | -48.04807 | 2024-11-21 12:50:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3e569086-31df-38c5-8d1b-152bf23b46c5 | -7.2778 | -48.63846 | 2024-11-21 12:50:00 | TERRA_M-T | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 44698dcc-6e2d-3728-a120-42cefac2d05a | -11.35148 | -42.28609 | 2024-11-21 12:50:00 | TERRA_M-T | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 37.1 |
| ca65b5bb-3c33-34f2-87d8-03856a1953ac | -7.47718 | -47.17554 | 2024-11-21 12:50:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ef1b8f0c-6656-3bd4-ac0b-dbc70f7aa772 | -7.0351 | -48.79193 | 2024-11-21 12:50:00 | TERRA_M-T | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 63fa8b4e-c530-3dbd-80ed-b26381588f57 | -10.98682 | -45.11629 | 2024-11-21 12:50:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 77dc518c-8cca-3438-8581-64c5b66fbc0c | -10.74087 | -44.90191 | 2024-11-21 12:50:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 631db79f-d310-3932-8841-d1e0c073b894 | -11.3449 | -45.00853 | 2024-11-21 12:50:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 5f8ee3fb-0cb4-32cb-a246-2a0b47c86955 | -7.47577 | -47.18553 | 2024-11-21 12:50:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9b8a6210-0649-3faf-8608-c031edb3f466 | -8.40253 | -48.05883 | 2024-11-21 12:50:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bccefb1e-9c37-369e-a942-d919d3f79d70 | -8.39345 | -48.05752 | 2024-11-21 12:50:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c2e5134e-933e-3649-8cf2-087d50fef8db | -11.34288 | -45.02421 | 2024-11-21 12:50:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f07a7553-5a15-321c-a8c5-64b0e1cba63d | -10.4186 | -44.47345 | 2024-11-21 12:50:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 531e6d1b-6fa3-3ba7-83cc-f0c3b5549cf2 | -8.93367 | -44.25272 | 2024-11-21 12:50:00 | TERRA_M-T | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 887bc1fc-cd27-3207-9094-d4d9baa9d397 | -10.42274 | -44.49705 | 2024-11-21 12:50:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9fe6ff11-1ea2-3556-93fd-0d710fd39578 | -11.06491 | -44.77246 | 2024-11-21 12:50:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| aceb5ef2-6a4d-393d-8a5a-414d1e67b7a6 | -10.43045 | -44.47498 | 2024-11-21 12:50:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 42386a0c-3b3d-3ceb-aaa8-f45f5af46d9a | -10.21835 | -51.44593 | 2024-11-21 12:50:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| f202e44a-352c-3478-b6c0-c1738fd54792 | -10.06715 | -44.26546 | 2024-11-21 12:50:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| c607be59-a362-30ad-91b7-c385f77b7285 | -8.24806 | -40.23515 | 2024-11-21 12:50:00 | TERRA_M-T | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 9557a745-5edb-376d-acf0-c4666bb706af | -8.33268 | -50.59367 | 2024-11-21 12:50:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e4dcd5ec-41e4-31c5-ace7-23cd972bd32f | -10.41643 | -44.49008 | 2024-11-21 12:50:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 4260bab6-e0f1-35df-9253-0afb56704ed4 | -9.80091 | -51.7026 | 2024-11-21 12:50:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 94e18f19-e6a6-3fdf-8bc7-678745c1f08c | -15.55929 | -41.44662 | 2024-11-21 12:53:00 | TERRA_M-T | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.9 |
| e295de5c-29d4-3f53-a3f8-d5f291e3a949 | -13.62125 | -46.5502 | 2024-11-21 12:53:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 54dba8af-2b83-33c4-ae46-29102be79915 | -12.01096 | -47.46094 | 2024-11-21 12:53:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8fe897f7-a28d-3fb8-a696-aad3455887cd | -11.20957 | -49.59365 | 2024-11-21 12:53:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d546c66e-6eb3-36c2-bbb9-9eac2efcf521 | -14.85493 | -44.86396 | 2024-11-21 12:53:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 026d7c82-57f2-384c-b104-f70df51c35b9 | -13.59522 | -48.94066 | 2024-11-21 12:53:00 | TERRA_M-T | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b695d2ea-ac54-3641-bcd8-f1409eefe207 | -13.24064 | -49.82748 | 2024-11-21 12:53:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 65b4d1e4-6ed1-3123-9cec-3c64c260e0b4 | -13.24647 | -43.65799 | 2024-11-21 12:53:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f3c82cea-392f-31a6-86d2-d476855a48ca | -14.84963 | -44.87635 | 2024-11-21 12:53:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 833f905c-6d67-3a1c-b641-f81e4eae81dd | -12.82588 | -48.44545 | 2024-11-21 12:53:00 | TERRA_M-T | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b10ba3b0-7105-3bc7-aef6-71909bbbd048 | -13.25016 | -43.65185 | 2024-11-21 12:53:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 483687ae-6cfb-3cb8-bca6-703f800704b2 | -12.00948 | -47.47195 | 2024-11-21 12:53:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8ce13faa-0f34-3b1e-97d5-3ecba43b3f59 | -14.91319 | -47.03693 | 2024-11-21 12:53:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 775f3eb8-11f9-35db-b644-73e76b3223e4 | -15.90791 | -51.54723 | 2024-11-21 12:53:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2ed9d58c-d648-302f-9c27-018f43b1b5fb | -15.54833 | -41.47537 | 2024-11-21 12:53:00 | TERRA_M-T | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 2a9d4d67-be9e-3474-bd38-093d93e6bdd2 | -14.85188 | -44.85777 | 2024-11-21 12:53:00 | TERRA_M-T | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 2427d475-9108-3c86-b5fc-c4dc40132a74 | -15.55187 | -41.44035 | 2024-11-21 12:53:00 | TERRA_M-T | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.2 |
| c30da38b-762f-3f6e-b0c2-6a89f7e91e8b | -11.21085 | -49.58464 | 2024-11-21 12:53:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 1866bea8-1be0-3729-b065-457f37aaeabb | -32.33397 | -53.61241 | 2024-11-21 12:57:00 | TERRA_M-T | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 14.6 |
| f9a3f2f3-2943-3fb0-8705-0d8acd376ce3 | -32.32345 | -53.62167 | 2024-11-21 12:57:00 | TERRA_M-T | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 15.0 |
| 4157fd09-723a-3f45-8c7d-85ac13c2aefe | -32.33252 | -53.62331 | 2024-11-21 12:57:00 | TERRA_M-T | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 48.1 |
| 1d6b2b95-891d-3a15-9de0-81d0e9a8702f | -3.2767 | -53.84 | 2024-11-21 13:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| fc708479-9881-3649-a1ad-e5b7503b790f | -6.1182 | -42.5086 | 2024-11-21 13:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| ac9c87dd-9917-3ddb-90b1-45cd1ab1df19 | -5.4548 | -43.2426 | 2024-11-21 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4edc0c7d-38f3-3c1b-b27f-aae8f5d58259 | -2.0259 | -54.5289 | 2024-11-21 13:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 81fd2f70-8979-3dc8-8c84-033c306c4fbd | -6.1182 | -42.5086 | 2024-11-21 13:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| f647cb63-1d0a-379c-801e-fccbf3ab7590 | -4.3708 | -43.0807 | 2024-11-21 13:10:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 9550b45d-06e1-3a74-a8d3-a509e1007e16 | -2.0259 | -54.5289 | 2024-11-21 13:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 5e2f0ce3-e4c8-3886-a4e6-30f795ed0478 | -3.4858 | -44.3969 | 2024-11-21 13:10:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 37464896-0e87-36a0-9ada-4e597f8c845d | -5.4548 | -43.2426 | 2024-11-21 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2f1ffdf3-4a60-3072-87dc-0ce72e1521a8 | -5.4548 | -43.2426 | 2024-11-21 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 8ca238a0-2bc7-393b-bc51-d55b91f87345 | -2.0259 | -54.5289 | 2024-11-21 13:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| f984ae9b-8ac3-3b18-a812-37b01112672b | -5.573 | -42.5999 | 2024-11-21 13:20:00 | GOES-16 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 185318d6-bc46-30ad-9529-8d85a3dfe897 | -4.3708 | -43.0807 | 2024-11-21 13:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| b020ca00-fb9c-35d8-a2a3-51227e6fee52 | -2.0075 | -54.5292 | 2024-11-21 13:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ff32db72-4876-3fc1-9dc1-e8323cf2e318 | -1.1715 | -49.1268 | 2024-11-21 13:20:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 68895339-b1c8-3df5-b64e-99164f4a18d4 | -1.1715 | -49.1268 | 2024-11-21 13:30:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 15820ca2-7fdc-3977-be2f-da3094abdc6d | -5.4548 | -43.2426 | 2024-11-21 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 9d7adeb9-40f5-3d6f-8c69-d17b3af49144 | -2.0075 | -54.5292 | 2024-11-21 13:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f1c1280b-8257-364b-b5e2-76fe77456fdc | -2.0259 | -54.5289 | 2024-11-21 13:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 6236b4e3-2c50-3aa7-9379-cc85f6377d36 | -5.4361 | -43.2439 | 2024-11-21 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 8c1219d5-c019-3715-a28a-32d64526ed10 | -5.573 | -42.5999 | 2024-11-21 13:30:00 | GOES-16 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 803d5609-74b3-3c64-97d6-48e5436fd367 | 1.3635 | -56.0244 | 2024-11-21 13:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e3b8e24b-85c6-3d03-b241-17d0b0a0be69 | -6.1182 | -42.5086 | 2024-11-21 13:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 8eeca0da-65dd-337e-8cad-962cd7c6ecb6 | -1.1715 | -49.1268 | 2024-11-21 13:40:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 6532a366-5e40-3a2c-b8d1-b13f4254e378 | -6.1182 | -42.5086 | 2024-11-21 13:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 060d3ce2-4c5b-305e-82b2-7daee165cbfa | -2.4101 | -48.6123 | 2024-11-21 13:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1a41d8c9-0c1d-3c29-b186-8e42f12181b0 | -10.42 | -44.4705 | 2024-11-21 13:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 26667243-6651-3961-9e88-e4bf9277791b | -5.4361 | -43.2439 | 2024-11-21 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1d31eecf-7aef-3161-8420-f0350b82699d | -3.6018 | -43.6331 | 2024-11-21 13:40:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| cb92e457-8db4-3c97-9d4f-810685395284 | -2.0075 | -54.5292 | 2024-11-21 13:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| aadfb2b1-0d27-3e2e-b921-c604319f4c21 | -2.0259 | -54.5289 | 2024-11-21 13:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| bb79859f-0654-3839-8b7f-ca2237197fc6 | -8.9241 | -44.2627 | 2024-11-21 13:40:00 | GOES-16 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 619dbee0-45c8-3b1a-ae00-624ce60e2777 | -3.5831 | -43.634 | 2024-11-21 13:50:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 5fafb852-90d0-3842-ace6-fad9af501a87 | -6.1182 | -42.5086 | 2024-11-21 13:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| f4a9c565-bba2-3edc-9d8e-7df9cb13b6ea | -2.4101 | -48.6123 | 2024-11-21 13:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fc3ff7eb-0a0b-3119-853d-b13a6c9e5e19 | -5.4363 | -43.2206 | 2024-11-21 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d8b8e425-a9b8-384d-9ee0-52a8ddeba42a | -10.4196 | -44.4937 | 2024-11-21 13:50:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 04e4ba4e-da0f-3ffd-aa04-1b0c5d3f1654 | -1.1716 | -49.1055 | 2024-11-21 13:50:00 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e9b3eca7-2bfb-3588-834c-7b50b732a1fe | -4.5799 | -48.0349 | 2024-11-21 13:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 88cfd41a-81d8-3820-807a-442846902426 | -10.42 | -44.4705 | 2024-11-21 13:50:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 331748f3-37ce-3be0-a6e7-30f4a6300052 | -5.2538 | -42.6472 | 2024-11-21 13:50:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 6cd5bf52-0f15-32d4-bda0-0b33301e98fe | -5.4546 | -43.2659 | 2024-11-21 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 5bc53994-5456-3142-b7b4-3e3b87428c3a | -2.0259 | -54.5289 | 2024-11-21 13:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 154.6 |
| fce15f99-e56d-3a0b-9e77-cf64ca049a94 | -5.4363 | -43.2206 | 2024-11-21 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3aa1f764-78a5-3064-a735-d3516394d1ca | -5.4546 | -43.2659 | 2024-11-21 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a5ddc178-8e10-35fa-9753-a4a8f1fbd040 | -4.5881 | -49.7055 | 2024-11-21 14:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f857cdc0-0d8f-3f30-b633-a4e5674c1474 | -5.6794 | -43.2725 | 2024-11-21 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b6365dc6-1892-3537-a8d0-eb58bd3ae768 | -3.4858 | -44.3969 | 2024-11-21 14:00:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 94055c62-4ba7-385f-9e89-d318e8064a2d | -6.1182 | -42.5086 | 2024-11-21 14:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 8e781e50-326e-38f8-a9e0-9b0183b10792 | -2.4101 | -48.6123 | 2024-11-21 14:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 0042e911-8d70-3a8f-b450-fc74a0911c9f | -4.3692 | -43.314 | 2024-11-21 14:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |


[Clique aqui para ver as próximas entradas](README84.md)
