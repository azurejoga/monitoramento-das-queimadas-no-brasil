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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 821905e9-e0d1-345b-b5ac-f50e511b7383 | -14.5458 | -40.8417 | 2026-09-28 13:50:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 132.9 |
| 9171e008-5f0e-374a-8ae9-d31ce890885d | -12.155 | -50.352 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 0db759a2-6106-3158-880f-5f3e602520b8 | -9.1584 | -61.4082 | 2026-09-28 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| e67cd611-3464-3fec-a1bf-dfb3f99de247 | -10.8187 | -57.2192 | 2026-09-28 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| b7d1eb2a-0e34-3364-9bcd-2b440d067a4b | -7.637 | -44.6065 | 2026-09-28 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 459c861e-93e9-36a8-92c5-21332a82810e | -8.2291 | -45.4602 | 2026-09-28 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 223.6 |
| e48932da-9526-3232-9be7-2df25f032e78 | -8.9637 | -44.1422 | 2026-09-28 13:50:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 16f2d370-5a25-3154-aa24-9c1f206e6538 | -9.1525 | -49.9639 | 2026-09-28 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| e9b810d2-3288-328f-864e-fe94ebda623b | -11.7316 | -50.6587 | 2026-09-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 72e5592a-484a-34fd-8092-5a376848d7c1 | -11.7513 | -50.6137 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| febad3c5-67a0-3035-8f70-0f3f9818f447 | -12.8851 | -44.7782 | 2026-09-28 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 63764511-903b-3e98-b7ee-5f1d9df7abb7 | -13.161 | -48.5437 | 2026-09-28 14:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| c584b9bd-c34f-3e49-b00f-07694be904cd | -12.7229 | -47.2712 | 2026-09-28 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d373c069-8f89-3f0a-8555-715a5e4b29a6 | -7.8308 | -55.1262 | 2026-09-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7a4fe787-aa59-345a-a25b-8d2a52365cc1 | -11.924 | -50.5081 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 259c3dd2-8e7c-368f-81b5-c7bda58918f8 | -11.077 | -51.3462 | 2026-09-28 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2a56735f-b630-392c-a736-6cbdd5b0eb9c | -11.7319 | -50.6373 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e4615c55-3ec8-3b7d-aff5-12cf047c12f8 | -10.4232 | -53.8219 | 2026-09-28 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c147fee9-958e-39a9-90bd-4ac19005085a | -9.1525 | -49.9639 | 2026-09-28 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 73ce0f32-7129-3ab9-83f5-3bb0f9d18b1f | -11.8641 | -47.1004 | 2026-09-28 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| d25061e3-6bab-3287-b1fa-570a937af100 | -9.177 | -61.4073 | 2026-09-28 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| b0c4c454-17a2-35a2-a96e-ede783748295 | -13.0848 | -47.4423 | 2026-09-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 7f773a82-bb57-3b64-a0e1-b3ad61eb9522 | -11.5628 | -50.5069 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 3a34a4c6-660d-30a4-b080-eab48162cfce | -15.1847 | -46.141 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 1f3f7ca6-4f37-3031-871a-ca1938530432 | -11.1966 | -44.7805 | 2026-09-28 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 286.8 |
| d17fd59b-4bbc-3344-b3e4-2d596f2f0ff8 | -8.2291 | -45.4602 | 2026-09-28 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 32fb19a3-2828-3e75-a442-41e0da5f5ccf | -13.1606 | -48.5658 | 2026-09-28 14:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 6b27d0a5-b4d5-3577-8847-30fcbbc9ff43 | -15.0926 | -53.8862 | 2026-09-28 14:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e1af6274-fba3-34f6-aa8f-5d485357cc8f | -7.449 | -44.6016 | 2026-09-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.2 |
| eacb61bd-4af3-395d-aa24-4f832d4dc51a | -7.055 | -42.849 | 2026-09-28 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| ed4921bf-18c9-3737-9a03-809a9eddce59 | -10.7343 | -48.7661 | 2026-09-28 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 07e160f4-7b4c-3e7e-9261-0b6341e52c54 | -11.2158 | -44.7778 | 2026-09-28 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 7e23d968-ec2c-30f2-b857-9e661c88fa98 | -7.4185 | -55.6301 | 2026-09-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 74e5924d-7c57-3a66-9f42-98a77ec23008 | -10.4043 | -53.8236 | 2026-09-28 14:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4eada840-96c6-350b-8206-be01f98571dc | -8.2859 | -45.4317 | 2026-09-28 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| b1359907-dc44-3e44-9ede-1a2953a3c874 | -12.6643 | -47.3245 | 2026-09-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 1d87e29e-cad9-3a41-bfcd-a749f537b3be | -10.9538 | -50.6592 | 2026-09-28 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| c0ce7fba-1cdb-3605-99a3-8e3c50fda11c | -9.7485 | -48.9598 | 2026-09-28 14:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 65452045-c70f-316d-aae0-4b8a91cdae8b | -9.1584 | -61.4082 | 2026-09-28 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| c8c532c9-7576-3bf4-899d-f82b6acfab38 | -10.7115 | -60.7312 | 2026-09-28 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| bb84f13f-bf2e-3330-a1b1-3cca210e92dd | -11.9039 | -47.0053 | 2026-09-28 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 047a1e5c-3d21-3d5d-b814-926236e8ede3 | -12.289 | -50.3143 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 693dc009-f528-319b-a09b-b2a14ce45df9 | -11.2154 | -44.801 | 2026-09-28 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 8354ff57-daaf-38ac-8a01-4fc5a77c52bc | -12.8059 | -54.0255 | 2026-09-28 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| fd8c470e-fd53-39f4-b381-3451dbd2212e | -8.2293 | -45.4375 | 2026-09-28 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 2095c5c8-8d8d-3cc5-86e2-518be55cc255 | -8.0361 | -42.8187 | 2026-09-28 14:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 4f7ce781-d190-3af3-b003-692d07b6085f | -11.1775 | -44.7832 | 2026-09-28 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 6e700983-b572-3603-8b8a-8377304c14aa | -11.1331 | -50.0409 | 2026-09-28 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 02fa10fa-19c0-3847-8ba1-72db5ffd84da | -8.0169 | -42.8444 | 2026-09-28 14:00:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 211.5 |
| 234ca5c4-5b31-36c1-9f14-b2fbbfc207cc | -11.1327 | -50.0624 | 2026-09-28 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 8d3eb62f-60e6-3c1b-890f-64f762fa49d8 | -7.468 | -44.5768 | 2026-09-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 241d6305-5fed-33f6-873f-b947eedccac2 | -11.8672 | -50.4933 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4ff44cbc-5522-37fd-a931-25740c4c537c | -10.2065 | -50.0113 | 2026-09-28 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| b520a451-b8ae-3ebd-a7a8-859eb44a3c80 | -10.2257 | -49.9879 | 2026-09-28 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e27e2f23-27e0-37a8-ac42-2b1fc59a3578 | -9.6489 | -46.5476 | 2026-09-28 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| d88ad0a0-67ab-33de-89c4-21c3820f00d6 | -10.2067 | -49.9898 | 2026-09-28 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| a35f0106-16e0-3ea8-9670-eb7f9c15cee2 | -7.8307 | -55.1463 | 2026-09-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 2bdf7f08-c84e-3437-8d62-d1a99430caa7 | -11.3771 | -45.4 | 2026-09-28 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 99b7d528-9af4-3a23-a94e-f90bd3aaa9b9 | -8.7267 | -44.8836 | 2026-09-28 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| fa311a55-c149-306d-b20d-3dc2e5084fb2 | -8.9637 | -44.1422 | 2026-09-28 14:00:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 26fa57b1-e57b-3ef7-b164-2acb9373e3fe | -12.2897 | -50.2712 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4c0b5119-1bce-3109-85dd-838c7a7ffca0 | -7.0361 | -42.8508 | 2026-09-28 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 03a0a720-ea23-3a90-8f16-ecf4ef807127 | -11.5352 | -47.3678 | 2026-09-28 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 5d6a3845-5bc6-3b89-b53e-76a64751f4c5 | -6.1599 | -52.8929 | 2026-09-28 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 8dec9c65-f3a2-38af-b6e0-ce2076002a89 | -12.8061 | -54.0048 | 2026-09-28 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 78b316e5-b67d-37f0-a309-0bc7227dd4fa | -10.8944 | -50.8569 | 2026-09-28 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a0b30f81-f640-34c3-854c-34eb3a52e439 | -12.7417 | -47.2909 | 2026-09-28 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 517cab51-6c70-3c54-b2a0-92ed51e37846 | -10.8185 | -57.2391 | 2026-09-28 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 45115db0-e729-320f-bac3-e8844848764c | -15.6867 | -48.2141 | 2026-09-28 14:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 33f143ee-db6e-3fe4-8b15-ef8faf3f6caa | -13.5911 | -51.458 | 2026-09-28 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 168.7 |
| d90dc259-afad-3a2c-996b-4767d1d6a3a5 | -7.4492 | -44.5786 | 2026-09-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 07623664-ea78-3a43-84b6-aacf2abed676 | -12.7868 | -54.0275 | 2026-09-28 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| c89a3992-ae53-345d-90bd-77dd88fbf3cf | -7.6913 | -44.7845 | 2026-09-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 7f6e8553-3bc5-3bdf-af73-ef13ef643ff1 | -7.4869 | -44.5751 | 2026-09-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| e8b04c5e-9e0b-38ff-9b32-507b7484c9bf | -12.6451 | -47.3272 | 2026-09-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 22a674c7-47cf-3e21-8d7c-6961b8b0323f | -12.3088 | -50.2688 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a3ac8336-ef87-3081-a8b9-1c15e7d93ab3 | -10.2254 | -50.0093 | 2026-09-28 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 840123a2-a450-3860-b85f-3cefcdc618af | -8.2862 | -45.409 | 2026-09-28 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| c1976eeb-2d94-3ae5-846b-f2196950cfc3 | -12.7413 | -47.3133 | 2026-09-28 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| a4f97315-59a8-3336-af13-c11811a90f0d | -11.1771 | -44.8064 | 2026-09-28 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 388.7 |
| 540dd2f3-d8ef-3741-b1ae-932b3dae58ed | -14.5458 | -40.8417 | 2026-09-28 14:00:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 0b904344-cc00-3114-93a5-6d48df936462 | -11.1517 | -50.0603 | 2026-09-28 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ee24d517-1768-3c65-b4be-b9c5b1bbe783 | -9.4999 | -46.385 | 2026-09-28 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 7dc602c0-b5cd-3674-8db1-5e039c2167dd | -14.5451 | -40.8669 | 2026-09-28 14:00:00 | GOES-19 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 2b69a7b1-f69a-3f9d-8676-ce63696e14e1 | -12.7028 | -47.3189 | 2026-09-28 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| a2744bbe-7d11-35c8-878d-a2a4b39d52b3 | -12.6878 | -45.0192 | 2026-09-28 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 139ea37a-c8e8-382b-accd-1e666c27a553 | -12.6263 | -47.3075 | 2026-09-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 5394afe3-4643-30b4-b4f9-db5cc057451e | -11.3927 | -43.418 | 2026-09-28 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| bc27710c-b576-3ec9-8423-260d91050a9f | -11.5625 | -50.5283 | 2026-09-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 94057ca0-8a01-3a41-9927-6dd066bfa4da | -10.8189 | -57.1993 | 2026-09-28 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 430971fa-986e-374a-a14a-de3e1d593ed1 | -12.6259 | -47.33 | 2026-09-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 80fee053-dda4-303c-85f8-f92432e1cef8 | -7.7086 | -44.92 | 2026-09-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 37f51fbc-f051-3216-946f-8fc8c708cf25 | -10.8187 | -57.2192 | 2026-09-28 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 8c092f90-525b-39a1-a994-d1efeac1f53b | -12.6836 | -47.3217 | 2026-09-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 1eccf935-59b7-3bd0-8298-99523406a9f1 | -8.9633 | -44.1655 | 2026-09-28 14:00:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| fdb2514c-a70f-389c-980b-2e9f2a69e466 | 1.2613 | -50.6845 | 2026-09-28 14:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5db4ba02-f9f9-39dd-9945-e45a2b173b54 | -20.1966 | -48.5773 | 2026-09-28 14:10:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 331abde9-33e9-36e4-a6e4-564519680345 | -11.2158 | -44.7778 | 2026-09-28 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 8c2ab2ac-86a1-3fc7-9e5d-9b273ac71d98 | 1.6749 | -55.9422 | 2026-09-28 14:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| d4c44ef1-bd51-305b-ba45-dafdff30b6fa | -10.2656 | -44.6067 | 2026-09-28 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |


[Clique aqui para ver as próximas entradas](README77.md)
