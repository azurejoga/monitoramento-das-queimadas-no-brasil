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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22c5d5b9-6a89-3518-aaa0-3b218047e6e9 | -8.21833 | -61.1874 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d24028f-db12-372d-be4c-5e0ff2556fd6 | -8.21778 | -61.19089 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 279217df-2255-3ef7-aef2-608a93c4408f | -8.215 | -61.18687 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5481edb5-a384-3b4e-a947-921e3dc0da6d | -8.21112 | -61.18983 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71dd4e2b-5dcf-3935-8c02-1aaadff97df2 | -8.16067 | -61.16389 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8440e4a7-fc18-3677-8ca0-7f2b0ab6f9f6 | -8.1579 | -61.26731 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a298d60a-5f5f-3286-9e50-5aba3a6b2e54 | -8.15457 | -61.26678 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5368591-a1d3-3cd0-97b4-c582d7d1a831 | -8.15179 | -61.28426 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98f5f8e5-d9cd-328d-9b6b-1792929882eb | -8.15124 | -61.26624 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b393355-c64e-38bc-8132-f94219450e38 | -8.11053 | -61.26997 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009e21b6-0020-30e6-bf6b-2dea6efbf103 | -8.1072 | -61.26944 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3df2f8c-6c6a-3111-ad75-70edb668eb97 | -8.10443 | -61.26542 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58144411-759e-3208-afc1-c00bed604b76 | -8.10387 | -61.26891 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47f5111e-2191-37c7-95ce-e497b0c53c41 | -8.1011 | -61.2649 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c718820a-fdd0-3de6-aac7-e16420a9fd97 | -8.09721 | -61.26787 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecd321c2-3dec-34c2-8a87-2c13ed6c75d3 | -8.09444 | -61.26384 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c4ede42-3d01-31a3-8971-d6bfcec54ef3 | -8.09388 | -61.26734 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7452b52-3dc2-3cd1-9010-d990a7a20773 | -8.09055 | -61.26681 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9ba22e1-f284-34f4-ba0b-d78cac884cc4 | -8.06725 | -61.26309 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34010fa3-3ec2-3b9a-9e3a-c7edd452122c | -8.06669 | -61.26659 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21263aa3-c270-340e-a57e-acac8a4856d9 | -8.06114 | -61.30158 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78946fd9-5fa2-36d0-85fe-9796c9c5db36 | -8.06058 | -61.30509 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1806c66-77a9-3605-9ff4-f8fd1995ee02 | -8.05781 | -61.30105 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b32b7a1a-971d-3479-a53e-15370717c40d | -8.05725 | -61.30455 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11a93cce-f5a6-3404-9983-b7a919712d00 | -9.34681 | -62.37027 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 680e9ea0-3892-3989-95be-e84eed265ae7 | -12.07314 | -62.62551 | 2024-10-12 05:23:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f6898ef-ef7e-394a-93da-52f4c993e017 | -11.83951 | -62.51754 | 2024-10-12 05:23:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e7af7b0-8bb5-3a80-b05b-a50faee25f86 | -11.80598 | -63.00166 | 2024-10-12 05:23:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd938240-d382-3bb6-8127-642a1ae11032 | -12.30747 | -62.30185 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccfa349c-7e42-3d18-ae86-f4ad9b3ab928 | -12.1578 | -61.84164 | 2024-10-12 05:23:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9887691-07e3-347b-8872-8e65510c2e59 | -13.06578 | -62.26203 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f051d884-1d10-3f32-9d46-ffb27c2afce7 | -12.76577 | -62.2714 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8987526-9e1d-3613-8c57-7316d8d0c876 | -12.76521 | -62.27495 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ce3d279-99e3-3398-80be-1a17481d29ec | -12.76132 | -62.27795 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af2b7730-34a0-3be1-9b58-15c3bc4de225 | -12.76075 | -62.28149 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ddc7705-ee46-332f-a8e4-e41f07a0dd91 | -12.75799 | -62.27739 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8784d59-dd8b-3000-a3f6-560ed86c5523 | -12.75742 | -62.28094 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cd46d49-9b23-3b66-8627-aef718d4bb63 | -12.75686 | -62.2845 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5917e612-8b66-3743-a600-da7deb5c1d72 | -12.73734 | -62.24088 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f53b8d26-442d-3ad3-9241-2786f7466323 | -12.73401 | -62.24033 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd0fbc2b-6b1a-3c24-b8c6-f78edcfbae6f | -12.73345 | -62.24388 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ceb67580-f532-3896-948c-435f19fda260 | -12.73289 | -62.24743 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baee148f-6130-3f2b-a525-b8c2927a4d8a | -12.73233 | -62.25097 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d1c2431-9822-3fe9-8c62-f19a27f3a268 | -12.73177 | -62.25452 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3fa0638-2120-3f0c-b838-183fa33107a9 | -12.73012 | -62.24333 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fe7c06c-47b8-331d-b5b7-29aa21da7bfe | -12.72956 | -62.24688 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4565a9d9-762e-30ef-9b5b-5342c347c412 | -12.729 | -62.25042 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b066221-dad8-355a-a3d0-4b73ff80af0a | -12.73992 | -63.03943 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ef8f53d-1d59-38a1-8964-48149a376bf6 | -12.73933 | -63.04308 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5359d938-d54e-34ba-bf75-70033ab1a905 | -12.736 | -62.86454 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c1dd021-e9ae-331b-82f4-0fa005750639 | -12.73265 | -62.86398 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86e4d038-9068-39fa-82cb-d8bb0412a8e2 | -12.72297 | -63.07456 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ac03bd5-c726-3257-b026-f0fd74728b66 | -12.72267 | -63.0334 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b369fbd4-1dbb-3f5c-a476-e079ff6f3f53 | -12.71931 | -63.03284 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19170281-e613-3287-bbb5-cb7f88e1c548 | -12.71535 | -63.0359 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1edfe662-608d-357e-84e5-d7792ab2200d | -12.71477 | -63.03954 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b7bc70e-127d-3951-bfaf-61093ad6f2a4 | -12.70175 | -62.97024 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a9bc237-dd61-3288-b46f-40a015550198 | -12.69839 | -62.96967 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3f581b3-58b1-364c-8f2e-09cacc698c22 | -12.6978 | -62.9733 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68c0acf2-bd9c-3f65-974d-b804df5ab081 | -12.66274 | -63.08313 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4210b842-9a66-3e9e-b1b3-a1f86e718ecb | -12.59166 | -62.5747 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5e6847b-4ecb-3387-968d-2619a12c6d2c | -12.59051 | -62.58186 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 812f181e-ebad-3706-86f1-2ccbf2185c50 | -12.58717 | -62.5813 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcdd0d33-ffae-3928-a4f3-45eff10c6f18 | -12.57917 | -62.62082 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d74e77c-46f5-3130-9901-fa0214116d0c | -12.57583 | -62.62027 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c4f55e2-65e8-3611-a551-97953b32ed39 | -12.50688 | -63.26749 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 477f11b1-eb71-3977-9e68-4fc73c620820 | -12.48372 | -63.00107 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea4217df-5a1f-375e-b9cc-1a8d0eea1b16 | -12.48313 | -63.00471 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe2eb9eb-45ef-3376-aced-8276f422f684 | -12.48035 | -63.0005 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fb08e3a-b1ea-396a-8eb7-4737d9bc02bf | -12.47976 | -63.00414 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c26934fa-656d-389a-9a57-40ab05d83851 | -12.47918 | -63.00779 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd91d106-7440-3fb5-acd3-0c06dcfe1c62 | -12.4764 | -63.00358 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5456d4d6-95f4-378b-b6ff-9c750cea20ff | -12.47581 | -63.00722 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f39e0855-f8bb-30ee-98b7-394fc3e6f87b | -12.47522 | -63.01086 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e72c6179-3620-3207-909f-00cc6dd99d87 | -12.47463 | -63.0145 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e77f0ba-d0a0-36bb-9d9c-800d70825f3f | -12.47244 | -63.00665 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 265b8cbd-9a70-3fcd-98ae-db4eab24f7d1 | -12.47185 | -63.0103 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d995b72f-7c8e-3dad-b135-003a341acbb6 | -12.47126 | -63.01393 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9cfac96-e57d-3c2c-b63e-ca4f9e546200 | -12.46966 | -63.00245 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3ebe5ec-b5ec-39f1-ad5d-cfbcbd8e18d8 | -12.46907 | -63.00608 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e2f448b-47f0-39f2-a8fe-c1193e2f3350 | -12.46848 | -63.00973 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56b25f2f-a37a-3c1e-a419-84b52da15ae2 | -12.4657 | -63.00552 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01a4eb82-76fd-3cd6-9328-b8a01f2afbf8 | -12.46511 | -63.00916 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29d61727-3302-398d-9e64-e2697c750909 | -12.46351 | -62.99768 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72cbf0a2-7c28-3621-b12e-048cf7ba7280 | -12.46313 | -62.723 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad9089fd-2d0f-3587-b2dd-7031e959b7a7 | -12.46074 | -62.99348 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2414e746-02fd-39a3-8e57-108d83d7e493 | -12.46015 | -62.99712 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc6db42b-70b7-3b13-b66b-540175c25da0 | -12.45956 | -63.00076 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d6a5cdb-9337-3196-8511-f07d3c6a5810 | -12.45678 | -62.99655 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 958cd430-8ea9-3df1-846a-717259c76848 | -6.84599 | -63.03995 | 2024-10-12 05:23:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92b23d8c-4176-30fd-8b25-61ad974e149e | -12.45619 | -63.00019 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b39a3d5-3831-3709-96f0-309ebb6826c1 | -12.40093 | -63.0136 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9ca0d71-2a3f-32e7-8737-808320f1f5b7 | -12.37984 | -62.97271 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14de8819-6eb2-39ae-8fed-312e31e8cd16 | -12.37925 | -62.97635 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87426be3-94cb-3b3e-9f63-470a39e9200a | -12.37808 | -62.98363 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e65855da-9826-3f04-91bf-b8a130072f46 | -12.37706 | -62.96852 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18ee54cc-f9c8-38fc-938f-0779dd045644 | -12.37647 | -62.97215 | 2024-10-12 05:23:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5810f842-b0d5-3d99-93a6-bb85e40efa66 | -12.94948 | -62.52019 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b6ac6c4-d47a-386d-9bdd-d508298916fa | -12.94738 | -62.61883 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ca0cadb-b18f-39f1-99c1-d4ad2db65cef | -12.94614 | -62.51964 | 2024-10-12 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README115.md)
