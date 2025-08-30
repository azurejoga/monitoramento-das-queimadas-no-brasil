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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d53057ba-249d-3467-a486-04f37abc41c2 | -7.4463 | -44.8307 | 2025-08-30 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 98fa4d8f-1faa-3d13-b78b-952f362a4a78 | -14.0118 | -44.5614 | 2025-08-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 502.5 |
| 506378c9-125b-3d98-b9c1-954169475bbd | -14.0318 | -44.5343 | 2025-08-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 4d42667e-4350-3759-83da-ec62b7854692 | -14.0113 | -44.5849 | 2025-08-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 44adf3de-33dc-319d-b6c5-a58638fdb21f | -11.894 | -46.466 | 2025-08-30 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8797ae82-85e8-3977-9b44-cd245106c83c | -13.3623 | -47.018 | 2025-08-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| bbc85d5c-c1cc-3983-b72b-d4ea625517d8 | -6.2096 | -42.7607 | 2025-08-30 13:00:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 6964abe1-b833-394a-8422-70e75371e0be | -11.8752 | -46.446 | 2025-08-30 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9666428e-bc27-3a5d-b0a2-ab63a601a348 | -11.3116 | -43.6664 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1d9c8f9f-04f0-3260-b341-1ea153132c8c | -7.8541 | -46.9747 | 2025-08-30 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| ff004057-eb13-3eaf-98b1-1907d94b41e0 | -13.3645 | -46.9047 | 2025-08-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 604dbda1-71f2-3726-9b0e-9275327a1332 | -13.3619 | -47.0406 | 2025-08-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| df7155c6-295e-3f49-be7f-80e09b0b742d | -7.0951 | -44.3128 | 2025-08-30 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 0247e592-8276-348e-9425-4c8c6eccbd8f | -7.603 | -42.7232 | 2025-08-30 13:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| efa1d23e-a67c-3e50-9195-74c829c4b8de | -11.3312 | -43.6399 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| da473aa1-102e-3316-b18c-7a897810d180 | -14.4671 | -52.0259 | 2025-08-30 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4906a58c-afe0-3cff-9917-2d1aca570d24 | -6.1853 | -43.3257 | 2025-08-30 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 306.8 |
| 82491b47-dea5-3a1a-966f-177a4d59c9e5 | -13.401 | -47.012 | 2025-08-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c4212a2d-4a72-35cb-812b-7843b080aa75 | -13.3817 | -47.015 | 2025-08-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 124.5 |
| e88b13d5-454b-3410-bc83-f2bda33cf65c | -6.1787 | -43.9995 | 2025-08-30 13:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b351828e-fb76-35c5-b7a4-c508466c95fe | -6.185 | -43.3491 | 2025-08-30 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 399.2 |
| d56ca992-d5ea-3220-8c85-1818243e67b6 | -14.0313 | -44.5578 | 2025-08-30 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 8eae04b2-8582-3365-9203-58ccb6b30206 | -11.3705 | -43.5868 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 85bcb5db-7ee9-3a61-aecb-2a98eb635623 | -11.3709 | -43.5631 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 6f7df1e8-4bbb-326b-81ed-84cf3f00d556 | -13.3456 | -46.885 | 2025-08-30 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 17650194-684e-39d6-b248-1b4dd284c9f2 | -7.4278 | -44.8096 | 2025-08-30 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b81e8820-279d-38d8-8516-7402bc93b8b1 | -11.3317 | -43.6162 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 6dfae44d-34f4-3f0a-a1d4-68170079f83a | -11.8952 | -46.398 | 2025-08-30 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| f2a80354-1635-34be-b6a8-8c8a134b5abd | -6.7816 | -43.7632 | 2025-08-30 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e26bea65-523c-3c44-8830-7a598fcba431 | -7.4466 | -44.8079 | 2025-08-30 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b4903edf-9fab-3e7a-8dfe-9d52da6ddf5f | -11.3125 | -43.6191 | 2025-08-30 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 6ceba8fc-3fae-374f-8d82-5d343f62d441 | -14.4484 | -51.9858 | 2025-08-30 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 69db7164-75e0-31e6-8aa6-5ef43b70fd28 | -7.8541 | -46.9747 | 2025-08-30 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 626a68b4-6fa8-353e-bc2e-e84113f92903 | -14.0123 | -44.5378 | 2025-08-30 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b566c82e-269a-3d0e-a89c-214689e3f0d4 | -9.1338 | -65.8067 | 2025-08-30 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| f053f604-d2eb-3972-90f4-9ef02b41ae0b | -11.312 | -43.6428 | 2025-08-30 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 4e39a06a-1fc6-3c86-adbe-4d6b72494d71 | -20.5048 | -57.0861 | 2025-08-30 13:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 118.2 |
| fd0171a8-28e2-3269-acd6-5edda48d551c | -14.0313 | -44.5578 | 2025-08-30 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 665afbaa-7d95-35d6-a92e-7e9637c6241d | -9.4497 | -62.3485 | 2025-08-30 13:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 01140cfd-303b-36ae-a290-81003f8fce60 | -6.7816 | -43.7632 | 2025-08-30 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5ae57733-0bb2-3ed9-9ac0-ff319f7d1ec2 | -13.3632 | -46.9727 | 2025-08-30 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b779540f-7fed-342b-a496-a3197e04a2dd | -13.3628 | -46.9953 | 2025-08-30 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| a14ab612-5aff-3aab-80e4-abdcbdf45c4a | -9.5139 | -45.3884 | 2025-08-30 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| d577b1c3-9e10-354d-9354-d8609bfd681a | -13.518 | -46.9486 | 2025-08-30 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 32df0449-7cd9-3dfb-aa08-5533c97d469e | -6.1787 | -43.9995 | 2025-08-30 13:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3e483526-dc05-3023-9e86-9fc854883acc | -6.185 | -43.3491 | 2025-08-30 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 263.5 |
| b7c0ab38-c961-3845-a364-258ec813cd23 | -11.8764 | -46.378 | 2025-08-30 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| bf60308e-6957-3cec-a783-bbc99ead97d2 | -9.4862 | -48.8346 | 2025-08-30 13:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e550dc38-07b6-3971-926a-bcc6e2a516bf | -11.8752 | -46.446 | 2025-08-30 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 34d49717-b8b1-3196-b829-f86bd8682f55 | -13.3817 | -47.015 | 2025-08-30 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 451f4fb9-ec2f-3f42-bcc5-880536a0c588 | -6.1853 | -43.3257 | 2025-08-30 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 6ccd157e-769b-3556-bc25-27887714c845 | -11.3116 | -43.6664 | 2025-08-30 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 82986103-a191-3f0f-b8b1-fc800f8b5dc2 | -7.603 | -42.7232 | 2025-08-30 13:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 19a608fa-d6ab-3bd7-8807-651aa0ed945a | -9.4498 | -62.3294 | 2025-08-30 13:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 528a7afd-9e3b-3212-a5b2-680b4732c56f | -11.7347 | -51.7618 | 2025-08-30 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 207.8 |
| b3a831f5-04cf-3f85-8817-016ce3d9236b | -13.3645 | -46.9047 | 2025-08-30 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 361c24d8-d412-366c-93f1-3ca376187af5 | -6.2284 | -42.7591 | 2025-08-30 13:10:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 603f5af6-b5d5-3bd0-9338-b3b977aa3002 | -6.1665 | -43.3273 | 2025-08-30 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 341.1 |
| 438e027c-a752-33ff-8464-f99f0827464c | -11.894 | -46.466 | 2025-08-30 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 87fc68cf-1ebd-30df-84be-63aba636c18c | -9.1337 | -65.8253 | 2025-08-30 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 4cd68755-058f-35b9-a572-46b656cd4ce2 | -11.8952 | -46.398 | 2025-08-30 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| eb9e5922-c4b2-3bff-9382-8a2570a3550c | -14.0118 | -44.5614 | 2025-08-30 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 361.5 |
| 3b542db7-9bef-3d16-b7de-5c76b87c1e0f | -14.4484 | -51.9858 | 2025-08-30 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 90e3923c-08ac-384b-b037-6f10f0d31181 | -6.7814 | -43.7865 | 2025-08-30 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 29c04ece-5bc0-3b46-8185-91c18aace9d9 | -7.0951 | -44.3128 | 2025-08-30 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| efe58625-4549-3f78-b1b8-7dd327d03a78 | -6.2096 | -42.7607 | 2025-08-30 13:10:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 220.3 |
| b6a20597-049a-32ef-a45f-f1b8ad26c082 | -13.3456 | -46.885 | 2025-08-30 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 83c85206-a0df-38ec-b654-ad6cd6c5500e | -13.3825 | -46.9697 | 2025-08-30 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c92ca824-2fc1-3ecc-bfac-e4ebbce8cc71 | -8.8665 | -45.7335 | 2025-08-30 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 287543f2-624c-3759-b4cf-6cfd4dc13e84 | -7.1108 | -44.587 | 2025-08-30 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 47e7002c-1d05-3e40-98d1-dbcb806cde8d | -9.1338 | -65.8067 | 2025-08-30 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5b8c93b1-93fd-3d5d-9e35-0b8c4789ef03 | -6.185 | -43.3491 | 2025-08-30 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 5b470719-1c51-3393-837e-edc1ef0359b2 | -7.4466 | -44.8079 | 2025-08-30 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a7433ba7-73ef-3f3f-ba42-0b62dd9bf3b9 | -7.4278 | -44.8096 | 2025-08-30 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 64c9d8ab-2b5b-3a9c-94e8-4dedcf865cef | -11.571 | -46.3525 | 2025-08-30 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d2eaa5e1-0feb-303b-8c9f-1b7ed2cff0fe | -9.1337 | -65.8253 | 2025-08-30 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4f4796cb-047c-3268-9cf7-dadcb081550b | -13.3623 | -47.018 | 2025-08-30 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| e907b94f-6c9f-37d7-90e1-3f6bef3c89d9 | -13.3817 | -47.015 | 2025-08-30 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| e419d45f-9545-33ad-bda8-4c565aaca702 | -11.8948 | -46.4207 | 2025-08-30 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 57de02e7-f04e-3e8a-8797-7ee7d30c85ad | -13.4986 | -46.9517 | 2025-08-30 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 9f82d880-4c6e-3d19-b675-0b7ea8fff646 | -11.3116 | -43.6664 | 2025-08-30 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f122a364-9cc7-3e07-bbbf-0ea9575d7d5f | -9.1156 | -65.7513 | 2025-08-30 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2722e747-07aa-3f8b-84f5-f0602c12ba7d | -12.8601 | -48.188 | 2025-08-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 0a03270a-f302-3156-bfcc-283bc4a5e54d | -6.7816 | -43.7632 | 2025-08-30 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b303405f-d598-341a-8801-b01c63d5b0da | -13.3456 | -46.885 | 2025-08-30 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| cd3326fa-170f-3cfb-bb37-a52a146896a2 | -10.7026 | -47.0718 | 2025-08-30 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 491d0cdb-5799-3eb0-8aa2-dbd9bb2ec502 | -9.4497 | -62.3485 | 2025-08-30 13:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 2a9f92c1-5489-34bc-8cea-03674a49f475 | -11.8764 | -46.378 | 2025-08-30 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d9a719c4-6e61-3689-8b20-827c8a03f4d4 | -13.3632 | -46.9727 | 2025-08-30 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 69423873-03f7-3c84-b500-a184a577dba8 | -20.5048 | -57.0861 | 2025-08-30 13:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 108.6 |
| cfd3bf90-0ef2-3af4-a855-510fd2570549 | -6.1853 | -43.3257 | 2025-08-30 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 286.0 |
| e93dd329-979a-35a3-ac4e-091207c27522 | -6.1665 | -43.3273 | 2025-08-30 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 359.3 |
| ca1e9163-c21b-3567-ada0-0fdca028e58d | -11.1523 | -54.3104 | 2025-08-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 118fd387-3935-379d-8de2-7cfe5c90482d | -11.312 | -43.6428 | 2025-08-30 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| f83c566d-f2f0-3f8f-ab7f-8e11398bb3a3 | -7.0951 | -44.3128 | 2025-08-30 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 1c1f030d-f12e-38fe-be9d-dd5c05ad631d | -9.0614 | -65.4355 | 2025-08-30 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9405f130-fcb1-3f64-8ff5-38066385b976 | -14.0123 | -44.5378 | 2025-08-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 373064e6-67f2-3ddb-8ef1-4cf3b21ecea1 | -9.1155 | -65.7699 | 2025-08-30 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 76273bb0-0009-3b4e-8945-8282d1e16c57 | -13.3645 | -46.9047 | 2025-08-30 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 112207bc-8e8c-3c82-b63a-98103d884346 | -11.8952 | -46.398 | 2025-08-30 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 222.3 |


[Clique aqui para ver as próximas entradas](README100.md)
