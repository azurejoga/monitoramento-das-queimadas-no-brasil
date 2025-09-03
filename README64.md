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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80a33406-516c-32cb-894c-5381c98ee054 | -6.79888 | -52.83121 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbf44601-5d45-30bb-bffc-38331ef000c3 | -6.94517 | -43.28696 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b3ec5cf1-ef0f-3cc3-b330-e692e2bd6b34 | -8.05349 | -52.34642 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c637f4a-df2a-3f44-a6d0-7546c45ecae8 | -9.94583 | -51.62526 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d36e765-d301-30b4-9f8e-8ccf9968aa85 | -7.00099 | -43.24921 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9de697f6-671c-34ad-85e4-ff16ae669271 | -10.4631 | -53.62241 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3758bda2-9536-31ee-9e69-e15ca177822c | -8.87243 | -52.03091 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6250946a-9604-3484-981f-9aef8c2656f0 | -11.96758 | -45.79789 | 2025-09-03 04:46:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fce94e13-88e9-33c5-a8b4-6a134de11c69 | -10.54982 | -50.43246 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30980e00-119d-37d9-acba-8d44f1cc68ca | -7.48411 | -44.80987 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e965bd77-5efe-3092-9f58-eb6a00e5b42e | -10.49897 | -50.32661 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da51faf4-fda8-3cef-8762-8815500b27fe | -6.2318 | -43.38376 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6c2a489-4979-3cc8-833e-3430922f0756 | -5.9053 | -57.73423 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 569bed9a-7641-3b73-9fd7-1286f72fbd1e | -11.58301 | -52.12006 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 019fd648-8ebb-3ad2-bf9d-9897131f15c7 | -10.75058 | -45.27307 | 2025-09-03 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68bd576e-c4b4-39e2-9b44-79cb15714b44 | -6.45393 | -42.38997 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bbd9d3db-47c2-3e6c-8d18-2a7ab1fb9591 | -5.51606 | -42.64391 | 2025-09-03 04:46:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8e9af401-6669-3390-a6eb-c13909ff790b | -7.9094 | -46.45286 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd80d179-54b2-36a0-8b75-3b3006545426 | -7.49181 | -44.82 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ec393a4e-7e2c-3942-a0bd-b8a5f34df80c | -9.42334 | -48.36059 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4ec4b32b-7df6-38d5-b908-bda0d45da547 | -11.91108 | -50.61161 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d99739fd-dda7-332f-a548-c6db9295cc53 | -7.5042 | -45.33447 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b579060-c8ae-3475-9336-903407f0923b | -5.84613 | -44.91149 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cec4885-fccf-3ac8-93ee-e811a2c18293 | -11.01331 | -46.9343 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 270aeda8-3c24-35b6-93b9-8555adbe5da5 | -6.29993 | -43.59731 | 2025-09-03 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 582e3fd0-65cf-33d1-bd6d-6bd38fdfc670 | -8.14319 | -54.93425 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e18b47a-d68a-33d5-b2fe-e09ee4729046 | -9.7313 | -49.00016 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79d90827-3709-3b31-a778-dfb11458c234 | -6.02646 | -46.00816 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4def4c82-9dd7-321a-9ed1-4ccb17c58ba1 | -10.48426 | -50.35471 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d44f7d9-d46d-39f4-bea7-8db3819c5757 | -10.89602 | -45.79266 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 825d078b-7a41-3eca-bb2a-79459e2dbb28 | -11.06822 | -52.08411 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c78e827-acd3-30db-b1f0-43070efb1bec | -11.94455 | -50.59766 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b11bbacd-28ce-369f-8306-bd4083994813 | -10.28457 | -54.26613 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d47e5514-13fc-3957-9667-7a13e88d4020 | -11.12171 | -44.64699 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 589c0e42-4e84-350a-b18e-9bb06c997863 | -7.05133 | -50.86103 | 2025-09-03 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b362f59f-ea39-3fc5-8ec8-a1352034cf9f | -9.75521 | -49.4017 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcfaee48-a49e-3473-b7a4-ff4a44eb5ef1 | -6.27091 | -43.31682 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0846687a-e504-3ebc-80e6-2923d20a6e8c | -7.59685 | -46.22748 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54115673-91e8-3b25-8cb1-98600f5fe0ea | -11.60502 | -52.10921 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 551d0226-3726-3a2a-a566-c9593bd2ff9d | -10.48595 | -53.65235 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bd96f1a-d0b1-32d2-914b-a184cfe4c96b | -6.35127 | -55.5582 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0991fb8-13bb-3c04-91ce-22be75fa0ae4 | -6.84539 | -45.53084 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a55b705-09b2-398a-92d9-1a4b154312c9 | -5.91871 | -57.73671 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85844504-f3de-340b-a419-a18424e162ec | -6.24492 | -43.39621 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45a884dd-979a-3b95-b0f8-300bbd5f4542 | -11.8197 | -51.44513 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6e6e9065-c538-3c24-ad91-9b57af01b4ab | -5.86547 | -57.77872 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e05caefb-3407-31af-b9e3-68219480158b | -6.26525 | -45.06154 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce39796b-1197-3242-b5dc-964ba3a152ae | -6.55108 | -56.19433 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4f74a79-ce97-3b5b-8240-2398903d63be | -7.72033 | -48.73053 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 372d986a-9999-3fc3-be44-6e6aef9a3288 | -8.8866 | -45.82146 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b98268bd-c8a2-397a-a363-ed1e20931d12 | -6.53295 | -42.94257 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f8aaabb-3d95-3b6a-bcc6-d86d57b710a1 | -4.52568 | -54.96888 | 2025-09-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51f57109-2c64-3953-ac6d-2ef0d419565f | -11.58355 | -52.11656 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d261f225-c6ee-3600-ac0a-98ab11f15f37 | -6.24962 | -42.62456 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5aa4d36d-ec79-372e-9ebc-a35d50588072 | -10.54926 | -50.43615 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4eef26ae-ca0c-3f3b-a00d-ed079d45b89d | -7.72152 | -48.72243 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3302cc1e-b1ec-3279-9eee-22ab08f39f6e | -7.70069 | -50.26528 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 095e3dcb-2c21-31bf-b53f-a17a2bbdbc5b | -6.23808 | -42.42971 | 2025-09-03 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a1fc3297-8cd2-3a45-9e2e-c3ad959ce7ca | -9.05628 | -54.95704 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bc57522-991a-3e8f-917a-f9907dbe9bdf | -9.63043 | -47.04729 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 521f3b9f-1cb5-3daf-a5c5-955b78649d84 | -6.51263 | -42.19322 | 2025-09-03 04:46:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d258c840-43b8-3324-bcde-4fd87651864b | -7.0042 | -43.22686 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 95c606d2-fe28-3dc2-aabc-fe83196b5bbb | -5.8102 | -43.22815 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c8ae96e8-2a56-3706-950e-8fb26ab27cf6 | -6.85698 | -52.79212 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d6722d-39e8-321b-97b2-ec63ccde5428 | -10.13832 | -46.25611 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fef388d1-37a2-32ba-a999-8b05ff2d63ef | -6.76048 | -45.91222 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da20fed6-9f84-33ca-beb3-ab2d2b1b8c16 | -7.90639 | -46.44523 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b68076f5-ff52-3b65-9dae-79f5bf287bdc | -9.634 | -47.07935 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 655d62b8-55b8-3eaf-8a8d-9c0dd54fd048 | -8.02165 | -44.04957 | 2025-09-03 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2f7f1e5-a127-366a-9dc2-842b020d8fea | -12.57234 | -44.7792 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2189878-f2f0-32f8-a9a2-9f56dab48d1f | -5.87302 | -57.76149 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bef6757b-3fa5-3aaa-9ded-fce8f821bffc | -5.9045 | -57.7116 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d79b981f-669f-3fa9-a232-292668536d59 | -9.43829 | -46.78873 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d4c4683-b7fb-34a7-bfc9-895c09b4fe6d | -7.72072 | -50.24623 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9ed9a9e-c8ae-3fef-ac3c-317b75210c3e | -6.85691 | -52.81441 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba2cc081-4df8-3802-a771-5798264206ac | -9.63104 | -47.04296 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b410a267-95d0-33e2-826d-b7776a6728af | -10.49275 | -50.34464 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 107b0f02-7600-31dc-81e9-8a8b0c3823c0 | -10.08209 | -48.05839 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6a4fe5d-bc6b-3acc-a632-b4b72bebb620 | -5.86101 | -57.77778 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a7ae5e5f-d781-3166-a347-e512197cd20f | -11.22086 | -55.06636 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6916bc4-0b42-3abf-b832-b8008dfc667b | -10.97271 | -50.91191 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66dce04d-19ab-3846-bcd8-b73ab8a24e2f | -8.88973 | -45.83 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e270e3c-d454-3ff7-8c7e-7e8b52aae3b0 | -6.97181 | -44.35851 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79486f8a-ae60-338c-ad41-d5373b9b1737 | -11.05166 | -52.06005 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05bd1988-b2fa-3dbf-8c15-0b14fd51a5d1 | -6.52989 | -56.19798 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 067d015b-8ff4-34c7-84a2-993c396fc612 | -11.58962 | -52.12112 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 6b862bf2-6d0d-3207-8c35-423ca829120f | -11.60716 | -52.0736 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faca43f5-961b-33ce-9cb3-5791a47c88df | -7.80538 | -45.46281 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a07afb8-ea61-350e-aa86-4b7c426b1e22 | -9.64238 | -47.8581 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eb730b02-a4a7-36a9-9700-a226be08c875 | -9.14313 | -49.64867 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45843c0a-738a-3423-804d-351db390cd91 | -11.58849 | -52.10657 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c71857f7-c015-3db2-8fe9-546a27e7d03c | -6.45926 | -49.52192 | 2025-09-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03753483-9a30-3d9d-96d4-15cbae4d8a6f | -5.80939 | -43.23374 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bda64e3f-7207-30cc-bbf0-3dca3c039fb4 | -9.74646 | -49.41238 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecf76a01-07ab-3893-80ef-4d171a12ba09 | -11.95267 | -45.77267 | 2025-09-03 04:46:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13e6e290-c24c-3d09-95fc-a4b64c3d1b71 | -10.31892 | -48.26579 | 2025-09-03 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54da50f5-2664-3b85-a917-a3c2b01b3a78 | -6.34299 | -45.661 | 2025-09-03 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1572a2bd-5cff-31c1-8268-7e0e5e95dac7 | -10.54414 | -50.42403 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14aa7efa-6e93-3a95-979c-b25465d0a353 | -9.7115 | -51.05252 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ed27730-82e4-3aee-8e85-b57fdf10eba9 | -6.23931 | -43.40097 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README65.md)
