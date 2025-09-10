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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f829256c-4ba9-3b72-bb23-f5272ab3da54 | -10.7373 | -46.0558 | 2025-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 244.8 |
| c4d1c497-a664-3c34-823b-965dd30a048e | -7.4639 | -44.9433 | 2025-09-10 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d339f352-918a-32c6-bf94-a5f8becdd6b6 | -9.6821 | -46.8791 | 2025-09-10 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 170.5 |
| af8efccd-3b5c-33ee-9a4d-09082a35594e | -11.7706 | -50.5901 | 2025-09-10 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 9817433c-11e6-3885-b1b8-abb7e830d454 | -13.1176 | -54.9191 | 2025-09-10 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 1e5a7c44-3f60-3ff9-b136-d1a72fd32fc1 | -14.4816 | -53.4598 | 2025-09-10 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3cfd505f-236e-367d-bc7d-c362f7fcdf0d | -11.7602 | -46.4621 | 2025-09-10 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 237.5 |
| ac38f993-b6c8-31c2-b003-cab2d6d521db | -15.1374 | -52.4039 | 2025-09-10 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 513d98f8-a665-3288-b2dc-5beb174ffc33 | -14.5315 | -53.9553 | 2025-09-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 03f5676f-286f-3c1d-9c8c-6818a144f66f | -15.2686 | -53.7801 | 2025-09-10 14:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 96166b33-e2b2-3c9a-bfdd-b9c99dab810b | -6.8897 | -47.8897 | 2025-09-10 14:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 98eaab3e-6382-31d9-9f79-a5c4356a642a | -10.1464 | -46.1973 | 2025-09-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| ee789596-4bbc-3998-8a9c-92a4b4899743 | -10.7369 | -46.0785 | 2025-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 351.2 |
| 17045c78-f8b1-378e-9edf-21c37b825b95 | -6.3804 | -44.4664 | 2025-09-10 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f7c4df09-e72b-3d8f-a667-58b515a94565 | -6.8519 | -47.9361 | 2025-09-10 14:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 83bea899-a442-3936-9975-e6049e753b75 | -8.0794 | -48.6407 | 2025-09-10 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 4f55db39-deff-3086-82a8-bbddffc4a4ea | -10.3885 | -50.5264 | 2025-09-10 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 9fddae10-efd7-3e73-bc34-e939aacb9679 | -11.4272 | -43.6254 | 2025-09-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 9d9c0c5b-8993-3389-976f-c9fa40df76f9 | -10.0155 | -51.7031 | 2025-09-10 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| d6f34b11-7c3f-30fe-b5a9-73af547a77ec | -10.1654 | -46.195 | 2025-09-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| d333d0e0-8f94-3d94-9a50-a1242aeb03f9 | -6.8895 | -47.9115 | 2025-09-10 14:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 2abbf942-3f7f-364a-b673-0d0bcccca027 | -11.507 | -50.4276 | 2025-09-10 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| d1625cd0-7431-3846-a6a6-e9afdf202950 | -14.907 | -55.8546 | 2025-09-10 14:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9c6d741c-b2ff-3d86-afa6-5eaec978af10 | -9.8649 | -50.1737 | 2025-09-10 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 508ac196-8467-32f8-a776-9d420524f976 | -9.7777 | -51.1366 | 2025-09-10 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| c9f2eedd-7a9e-3644-9c9b-7ba6e70933d1 | -14.8877 | -55.8567 | 2025-09-10 14:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 300a4d1a-cf05-3f9a-ad4e-8b471764f2ef | -11.4702 | -50.3461 | 2025-09-10 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| c4c8613a-326c-3f17-918d-6c27e149b7b7 | -13.1364 | -54.9376 | 2025-09-10 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 200397ae-c3a9-365e-a689-7ba227b9a55a | -9.7011 | -46.877 | 2025-09-10 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 9dd08aba-952f-3831-b1ef-f944c495d3c1 | -11.1693 | -45.2683 | 2025-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 86fe894a-8597-352f-b244-94041cd3b888 | -8.994 | -46.0808 | 2025-09-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| a68f9e04-d6e0-3953-95eb-1860187fc091 | -6.2043 | -43.3008 | 2025-09-10 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 584a1552-ff1f-38e9-9fa0-7bc2d0d2c37e | -15.2881 | -53.7777 | 2025-09-10 14:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 479839d2-37b2-34a2-8846-1b986e8a5ee0 | -8.9943 | -46.0583 | 2025-09-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| a43c7642-98e5-323f-8233-6cd19c67fbd7 | -6.2597 | -43.3895 | 2025-09-10 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 96aaeb94-52d6-37fc-a59a-514a5729f7a5 | -15.655 | -53.8771 | 2025-09-10 14:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 7c4ba98e-51d9-3851-aced-4474ee48843a | -11.4456 | -43.6697 | 2025-09-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| baaf8386-3f31-39d7-b559-6ae6c3213187 | -5.9193 | -45.7492 | 2025-09-10 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 24f95bb7-2400-3048-9248-1fe05c55fdab | -15.1903 | -53.832 | 2025-09-10 14:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 6d982426-fbd2-32a0-bfa7-cad5f0f8e3e7 | -11.1245 | -52.0359 | 2025-09-10 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 235.2 |
| f4843308-4747-3e70-a51c-ad2b87babafe | -6.8521 | -47.9143 | 2025-09-10 14:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 8eb5da60-ccad-3e75-b40e-9b38254c309b | -14.3882 | -53.2826 | 2025-09-10 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a7999931-6f58-30ea-b0a7-5b5a4b68ccad | -7.5546 | -45.2307 | 2025-09-10 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 95309580-a45d-39c2-9731-7e9231157b41 | -6.204 | -43.3241 | 2025-09-10 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 4f862411-f7f8-3dc3-84c7-b1c2684515a6 | -6.3806 | -44.4434 | 2025-09-10 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| c26e6e8d-9968-356c-8747-6fb2db00bdb7 | -5.5702 | -42.9062 | 2025-09-10 14:10:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 8899963d-0e51-3d3c-8810-4acb13c4238e | -6.2595 | -43.4129 | 2025-09-10 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 2ddf0d98-bb37-3b93-8d2c-fb311af8ea2b | -10.1467 | -46.1747 | 2025-09-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 28356226-27ca-385d-988f-f3cf2f2a8c48 | -10.3882 | -50.5477 | 2025-09-10 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e719adf1-fd84-3299-8e36-d74ea2080110 | -11.1247 | -52.0149 | 2025-09-10 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 274.5 |
| db0bb590-fafc-3401-b6bd-b39b56776fda | -11.4648 | -43.6668 | 2025-09-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 9ccdc92f-ce9c-355d-accc-22daf1f1f9ca | -8.0416 | -48.6656 | 2025-09-10 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 179.2 |
| cce7ad3d-5f69-3be3-b0e9-8298f46e1786 | -19.282 | -47.9946 | 2025-09-10 14:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| a6113de6-5fb1-3d04-9d12-1ecc72dfbc2c | -5.655 | -43.9013 | 2025-09-10 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 40dfe290-0359-351f-b41a-32e7cfa52d1b | -6.2409 | -43.3911 | 2025-09-10 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| ecb4e3aa-ae15-3b7a-b79c-18ae0c552e33 | -14.5609 | -52.1836 | 2025-09-10 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 4f8132e0-62c5-364d-9782-1732dc7aabd5 | -9.9951 | -50.3102 | 2025-09-10 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e7a91fd5-7a21-3786-a019-fc9125aa2003 | -9.7589 | -51.1383 | 2025-09-10 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 160.4 |
| abe2b326-8ff8-3089-9cc0-402f5576eb22 | -6.8523 | -47.8925 | 2025-09-10 14:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e78dd441-565a-31df-862b-0ac5fb81a43c | -12.1803 | -53.863 | 2025-09-10 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 4a10fbed-cb41-37f1-af01-d50615679659 | -14.5612 | -52.1623 | 2025-09-10 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a5197875-6202-3a61-bd1d-ee95e7aad2af | -14.7542 | -45.3156 | 2025-09-10 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 78a5d14b-8fb5-3bea-ae42-17f8fc5380c2 | -7.5218 | -48.2536 | 2025-09-10 14:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 220.0 |
| fa608bad-6965-3590-89d3-19e286f3b84a | -11.3905 | -43.5365 | 2025-09-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 262.2 |
| ad636176-268f-31a4-a400-83a86b182b51 | -9.8838 | -50.1719 | 2025-09-10 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 0fa80ad5-1a56-3292-a24d-ac8e74920e23 | -6.1896 | -41.0398 | 2025-09-10 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 159.9 |
| c6465893-c4bc-3f92-bae4-f6a9385ef51e | -3.2157 | -42.5776 | 2025-09-10 14:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 055e59ff-ddbb-373e-a647-0084b4054ff3 | -14.6067 | -40.7531 | 2025-09-10 14:10:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 114.2 |
| c0a6dd9c-d449-3a57-9cab-e9a8c7788b3f | -5.6788 | -43.3425 | 2025-09-10 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 03c413dc-8951-3f37-abbc-fce87faadaa2 | -7.5033 | -48.2334 | 2025-09-10 14:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 9b075a86-3d95-377d-9b39-9e949d1c2821 | -9.0579 | -46.9688 | 2025-09-10 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| a410e919-8ca3-3d5a-b79d-d36fdfebf2f0 | -6.3993 | -44.4419 | 2025-09-10 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ae085216-90e3-3147-8291-5c45567168ca | -12.1993 | -53.8611 | 2025-09-10 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 06d8d5da-4eb7-392a-8909-d8d969e79aa7 | -6.2407 | -43.4144 | 2025-09-10 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 01b13093-f722-34cd-9a35-6ad2a412a406 | -11.4268 | -43.649 | 2025-09-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 269a67d6-d7c3-3765-9a2b-93f7ed706585 | -7.7439 | -50.316 | 2025-09-10 14:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 72917e36-01d2-3a24-9cc1-ce9b01f66138 | -6.4035 | -44.0273 | 2025-09-10 14:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 61832b4b-c62e-3d72-bcb6-35f780cac17b | -8.7361 | -47.0904 | 2025-09-10 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 04593b32-870c-3b5c-999c-1f511fd8a050 | -10.0157 | -51.6821 | 2025-09-10 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| ba1140fe-aa65-345d-9e68-cd623d3b239d | -10.0137 | -50.3297 | 2025-09-10 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 242.3 |
| 7e1bbc8e-34e5-37df-be17-02c7ee5d7ff8 | -15.2877 | -53.7987 | 2025-09-10 14:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 26009453-3a87-3088-af3f-be94d0c77dc8 | -15.1021 | -50.1249 | 2025-09-10 14:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 197.8 |
| ddd5720c-26b5-3d43-8d44-dd40da6ceed7 | -5.9189 | -45.7941 | 2025-09-10 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| f96ddd1b-67d6-3290-a3fe-a673f3564f5d | -14.4054 | -53.4063 | 2025-09-10 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 375390fd-5e04-3871-998e-073b86bec97e | -14.5125 | -53.9367 | 2025-09-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 31a2db9a-bff6-3f07-813f-9a01ca66862a | -12.9474 | -54.8135 | 2025-09-10 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 8846df0e-709e-3e0d-a89d-c8d49c1625cb | -9.0768 | -46.9668 | 2025-09-10 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 6c1ceb1b-fc86-3f14-bb90-0e9f59137ca8 | -9.0132 | -46.0563 | 2025-09-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| a1179354-9434-35a0-b863-3ac93c299513 | -14.9067 | -55.8751 | 2025-09-10 14:10:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 541f6f48-92e7-390a-8be3-aef9ea4da752 | -11.4652 | -43.6432 | 2025-09-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 448.9 |
| 1c6914fe-00cd-3267-bad1-f9acded3a76c | -11.9535 | -51.081 | 2025-09-10 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 169.2 |
| fde739ba-c0c7-3f5d-a716-1f54b2ddeba5 | -5.6738 | -43.9 | 2025-09-10 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 84c9bcba-c0ef-3c97-91ae-384b770b31ab | -15.5269 | -48.376 | 2025-09-10 14:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| afaa9791-896f-3c8e-ad2a-51a8166c1f19 | -11.1689 | -45.2914 | 2025-09-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| c346debc-9e20-359b-a8c8-1ae7dc57f7f9 | -9.7599 | -45.4048 | 2025-09-10 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 1fb976fd-90f3-3bb8-a436-caf3619a823f | -9.8263 | -46.0549 | 2025-09-10 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 856e162c-903d-3908-b4af-529ffe2e9d1b | -11.4097 | -43.5336 | 2025-09-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.4 |
| bd6e9a86-de95-3335-965e-528023ab9a3c | -9.7591 | -51.1172 | 2025-09-10 14:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 210.3 |
| 6b186914-9787-3075-99b9-934e93d7e70e | -20.5283 | -47.6213 | 2025-09-10 14:10:00 | GOES-19 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 95937be2-cb4e-398e-a73f-3ee3344fb155 | -6.2177 | -45.8172 | 2025-09-10 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |


[Clique aqui para ver as próximas entradas](README114.md)
