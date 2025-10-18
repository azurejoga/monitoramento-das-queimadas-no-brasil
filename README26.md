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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a4fdd07-f4c8-34ec-b3f3-42a523cafd06 | -12.91951 | -41.83614 | 2025-10-18 04:02:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2827889f-761c-3c13-b874-61771e1df4cb | -10.25394 | -44.03653 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 215e665f-f143-39b9-af04-0225c99cf01c | -10.96115 | -45.4547 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95a8e065-e797-3605-9659-6bbd8be98501 | -6.5955 | -46.69192 | 2025-10-18 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79956590-0d12-30bd-a002-da76de36ec5c | -13.45292 | -47.93198 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 117ecfc9-49dc-36ca-83f1-11f7184f3b08 | -10.15578 | -44.53197 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 299f3594-f8f8-3dff-87b0-7ad3841c855a | -10.49869 | -47.54379 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3150f0dc-e815-34e4-b942-6f3cdd73fbfa | -10.61804 | -47.37976 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5bbe627-4fdd-31fd-bfdb-69a3cc0293c1 | -8.54421 | -50.08313 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cfc2d75-1229-3b88-8cfc-aa92bca56fc3 | -8.36349 | -46.23896 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8a4eb3b-ce00-39c6-b06d-9b7dfb9010d8 | -8.22519 | -43.3097 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f8e445f-87b5-3177-8995-ae3e4b530605 | -7.57819 | -44.98154 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f098661f-b762-3493-b298-b15ecadc6385 | -7.65957 | -44.64222 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03fb2169-5763-38d6-9548-dab77e84eb92 | -10.48836 | -43.39979 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aadff5a3-9154-3040-a9d7-00ea5e09c57e | -8.7972 | -40.4369 | 2025-10-18 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ff3e38a6-38f5-37f6-9e40-8fbce077e749 | -10.09211 | -47.65586 | 2025-10-18 04:02:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f81e26d-2901-3773-995f-349521819b99 | -12.68954 | -44.40738 | 2025-10-18 04:02:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1278cb1c-56a2-3b57-be97-9566b0fe5d62 | -10.25533 | -44.02832 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42785d3a-2d8f-328d-89e7-096ea8d0a49c | -10.94952 | -45.45285 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9697355e-abd8-312b-aeda-416c03471829 | -11.61184 | -44.09194 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 583ce295-67d9-3f7f-9a80-dde99bfc185d | -8.20344 | -43.96433 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d38098b-2fde-31c3-935c-757e6945cb24 | -13.02588 | -46.94877 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b9bb437c-f7b8-3f93-9803-52b83e9b1f4e | -10.41767 | -47.73799 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d34558c9-496f-32c8-b3fe-855ba6774848 | -10.95343 | -45.45326 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0dbe7901-c7db-31c7-a0b4-9908703edc05 | -10.97441 | -47.92501 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c3c4581-393d-3f56-b978-c59cda0198d3 | -8.3693 | -46.20718 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 539cb9a7-4e77-3f7d-8519-cc2d8b8b5a04 | -8.82479 | -49.68482 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1de9907c-4866-362e-8640-de8568e6b665 | -10.43133 | -47.74002 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46bc24c6-9cac-337c-b684-4d21096dcb3e | -7.00169 | -46.99217 | 2025-10-18 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 885cf70e-ee42-346b-a22d-b1d33e271907 | -12.46553 | -45.46293 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdbaa182-ca42-3200-8fb1-9f91458fc8e8 | -11.49219 | -44.22236 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ba9e83-984b-39c0-9c35-5b024bdb264f | -8.33779 | -49.97165 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a47cee5-f1e9-3c2b-a7c5-aac4ffdf4fea | -8.04715 | -44.09209 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32d80c64-c146-32fd-9a16-9c500d1403e7 | -6.42909 | -47.29536 | 2025-10-18 04:02:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 655eb4f3-ec1c-307a-a0fb-300825107b73 | -8.5394 | -50.07844 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb5f4a5a-51a2-3ef9-8546-7bbfacb1fa77 | -7.17127 | -42.36277 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d8e18384-0606-3143-b16c-b728bb1f1b0e | -12.87652 | -43.4428 | 2025-10-18 04:02:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1766ddcc-ae34-3006-9a2a-a442ef7a1769 | -10.62822 | -42.3054 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f014a365-741c-39a7-8b41-7ebd2d34e016 | -14.02243 | -44.69161 | 2025-10-18 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0484bb38-29ee-3410-923f-0aa88383276b | -10.94736 | -45.44217 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 276c54f0-3a7a-33ea-964e-3aece4e040e8 | -11.61322 | -44.0837 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c38be817-4c4a-35a3-b060-56db364b4d92 | -10.25478 | -44.04594 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e3101c8-175b-3c7d-b176-eb5a42894153 | -8.46685 | -40.61092 | 2025-10-18 04:02:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93273ce0-a4bb-3884-967f-6ce7a60de319 | -13.70965 | -47.71887 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dbd0a1e-f6b0-3c22-be2a-7e15932c414d | -10.96636 | -45.47096 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0d57b9a7-fa47-32af-9880-03def2617ca6 | -13.76493 | -48.23689 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1560bcc8-705b-35e5-981b-dbad594b9818 | -9.91576 | -47.66142 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3caa3f4a-2141-3bb9-9ad0-73280a1dfb00 | -10.25617 | -44.0375 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92150d33-7af8-3033-aaea-50d5ad5c0aa2 | -10.15652 | -44.52753 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3b84790-44fb-3ee6-8bb1-a1d32600e0f2 | -8.60732 | -40.19397 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 54536b90-4704-37dc-8fbb-a42c92001ee3 | -10.50931 | -43.40332 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d03f4ba0-f7ee-37d8-817d-73a744f78083 | -12.46932 | -45.4636 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f779030a-2ee4-383a-9a94-2dad6954fafb | -13.02785 | -46.94575 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3ba5d170-9e75-3850-a8e1-4a72cb346bfe | -10.49431 | -43.45036 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 20022abe-fd2b-3ef7-8c91-04e160d1977c | -7.59103 | -44.99631 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78ec3c6e-4c32-35b8-935a-c784844cea48 | -13.226 | -43.98303 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1504dca-f711-3d95-91b1-093ae1b776a3 | -11.37312 | -45.27194 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48f0788d-ce14-38da-8d72-d0ce50d54b2b | -11.37392 | -44.25548 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a93addec-1fc4-3f05-9815-6f3f26243d01 | -10.92336 | -47.97368 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2edff7dc-489f-3ff6-8034-d0219bd52561 | -13.86431 | -45.46113 | 2025-10-18 04:02:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 659e1f82-489c-3a25-91c9-e9be3a060374 | -7.72914 | -47.63839 | 2025-10-18 04:02:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6f6b96b-0cbc-3a4c-aaca-e0b7c224590b | -8.31647 | -43.41649 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5b159574-3b23-31ce-b8b0-5431bff693b1 | -13.77462 | -48.23381 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d89b5bcf-4d91-3392-86a7-ce57ea7a3967 | -10.6288 | -42.30176 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 551d37a3-d1aa-378a-95b2-294653c61b87 | -7.17093 | -46.52858 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33418051-f098-3033-bd2e-11d54104fd49 | -11.51497 | -44.06369 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79c289d6-16b8-3024-84a4-34691bf36f20 | -7.7525 | -42.50995 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 212c869d-a1de-3a0c-9fd2-b1b798edb3f9 | -8.36425 | -46.2098 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16493576-fb5b-3027-a16b-9787a74b471a | -8.19595 | -43.30924 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2504d118-e792-3e33-9347-6700301b2554 | -8.31528 | -43.44585 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92e77b94-bb77-3d1d-b244-3e9b13df21f0 | -10.70142 | -44.54779 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 544c8748-7317-396c-ae46-b9156b920ed0 | -11.60323 | -44.07775 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86090c2f-3153-3fd4-8e97-58fa9ac38dbe | -13.40319 | -48.59013 | 2025-10-18 04:02:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 801240ba-74a3-3195-94da-195676a3df85 | -13.61721 | -43.96278 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bd35f3c-5976-3fde-960d-02c48176eba7 | -12.72989 | -44.86388 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 919aca9c-2bbb-3830-8131-cb5bd66bb932 | -13.73224 | -48.11687 | 2025-10-18 04:02:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cbf9cc4-5adc-3371-9476-f44988b698f7 | -13.46356 | -43.76144 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c229f82-7033-3e45-95f3-aebf942310c6 | -10.241 | -44.03951 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6decebcc-2042-3e90-89ce-befe92f48060 | -9.61213 | -49.67779 | 2025-10-18 04:02:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75b1d547-f381-3f50-a1d8-caa3378d2043 | -11.40422 | -44.2737 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaae2684-723b-34e2-8f66-870e7ee69d59 | -12.16862 | -45.08706 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e59d784d-a8be-3e91-91fb-c911780f5fc7 | -10.14393 | -44.5344 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0260da1-ebcc-3591-9460-b76c667a8c18 | -13.53126 | -48.00043 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ead41f47-c20a-3256-92d4-be929fa48948 | -13.04565 | -48.19582 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba53ab06-6161-3a85-8a5c-929c1b41acac | -11.48376 | -44.27285 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acf3c725-0335-3c48-ab78-984c84293410 | -8.38624 | -46.23372 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f42af622-18c7-3688-b0fb-bc1c040230ae | -7.71121 | -47.85287 | 2025-10-18 04:02:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2279dc5f-b669-3144-86df-a7dc6c9ec6a8 | -10.1639 | -44.529 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 15ed4588-2bb6-3571-a19c-9b583e2242cd | -10.25323 | -44.04071 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1184d64-81e0-38bd-b4b5-a905c0611d03 | -14.09378 | -43.63172 | 2025-10-18 04:02:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0af2814b-9a39-3e70-9e55-a1b4b7b5e659 | -10.88432 | -44.39681 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d80a8bd0-b0e3-37c8-9ee5-89d379aa2315 | -12.46471 | -45.46766 | 2025-10-18 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| daddaac8-36b4-3670-9188-a47fa2ddde60 | -12.98706 | -48.46029 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d9caf8d-e13b-30c7-81d6-a91c21ff44d3 | -13.71224 | -40.98602 | 2025-10-18 04:02:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7db83d60-20c1-3568-976d-7d7915e75067 | -7.14423 | -46.42112 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 383b7fe4-6dac-388b-8cf7-f897edfd30d7 | -12.59354 | -43.02108 | 2025-10-18 04:02:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7bd12c0f-5a4c-35d8-b665-e35b992c8935 | -10.81681 | -43.93306 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eff9b0b-de67-3593-93b9-49774082e985 | -10.6215 | -42.30429 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8359a2d1-d9fb-3998-a068-ab4b01338486 | -13.22667 | -43.97909 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1bc74e6-86bd-35cb-bdbb-aff8078b3376 | -6.93318 | -43.69765 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README27.md)
