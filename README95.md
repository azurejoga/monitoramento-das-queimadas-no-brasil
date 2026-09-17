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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dec6949-9375-34c5-834d-c269d280bc1e | -4.5045 | -54.9646 | 2026-09-17 14:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 313.7 |
| 7af95555-1e92-3b44-9a00-67b76dbfbcbc | -9.852 | -46.9046 | 2026-09-17 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 186.3 |
| ff268df4-00b9-342e-9f50-31538b48c9f9 | -12.3766 | -48.4532 | 2026-09-17 14:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 87b74d0d-014f-31e7-a448-e2769d3045e1 | -9.7793 | -60.4744 | 2026-09-17 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c104e351-394b-3449-8661-2d693e71a9ae | -11.3161 | -46.7699 | 2026-09-17 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f840986f-ebbf-37c0-a41d-f172495879b8 | -8.8923 | -62.3917 | 2026-09-17 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 51798360-a561-32b2-98dc-ec701a3916bf | -18.8906 | -46.8284 | 2026-09-17 14:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ca1c8f76-6667-3931-9644-9f20c2af2515 | -8.2831 | -45.6585 | 2026-09-17 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 72be0915-05f6-3b76-8373-6738ca498c9b | -10.0608 | -45.5732 | 2026-09-17 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 4ec10f9b-5b10-34db-91ee-8da77280b3a8 | -9.3569 | -50.1583 | 2026-09-17 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| d9ff1b2e-6f59-3f81-a081-7522dbe0bc54 | -7.8033 | -44.8651 | 2026-09-17 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| aa22d736-9453-3fa3-a9d7-09292df92d23 | -10.0418 | -45.5756 | 2026-09-17 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 206.5 |
| fad36842-ab11-37c5-89a4-a9e3d50928f9 | 3.9169 | -59.6641 | 2026-09-17 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 150ad589-44fd-31ca-9a4d-48f66f5476fc | -9.7608 | -60.4561 | 2026-09-17 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 1d6603ff-ff01-3f44-a282-3331f93eec49 | -8.9108 | -62.391 | 2026-09-17 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 6d1aedd7-f14c-399a-8335-f78bcacc9385 | -9.7794 | -60.4551 | 2026-09-17 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0d45e43e-1cb0-32b7-9b9f-37ff91e7d92f | -9.4325 | -50.1299 | 2026-09-17 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| e427b061-d0e2-34ff-8cfc-a431421e3ce8 | -9.3893 | -60.3022 | 2026-09-17 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fbe0fd35-0a81-3d00-9c9d-0edb56f3616e | -12.7243 | -48.2734 | 2026-09-17 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 105de59e-fc30-3d2b-aaa9-33148091d002 | -6.43 | -60.0108 | 2026-09-17 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 5ea48f10-3ea9-3dfd-bae8-f77dc53138ae | -9.4139 | -50.1103 | 2026-09-17 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 43fea4c9-e0e6-3b25-a99e-aa027672ef96 | -7.1384 | -42.1529 | 2026-09-17 14:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 120.8 |
| db7c26e7-fe2c-3c99-9e77-da6ce427303c | -8.4983 | -57.6271 | 2026-09-17 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 0789a418-f51d-39c3-ad46-f6a1766ba961 | -9.5522 | -48.1086 | 2026-09-17 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4f1c79db-2e79-3157-98f6-d06876cd0984 | -6.6703 | -43.6337 | 2026-09-17 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 24f202e1-6ac4-3d09-8e1e-a5f755a2d6af | -8.4669 | -44.5445 | 2026-09-17 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 7ccedca9-4242-3775-bd5d-afce0287958b | -12.6826 | -54.6763 | 2026-09-17 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 53d9bfa0-8bd2-3edf-898b-e6968eab2b87 | -13.6143 | -46.9561 | 2026-09-17 14:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6799ed82-7aee-33f9-8720-33c4ea85a53a | -10.414 | -48.6495 | 2026-09-17 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| eaee350d-ec96-356c-b734-a684b7f10b51 | -14.8183 | -59.5532 | 2026-09-17 14:50:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f46c13c9-ed31-3e0d-97d9-6aa041ba8782 | -11.3629 | -44.0112 | 2026-09-17 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| ca0d6200-18f1-3509-aed1-5792b3e4b053 | -10.0422 | -45.5528 | 2026-09-17 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 26a14e78-b397-34e7-8cb7-6a0b091431b9 | -7.0084 | -43.6497 | 2026-09-17 14:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 1b87628e-787b-3740-bcc8-3a7f4d46482d | -13.3758 | -51.7193 | 2026-09-17 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 659fc76d-d6d6-3c87-84de-eb15f2bfc2dc | -9.1711 | -49.9835 | 2026-09-17 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 3a55d9e2-7d44-3c58-a9b7-e2624ed83257 | -4.5044 | -54.9845 | 2026-09-17 14:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 387.3 |
| 5c7de71e-180f-30bb-98f1-ab59268c9ada | -6.5837 | -58.8498 | 2026-09-17 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 17f35766-38eb-3e91-8648-184911be1b05 | 4.1516 | -60.6878 | 2026-09-17 14:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 09b3a4e5-a9d6-384e-9ada-d5f4c4d35363 | -7.9355 | -44.8291 | 2026-09-17 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 267d316a-1267-32dc-8fb0-f27cf195caae | -14.1742 | -45.1407 | 2026-09-17 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| b731e695-c2a1-327e-bade-ee7773f91be9 | -4.5229 | -54.9639 | 2026-09-17 14:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 02f0e57f-94c8-3e97-b814-809fdb4e7b95 | -8.4797 | -57.6282 | 2026-09-17 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c5476fa6-4cce-391e-8109-1dcd183d1fbe | -8.8647 | -45.8693 | 2026-09-17 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.5 |
| d9444b32-0e91-3008-b4a5-8746da4e619d | -14.1547 | -45.1442 | 2026-09-17 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| f698e97f-308d-338d-879a-6335b0d70cbe | -4.5045 | -54.9646 | 2026-09-17 14:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 262.5 |
| 4f78a87b-1442-397d-a28b-d4f191f54595 | -11.8928 | -50.0608 | 2026-09-17 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9429baaa-8e34-3521-9a0a-47a4f0d89f5a | -8.475 | -46.8943 | 2026-09-17 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| cc4be4f0-b693-34ed-a948-be9423e8bfd6 | -7.9543 | -44.8273 | 2026-09-17 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 6f42deea-1d1a-3ad3-98dd-9f4940bf235e | -6.6515 | -43.6354 | 2026-09-17 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 1b02dbc3-2084-39a7-859d-96edb32f3c89 | -7.0242 | -59.2374 | 2026-09-17 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 98a8af58-c519-3007-b33c-0ae0d1af446f | -9.8508 | -48.3615 | 2026-09-17 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c9112184-06c5-3b25-af5a-4e5dcbce654b | 3.9353 | -59.6446 | 2026-09-17 14:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| bdea7482-dfec-3fc4-90ea-2c155665e860 | -3.4757 | -54.6972 | 2026-09-17 14:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e61fd3e5-b7e5-368e-bc77-b1f5e6c99a6a | -10.3769 | -49.9723 | 2026-09-17 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 1d72a3a1-ea4f-3a99-b224-01db30fe19dd | -11.8069 | -58.1759 | 2026-09-17 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 251e1878-f166-3a79-b432-55e9cfb28101 | -11.8924 | -50.0823 | 2026-09-17 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b162e725-e7d0-396c-8f6b-2ab21a4deb9a | -14.8376 | -59.5515 | 2026-09-17 14:50:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5b3a10a2-ea59-328a-bd39-88504ca84093 | -13.6531 | -45.97 | 2026-09-17 14:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| fa99a57f-0243-3feb-8d61-bf352c3523cf | -11.875 | -47.5902 | 2026-09-17 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 6cd80259-e47a-3309-8715-2ccf6863fb34 | -9.852 | -46.9046 | 2026-09-17 14:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| a3e5804c-c6ff-3d3a-8124-894b7f7b5da5 | -6.67 | -43.657 | 2026-09-17 14:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 28841789-b67e-3f11-ab27-f43ce37ff5ea | -18.8899 | -46.8519 | 2026-09-17 14:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8fd79325-5625-3702-9d83-c757b4344757 | -9.1056 | -60.9703 | 2026-09-17 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 71f67c9e-c281-3235-8773-83474835bd4d | -7.1086 | -43.1027 | 2026-09-17 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.3 |
| d9a95b31-38dd-3067-a8ea-c842575f5c57 | -9.1523 | -49.9853 | 2026-09-17 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 15a134a3-649a-3577-881d-12c87fd426f0 | -8.9293 | -62.4092 | 2026-09-17 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.2 |
| d4145917-c5c7-3ae5-8189-46daf15c0802 | -9.5512 | -45.4296 | 2026-09-17 14:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0c0b6547-5e8b-3f04-9609-2d6cd30ceb02 | -13.2986 | -51.7501 | 2026-09-17 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 86c14c9c-8c56-38bc-9cd9-21fb430870ac | -7.8221 | -44.8632 | 2026-09-17 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 41709899-dad9-3293-88af-3c9b4c63f7f7 | -7.6414 | -45.8556 | 2026-09-17 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 07e00804-0e5d-3c55-bc9c-5e6dd3fe7f8c | -9.3572 | -50.137 | 2026-09-17 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| dcd35ff8-f844-36b1-a732-8438ba93a65e | -9.8322 | -48.3417 | 2026-09-17 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| f58de359-8bcc-31a5-bfe5-fc2815769bfe | -9.3755 | -50.1779 | 2026-09-17 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4e1be405-953f-35ca-8d97-5918e5b27423 | -12.0905 | -50.8307 | 2026-09-17 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 32661561-b944-3def-a53a-bee19c4f7dea | -9.7794 | -60.4551 | 2026-09-17 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a37bc2a3-9fd2-3a47-8702-0fef3c27d471 | -15.6557 | -52.7366 | 2026-09-17 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 9bf5f0c1-8eba-37f6-97d3-10a3fe7c2408 | -9.3572 | -50.137 | 2026-09-17 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 96a1a99f-df4b-3b8f-955d-0705940e11fb | -8.4669 | -44.5445 | 2026-09-17 15:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 3ca6bdfb-8ee5-33f6-8e8f-b881fc6bd7fd | -11.2113 | -54.1208 | 2026-09-17 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 0925fb47-8d58-37a8-a0c1-209009c4f335 | -14.5558 | -39.6477 | 2026-09-17 15:00:00 | GOES-19 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 206.1 |
| 851e0b36-69df-326a-a4e9-271c91f38d9e | -15.4708 | -47.3484 | 2026-09-17 15:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| d49a14cf-dddc-37ce-9c2e-d317bb5b9ecf | -9.1056 | -60.9703 | 2026-09-17 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 92fdb2e3-f78d-3027-8172-c2e52a8dff0b | -7.9543 | -44.8273 | 2026-09-17 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 5da2f066-0577-3298-a136-46fc5859815b | -14.8376 | -59.5515 | 2026-09-17 15:00:00 | GOES-19 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9f6a5745-c594-3423-b41f-efdc46539b89 | -12.7051 | -48.276 | 2026-09-17 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| e7e8073f-e339-35e0-b2d6-16e988231d92 | -8.8836 | -45.8672 | 2026-09-17 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 9188fad7-7937-3575-8b49-8b80cc05ff61 | -8.1496 | -54.8049 | 2026-09-17 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| d776789e-3f97-3391-a3a6-989c86c4fb89 | -13.6531 | -45.97 | 2026-09-17 15:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| f0e548b2-8895-39f7-9303-62bf0cb6aea7 | -6.5837 | -58.8498 | 2026-09-17 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| dc07e739-b3e6-3fcd-9eac-15046b2b2bfe | -14.1937 | -45.1372 | 2026-09-17 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 9930cbf0-9fac-3220-a210-cfefde442ba2 | -9.0982 | -59.4088 | 2026-09-17 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b89a7ecc-2833-3868-87f7-66616335ebc6 | -9.0868 | -61.0095 | 2026-09-17 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 78b2ba92-cf9d-36bd-98d0-7aa6a64d2124 | -13.2986 | -51.7501 | 2026-09-17 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 4e9b089a-5e00-3e8a-95ab-8b5715a0c348 | -14.5565 | -39.6219 | 2026-09-17 15:00:00 | GOES-19 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 160.7 |
| b4d1a53e-b9af-39af-a983-f35be0b86c45 | -11.8924 | -50.0823 | 2026-09-17 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d97dfbd1-03c9-3e57-8e7e-21b7ef1df94c | -14.1932 | -45.1606 | 2026-09-17 15:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 790c2480-4cfe-39bf-aff7-58a98f786308 | -8.4797 | -57.6282 | 2026-09-17 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 5424dcee-8c96-3709-9f77-5ca717673888 | -11.875 | -47.5902 | 2026-09-17 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 712b4130-6ca6-36d1-8417-794ee777c6e0 | -8.9293 | -62.4092 | 2026-09-17 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 35d633bb-0f27-38cf-b93d-17532c41e2f7 | -15.5202 | -53.8106 | 2026-09-17 15:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |


[Clique aqui para ver as próximas entradas](README96.md)
