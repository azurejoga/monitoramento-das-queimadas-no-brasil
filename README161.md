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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47d505ac-b8e0-3d9d-84d1-6dc652c3ebeb | -10.05589 | -48.17908 | 2026-08-31 16:50:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf81cc71-0990-34db-832b-4bd8e5ec34d7 | -8.86439 | -47.08807 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e222bc4-63e4-3683-b0bb-e6995512e697 | -11.19375 | -45.03978 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b1e06132-6487-3f7c-b6fe-2adb9ce70966 | -11.6345 | -49.41 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a8040d54-7ecd-3489-9192-da9a5a1fbb28 | -9.19306 | -51.56357 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2061e1c8-f8c2-33b8-ab9e-09ff9528ba90 | -8.17702 | -54.92839 | 2026-08-31 16:50:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 832086c7-92cd-3716-95ec-3196173915f5 | -11.25013 | -45.09392 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 37ece4d6-390e-3bca-aa1e-108607401815 | -7.09417 | -45.7776 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dc82f4fa-6572-3dc0-87a0-162f0f6cb77f | -7.79176 | -46.15829 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1aa4a7a2-1603-38e9-8e11-3baaec45b93b | -8.45238 | -47.5528 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a29d835-f340-36b8-b6a2-43997b9436e5 | -10.57114 | -50.38876 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| c005bc95-eeae-38fc-9953-0642876af7da | -11.19512 | -46.1138 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 14a3268d-f228-3e27-a302-cc828096f1b5 | -7.64833 | -46.7364 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 241f8667-3932-3db2-980d-8ddf1d8a538d | -12.09565 | -47.14303 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 766b6437-0ea9-3dcd-90a2-b9a28cdfe04f | -11.17396 | -55.08689 | 2026-08-31 16:50:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fcd5269e-186b-36d9-8e4f-56f72d6a8b03 | -7.61372 | -44.88161 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| f63713a0-05e9-3870-a536-e1fadc309ddc | -11.24738 | -45.14498 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| a11f00ec-3b51-3909-8416-ad1e5d754d8f | -11.02946 | -49.67178 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b710bbc7-4aac-3927-bbdf-d2c5010ba129 | -11.32346 | -45.1917 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ea2d1ae3-16df-33b4-b81b-d936449007ba | -10.81835 | -45.05378 | 2026-08-31 16:50:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0460919d-ee50-32be-877e-6a2b444be958 | -7.93527 | -61.73455 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 55e99d15-f955-3c33-a1ed-e7c42521f72e | -6.0237 | -44.22385 | 2026-08-31 16:50:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0045bdc1-8910-3da9-b2aa-e02b7903401f | -9.13856 | -60.91559 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c1771bb1-3898-36a4-973d-28292d64e0bf | -7.62579 | -55.29068 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 0759774d-02c8-3d40-9077-e9d97fa56e62 | -10.82545 | -50.72598 | 2026-08-31 16:50:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c380ff84-723d-3e98-9673-0e15a8ebf83a | -9.59441 | -47.60744 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dc8ff730-890a-3c0b-ae85-6906bd097b34 | -11.71473 | -47.62202 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 50764f20-70f5-35af-b9f4-cd575db47496 | -6.62656 | -53.17532 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6621e2f4-0ca0-300d-aef2-1d7e7e961000 | -5.6382 | -45.56694 | 2026-08-31 16:50:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 162fc2d5-e8c6-3486-8463-423f7af20898 | -7.64653 | -46.72504 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3340703d-d6f6-3062-9af5-6a34104446d6 | -10.12997 | -50.31042 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 491bdffa-b4b5-3ac2-8118-68e3cc757f91 | -7.91476 | -44.2566 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aa1dc85b-1870-3080-af08-111869df3d74 | -5.58282 | -42.32656 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| a89a2288-89dd-3eed-b24f-70f400d67a63 | -9.20302 | -47.99538 | 2026-08-31 16:50:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 137f55e2-7e45-34e2-8f2c-c52fc98c55f3 | -11.21607 | -45.0869 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 01bfc041-0b00-3578-a10f-2f5c5fd5dd82 | -11.63504 | -49.41365 | 2026-08-31 16:50:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 11e706a0-198d-3f58-b980-3cbb870a4bb2 | -5.30091 | -43.6865 | 2026-08-31 16:50:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b52bec6-bad5-3d37-b1f2-c151ea89dc60 | -8.38698 | -46.46371 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6de94bfb-8b98-31b5-992c-f89e7a3ece81 | -10.86122 | -45.37879 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6eaeb984-73b1-304c-a409-1dd27acbcfa4 | -10.17188 | -48.47158 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7633cd3e-9541-3e6f-8fcb-dbafb65d183d | -7.63323 | -44.92713 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d4da0a67-489d-3d83-8779-9346d67c6258 | -7.46213 | -60.76303 | 2026-08-31 16:50:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 01fce959-364f-30c4-968a-7688d4cb3e81 | -9.65322 | -46.07047 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| d5e4d5c1-bf65-3437-bd3e-c2914c408c17 | -6.81117 | -43.53716 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f3b85576-a9f4-3846-b85c-957b5baebad8 | -11.23391 | -45.37571 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| aea29406-30fb-32f0-b641-f4ff3b6fec35 | -12.46213 | -46.51595 | 2026-08-31 16:50:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dac13e9e-e6f6-3a82-9bba-d5cec4925255 | -9.20486 | -59.41489 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5ee43258-41b8-36f8-be80-c3358aed91fa | -7.52191 | -60.48273 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e83b9a68-b5fc-3254-bbed-a74500d973a0 | -7.61833 | -57.61924 | 2026-08-31 16:50:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fbdcb981-e740-3bf4-a09d-73516afc386c | -11.68016 | -44.8714 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 72c6bb58-7fd8-3e59-9911-013667ec3de8 | -8.04947 | -47.2793 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 32e82fd1-4d5f-39a5-802b-4962f502c014 | -11.18971 | -50.62536 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fbe85ecb-080d-30fa-a77b-b48d36efbb9f | -8.76766 | -45.37712 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 898da406-b29a-3a6c-8753-2fdec761598e | -12.90461 | -45.84126 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b7cfbccd-ed69-3859-8e51-2069230c58e3 | -6.7344 | -45.07806 | 2026-08-31 16:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eb0a152b-2561-32d0-90b3-284577b27639 | -9.65498 | -48.28694 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e13aec61-34e4-3a9b-9ff6-181b0714bbf7 | -11.32565 | -45.18279 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 7618927f-0afb-3500-b39f-3ff462934254 | -7.29878 | -46.17835 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f0f98cd6-77e0-3172-96bf-af692f4fb73a | -9.66712 | -47.94506 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ae9e986d-acd5-37e7-a3e3-3562ff8b5d64 | -4.90607 | -37.43715 | 2026-08-31 16:50:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e0ee8a04-5d34-3ae2-b78a-e8fce8e4efe8 | -5.62703 | -45.5687 | 2026-08-31 16:50:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c5196ab0-8d23-35b4-810c-a1d6cb950583 | -7.35708 | -55.19677 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 85c346e7-5be1-32e0-a4b5-237937137fee | -8.7447 | -46.46437 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3300170e-1631-3c6b-8c9c-0762fbfeaf80 | -11.85626 | -46.7647 | 2026-08-31 16:50:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a34f4479-935f-3436-a3ad-eb44e0c83c76 | -8.75875 | -46.44683 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| eeb343c6-33f3-37ef-ab43-fb60cd32f2e7 | -10.85674 | -45.33021 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a4f5bca6-be21-3981-9de3-27df257dcdf9 | -7.60778 | -44.84466 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e338befd-e552-3ced-a7f1-0731ecdc6feb | -8.12727 | -45.49331 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f2ca0001-b91f-3046-bda3-615b4cecd8e4 | -13.48488 | -57.05637 | 2026-08-31 16:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b83f478-d1e1-38ee-96c4-50b644c859a8 | -11.37433 | -45.19152 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3bf5a2dc-7a8c-3128-94a9-9e46a291d64f | -5.58405 | -42.33723 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 935f0de9-df6e-3cdb-9d5d-dd606f0d56ae | -5.60762 | -44.00141 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1ec7824a-909e-3037-ba6d-6762e96dda7b | -11.79023 | -47.67098 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| e7914124-6e52-38fd-8e65-8ed969a926c9 | -9.97316 | -46.83325 | 2026-08-31 16:50:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4ca2829b-475c-3324-8df5-1235d30c9eb9 | -13.43358 | -51.69519 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 26f98615-46a8-344a-92ca-2e4258d90a4a | -9.58811 | -47.63042 | 2026-08-31 16:50:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8377a69b-4f6a-384e-b986-905ffe5d8b29 | -10.34933 | -49.9712 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 98d95d1b-1994-3437-936d-6abf1413a97c | -11.19779 | -45.06455 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8331df2-290f-37e2-8af8-d0041e48e3a6 | -12.09932 | -47.27674 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d5ec7b0-ae3c-3649-996d-b2b3c39e220f | -10.11568 | -50.3087 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d47aadcc-1132-3157-808d-e81c977e1d26 | -10.12186 | -50.32709 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1f13ef76-05d6-3ae7-b422-ef7924f08e65 | -7.95644 | -44.2627 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5b7c0b28-f8a4-3c36-b365-cf65d345eb02 | -11.34033 | -46.03547 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| b0f23577-a3b3-3553-9e24-c03b8a64ba65 | -8.15883 | -55.41888 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3cdc41ba-c66b-3623-80a5-b2fadd2e8aae | -7.602 | -45.00009 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0cbcba0f-3357-3687-8edf-1a945312b0f9 | -8.76404 | -46.45775 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 41d6814b-0b76-30bb-a7d1-d2b83df91f88 | -11.23584 | -51.25439 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 60a7bc1d-1538-3b2e-915e-7ff7e2e5cbe1 | -12.10023 | -44.99839 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| cd4e03c2-0554-3dc0-9749-33bf3fedddb3 | -10.09964 | -50.29183 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e8cd4aac-2257-3f1d-85b7-c9af7bec42b0 | -10.8659 | -50.487 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| aa27982c-e525-36b3-a277-ae243bd0458a | -11.32481 | -45.2 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 84e627a4-a461-31c1-80f2-ee111787a22b | -6.87311 | -41.65081 | 2026-08-31 16:50:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| ff5e4f25-4e8a-3ba9-bbbb-03102a9f2202 | -7.58019 | -61.32599 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 865f0496-2de1-3efb-8101-5bba47352b8c | -10.13136 | -45.84149 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d7a85687-27b6-3b8b-9aca-06504469977f | -9.47064 | -57.02605 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4433e42b-436b-32d2-a6c5-0ce7a81497b3 | -8.45348 | -47.55991 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d747314e-6248-33d4-b63a-1c9e69fb3713 | -10.40339 | -45.08557 | 2026-08-31 16:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b4b25782-77b0-3ba9-83bf-73694dce09bb | -5.30156 | -43.6904 | 2026-08-31 16:50:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7851ce3e-aceb-3131-9285-588334e6eece | -7.62961 | -55.28572 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 1effc377-5c7a-31cf-b2eb-8d1708cc7681 | -12.10339 | -47.14906 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README162.md)
