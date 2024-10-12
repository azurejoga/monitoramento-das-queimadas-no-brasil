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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 009d53c5-1206-3eda-b194-1d74f21f0937 | -8.05636 | -61.30108 | 2024-10-12 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3492ee19-5be3-3514-846a-62b37cfb50e5 | -8.97212 | -62.3648 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30c9be66-f8ed-313e-9844-f25340814024 | -8.97189 | -62.36153 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad33988f-57f5-35a9-a2b3-5bd237c3fc53 | -8.97119 | -62.36993 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f1bafa8-c660-3c5d-bde2-db6b7de5d05e | -8.97099 | -62.36665 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94f02835-c9c1-3fb3-ba6c-6a118daee27b | -8.96831 | -62.35886 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb837b6a-9d3d-3330-ad4a-04595e682a3b | -8.96804 | -62.35556 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa5e7383-4066-3135-a1a1-7eb9f017199c | -8.96738 | -62.36396 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62a041a1-771e-33e3-bbbe-c862e4d3ec6f | -8.96714 | -62.36066 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0426d22-0301-3c7c-a52e-46bf5a92d1b9 | -8.9651 | -62.34444 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d06fe29f-4131-3896-afc8-d8b2e9d5d251 | -8.9642 | -62.34957 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2073406b-6776-3111-b5a2-7138d5952b80 | -8.9633 | -62.35469 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1720ebde-692a-3be5-bc0f-905533af871c | -8.9624 | -62.35979 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c69a8d93-26c4-342f-97c9-03b0c0a0b956 | -8.96149 | -62.36494 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dc0ea6e-14d6-3c93-b78b-9e64362c7b41 | -8.96036 | -62.34357 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19462950-8e77-3559-816b-0e680c1ab3b2 | -8.95945 | -62.34871 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 719bbcab-37e6-3863-9f2e-abe27be65cfc | -8.90353 | -62.36018 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cea7bcb7-b053-39ec-bc5d-697af090ddf7 | -8.9026 | -62.36536 | 2024-10-12 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d04e4c4b-ee30-322e-bfd9-6f1e746ef255 | -10.32613 | -61.64988 | 2024-10-12 04:59:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dee3aba-23d2-3bc0-883a-ba3601d909ed | -10.32174 | -61.64894 | 2024-10-12 04:59:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28b5a78c-5bf8-3431-b4c1-7dd7cacc3bfe | -9.96872 | -62.5827 | 2024-10-12 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c578c1ed-d10d-3dea-9ba9-277af825b4a6 | -9.96399 | -62.58181 | 2024-10-12 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b43665d7-387f-3123-b0c5-bccdfc3fd245 | -9.92786 | -62.26035 | 2024-10-12 04:59:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55f296b4-2ac1-368d-8aef-5eebc0920b94 | -9.70426 | -62.3227 | 2024-10-12 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d365661c-fd29-357c-a91a-66db935693f5 | -10.50001 | -62.97635 | 2024-10-12 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df73787e-181a-3406-868e-68c6ebba4b85 | -10.49933 | -62.97429 | 2024-10-12 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36af6ae5-3159-3d51-a95e-b5df14f589a7 | -10.49839 | -62.97932 | 2024-10-12 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39b9d719-5763-3715-b984-0a6fd4a0e155 | -10.49511 | -62.97591 | 2024-10-12 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5246b426-c437-327a-aef3-aaae5bece437 | -10.49441 | -62.97393 | 2024-10-12 04:59:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 507251b2-067b-3c3b-878b-a99911d63902 | -11.95892 | -61.95032 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e3cca8-f4ab-3152-8253-49cfcb1d9b81 | -12.16508 | -63.34327 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d4afd61-8178-3adc-92cb-5ff084505874 | -12.04526 | -62.95507 | 2024-10-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 404a1459-9add-3d1a-affa-1ee6a4a53c75 | -11.93392 | -62.69201 | 2024-10-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f171e75-4cf0-3f47-91c1-67eb2c4dfcee | -10.85666 | -62.32306 | 2024-10-12 04:59:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 587e557b-fa6b-312c-b389-93bc02e0c3fc | -13.06775 | -62.26348 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8c055f6-dfaa-38c2-85ce-27526eef9181 | -12.99556 | -62.4804 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a0bc0ec-7e7e-39f5-b573-2da999039c91 | -12.99111 | -62.47956 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc36e382-5fae-30ee-ba41-55428cf5334a | -12.98579 | -62.4833 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6ba1799-003d-3522-a002-e22203a760d3 | -12.98305 | -62.48347 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7dd1c7c7-f16e-36fb-a2c9-b5aef887f188 | -12.98131 | -62.48256 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 085e396b-54d3-337e-9fe4-cce743d1819e | -12.96998 | -62.51826 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e1ca71-0412-3dc4-a5b5-b2b9517b5f87 | -12.94879 | -62.51963 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b463940b-edbb-35b3-81e5-8afdc2ec1a2a | -12.94432 | -62.51879 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b38d38f-f104-3d66-b9f0-e93ce7349cde | -12.92559 | -62.51997 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8572416-f0a0-3980-a273-e45370d60505 | -12.91835 | -62.50896 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaa69eec-2523-3b62-9d8e-8a61d6d6530c | -12.91388 | -62.50811 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3557b829-6e64-3327-b999-3ea1a3845656 | -12.91048 | -62.52655 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88fd29bc-4b42-3e64-ab64-424f0ba478be | -12.90963 | -62.53117 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e637818-85bd-3dc1-b49a-292401d21d4b | -12.90516 | -62.53028 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 385948c0-cf04-3915-99a0-5c6faf7fcae1 | -12.89982 | -62.53408 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76c0ddd8-a511-310c-8df1-5f86106f5f66 | -12.76654 | -62.27437 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43f4fe48-020d-3775-9bdd-0581083c7d8f | -12.73611 | -62.24112 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50ad15e8-0100-3dd9-8f79-7a2364d0ad74 | -12.7317 | -62.2403 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5226d63-00ea-30ec-ae02-2ba10a79c05e | -12.73088 | -62.24476 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c85bbedc-f308-31a3-9084-bf48c54815c7 | -12.73007 | -62.24918 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40a55146-dd6f-3b65-a3a9-9a1918533192 | -12.72926 | -62.25357 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfab186a-38a5-3bf2-9af9-1d436b43df6d | -12.99046 | -62.73339 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5dff7b1d-8d9c-306a-beb7-63446c021144 | -12.9868 | -62.72781 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9923ac9-3470-37cc-b8e6-41db1276f8ce | -12.97861 | -62.72139 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 660ef06e-d548-389e-804c-c53f9b151877 | -12.97362 | -62.79895 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c42bb59-fe3e-35f4-b8d6-ecd57388c010 | -12.97084 | -62.78854 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f689b3e6-6049-3066-bce2-5460546bfa93 | -12.96995 | -62.7933 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b463edd-5d57-344e-bbc0-a472d2dd17b6 | -12.95832 | -62.65455 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe818069-bfe0-38a8-a958-dd8b7ab72df1 | -12.95681 | -62.65513 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b534424-037e-34e8-ad78-9e74b3d7da3e | -12.9464 | -62.61869 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5d40e49-53c8-32b1-b2a6-3a3fa1dded11 | -12.94466 | -62.61912 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9102ac6-a8a1-381c-bbea-21646d662905 | -12.93063 | -62.72691 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11712a8e-bf5a-3f50-a32a-2226a8916e64 | -12.92966 | -62.72768 | 2024-10-12 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa8012ca-5823-328c-b911-007b8842802b | -12.84601 | -62.90031 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44a3a550-1307-370f-ac0f-a10bac133b98 | -12.84143 | -62.89937 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 135c2e91-b607-3d3e-9c5a-432bcf9654c4 | -12.82491 | -62.91133 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75e24085-2c0d-367b-a21e-a1fc4e515d92 | -12.82031 | -62.91048 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c611bec2-a9f7-3eec-bd67-14935c091ee9 | -12.7399 | -63.04096 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0e89cce-2c46-324b-a2fe-bc0a64d155be | -12.69992 | -62.97177 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dee63f96-b18c-3d7d-aa13-43c46a8bbdbb | -12.4815 | -63.00144 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34a10d22-f2f4-3f96-a6eb-6d2f91adc4a7 | -12.48056 | -63.00649 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1901639e-b864-3af2-ad45-6eaa6f546b3f | -12.4759 | -63.00561 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b62670a-1e19-3d50-9664-ad31aba8a766 | -12.47495 | -63.01065 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65de05c1-c44a-390e-9b0f-bf3836d05090 | -12.47401 | -63.01568 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e76dc5d3-2322-37c0-8a1e-6036c8d82c75 | -12.47124 | -63.00473 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e622ff4e-9678-39bb-a808-9f59ba582349 | -12.47029 | -63.00977 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea092ce1-bf17-34d4-ae57-012fbbcd63cb | -12.46564 | -63.00888 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e581b97f-bf9b-3c23-bc3d-943801c75e5e | -12.46077 | -62.99519 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f0255f4f-6186-3e2e-8748-e42862a05fc9 | -12.45986 | -63.00023 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4deaca3b-afc6-3976-a4c9-18cdb309863a | -12.45916 | -62.99205 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d052bd5-8a7e-3a59-a839-ce1a1f17d1c6 | -12.45821 | -62.99706 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ae384df-f771-3863-81d9-539796d4327c | -12.37879 | -62.96926 | 2024-10-12 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16a40ec6-d2dc-346d-9f41-57b2e5f634e3 | -7.83616 | -63.58625 | 2024-10-12 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97d0d154-1c25-3e9a-b2f7-22595ccebc2a | -7.83557 | -63.58951 | 2024-10-12 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb774984-89c7-3840-8333-1f987b848edd | -7.83499 | -63.59278 | 2024-10-12 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8c7763c-cae1-3a72-9637-e79782053269 | -7.83032 | -63.58857 | 2024-10-12 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afacbae4-7e39-3dac-abee-8e9cee78c3da | -9.29189 | -63.20994 | 2024-10-12 04:59:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0dae4aa-78a6-368e-b82b-acf794c8702d | -8.40808 | -63.83257 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 944ceb38-9720-3ea6-be66-ce5436840ea0 | -8.40747 | -63.83588 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f08255b3-3669-37b7-afcf-e507e0df913f | -9.02824 | -63.6102 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f993a1c-df98-3bbc-be71-f6547f36f315 | -9.02766 | -63.61333 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa357510-91d5-356c-9036-3e8b1a17fbd1 | -9.02308 | -63.60926 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6eda3c8f-c8b5-3022-a10d-2fe291ae9811 | -8.99282 | -63.48533 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf089a6f-ff9f-3522-a6a5-80629758de2d | -8.9904 | -63.48382 | 2024-10-12 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5b73d78-19e5-3098-8337-d7e1bae73704 | -9.51069 | -64.30889 | 2024-10-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README85.md)
