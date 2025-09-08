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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d48ccff-e065-37c0-811b-93227a724188 | -14.3492 | -60.3046 | 2025-09-08 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 145.5 |
| d260c44b-d1af-3eaa-8c28-797af7389e90 | -12.6343 | -56.9725 | 2025-09-08 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 8e48e14f-3937-3d3a-af35-d60e9228c7d5 | -15.1845 | -47.9627 | 2025-09-08 14:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a777a296-fd85-3959-a3b6-b8db69b4e62d | -14.349 | -60.3243 | 2025-09-08 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 2a53c9e7-03c0-32c1-9c26-03356eb2ad81 | -4.9013 | -42.2226 | 2025-09-08 14:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 127.2 |
| 344f714c-67fd-391b-944d-b5ad6b4a0468 | -7.5035 | -48.2116 | 2025-09-08 14:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 4d12cb5e-5d83-30d0-aecd-f4464fa71ccf | -12.967 | -54.7705 | 2025-09-08 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 231.7 |
| fd2f1611-8962-32cb-a5ab-75de965ebb3f | -12.6153 | -56.9742 | 2025-09-08 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 139f2967-5c8e-355b-8339-7fd9b0a7cadb | -11.8827 | -50.7267 | 2025-09-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 88383c9c-ca04-3af4-8389-6b9d93ddaf33 | -6.1024 | -44.144 | 2025-09-08 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 7c26444e-fc8c-3a52-af74-2c066b447d2a | -12.8223 | -52.8806 | 2025-09-08 14:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 0b1f7acc-075d-3277-9165-5618b7c714cb | -10.177 | -46.6881 | 2025-09-08 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| f428e40d-9d3a-3309-814d-b6ac45522406 | -11.3901 | -43.5602 | 2025-09-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| fb7546c8-fbae-3c38-b1a2-c7c58b9127d5 | -16.3345 | -52.9387 | 2025-09-08 14:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fafd4d52-afa9-35ee-9a03-6adfc7ab4276 | -5.8774 | -44.1614 | 2025-09-08 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 0edaf6ed-56d1-39b4-a717-4b90378dea45 | -15.2496 | -53.7616 | 2025-09-08 14:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 88964f19-214a-3896-810b-2fa6bdb2dde4 | -6.1904 | -40.9668 | 2025-09-08 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 127.8 |
| 85f07a0e-40c2-3e61-b269-20f2d3a0c22b | -11.2831 | -46.4591 | 2025-09-08 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b58651a2-bbd2-3db0-9a89-ce17673d4906 | -9.8757 | -46.5665 | 2025-09-08 14:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 8339a355-a2c4-308f-8f93-ac74e9c8b256 | -7.7296 | -44.735 | 2025-09-08 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| f9c56580-c44e-3eb0-af60-888b50dc034a | -9.4621 | -60.5297 | 2025-09-08 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ee196de5-6471-3424-b6ab-feb22c5537f6 | -14.5648 | -53.0925 | 2025-09-08 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 8e19996c-7475-3949-bd6b-e2e4d8ec591c | -5.6603 | -45.4525 | 2025-09-08 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 9ae20608-26bb-3cc4-9c40-9afd967069f0 | -11.2827 | -46.4817 | 2025-09-08 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 0441d2c5-971c-3187-a000-986a1632bc35 | -5.9565 | -45.769 | 2025-09-08 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 519bd879-09d7-3ccc-802c-74be5de0f413 | -15.184 | -47.9852 | 2025-09-08 14:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 0294eacf-cd13-3417-8680-ae6827c1788e | -15.758 | -53.548 | 2025-09-08 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 53800ae2-6b7f-33db-ab3d-6ae420f355c2 | -9.9251 | -49.8898 | 2025-09-08 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 31aa53f6-cc9b-34c9-9e4e-c0eb825114c2 | -8.0592 | -45.4998 | 2025-09-08 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| b97cac01-a9a8-3691-8d2e-0852f00aa791 | -14.714 | -60.2551 | 2025-09-08 14:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c08d56a3-9b88-3c43-9d70-c07a96472882 | -9.4623 | -60.5104 | 2025-09-08 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d6ffcbaa-8cb3-37b6-8385-f6b2c5123800 | -5.8079 | -45.6673 | 2025-09-08 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 53a7d1bb-0fb1-3641-afc6-972b62ebc7e0 | -16.3073 | -58.0852 | 2025-09-08 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| df7db3eb-0f10-3c95-8abe-49a50990070c | -10.0993 | -48.1595 | 2025-09-08 14:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ae7666eb-5ba0-3e6f-8f73-0459bb8ca43b | -16.3265 | -58.1034 | 2025-09-08 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 30b4b049-26ac-39e4-b710-d4cf4c763881 | -5.6106 | -44.7078 | 2025-09-08 14:20:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 576f082c-8e26-322a-8d31-e6935741d598 | -11.4076 | -43.6519 | 2025-09-08 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| ed7a6b30-c689-326e-a0c8-3a63d9370683 | -12.9482 | -54.7519 | 2025-09-08 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 96bdbfcc-1825-3529-bdca-e7b44493a0a1 | -12.884 | -62.1062 | 2025-09-08 14:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c2508d60-34a4-3aeb-83e3-5a0050d99f19 | -9.7403 | -51.1189 | 2025-09-08 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 6d3954d6-df32-3983-aece-5b4915d2cc6d | -6.2092 | -40.965 | 2025-09-08 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 93c0b31c-e1c1-3cf7-9883-cb78dcce052d | -11.864 | -50.7075 | 2025-09-08 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1d4352f8-af7a-3a58-a76b-2638c29129d6 | -9.74 | -51.14 | 2025-09-08 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 6f8d166a-5181-3fcb-8075-24487a715a36 | -12.1988 | -53.9024 | 2025-09-08 14:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e7e41aa4-f6ee-32b3-803b-398a991d1279 | -11.4076 | -43.6519 | 2025-09-08 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 88c35499-2f63-3162-95e2-c82baf1a495a | -12.9482 | -54.7519 | 2025-09-08 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 6e8bd2b0-c57b-37ea-b1e4-97f251517419 | -19.0765 | -49.7432 | 2025-09-08 14:30:00 | GOES-19 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 121.9 |
| ee50304c-2dcd-3cfe-ab3c-df905f999147 | -5.7727 | -45.4221 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 6f66f02c-b052-3fbc-a79f-e896e17a15e9 | -8.3179 | -47.4621 | 2025-09-08 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 77a34439-6328-3df5-8a87-61ab5a0b0c84 | -9.4611 | -46.4566 | 2025-09-08 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 17aa8a73-9bde-36de-86ea-99c3351a43fe | -14.2752 | -44.9592 | 2025-09-08 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| b918c608-3a10-3481-be2f-9abac0b6a09f | -5.8354 | -42.6265 | 2025-09-08 14:30:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 857a271e-8f49-3d62-8fd0-843033555104 | -11.883 | -50.7053 | 2025-09-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 8706dc17-0549-3579-a2b2-2b87b87e2c20 | -12.1988 | -53.9024 | 2025-09-08 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 2441cadc-2e14-385e-8301-e496b4c6d9c1 | -5.6605 | -45.43 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 256d1234-f7ca-3bc9-9628-eea3b069bc2d | -13.8213 | -46.2631 | 2025-09-08 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 7910ff57-b290-36e2-9f23-a025bc0be1fe | -9.7591 | -51.1172 | 2025-09-08 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 1112fd75-17b3-3dd2-816a-e22731fd42ce | -12.9477 | -54.793 | 2025-09-08 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| be16116c-2522-3d6b-a566-bb4335cd43d5 | -6.209 | -40.9894 | 2025-09-08 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 197.1 |
| 7ffe3508-2c7d-3262-b81c-c6c4b275caa3 | -4.9013 | -42.2226 | 2025-09-08 14:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 126.1 |
| 99f22ae7-7e4b-3623-90dd-b3498c22995f | -10.177 | -46.6881 | 2025-09-08 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 46d7e2c0-02ce-3d90-9edd-7882a7ad1509 | -6.5453 | -44.8415 | 2025-09-08 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 579ca745-384e-37b1-a8cc-8cb0ea14eb7c | -6.2087 | -41.0137 | 2025-09-08 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 159.8 |
| 5cf58175-53f1-3b0f-a850-4736b6d8a2ee | -16.3073 | -58.0852 | 2025-09-08 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| ad4aa588-dff6-3e83-8f2c-c5c4269b82fd | -12.8651 | -62.1074 | 2025-09-08 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d9320602-46e4-366e-9818-b3211e8964b7 | -16.9615 | -45.8411 | 2025-09-08 14:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 2aa03920-d363-35e1-8cd3-09af66607e55 | -5.7914 | -45.4208 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 197.4 |
| d2b53f2e-e907-3b8f-9a20-ac46cb822feb | -11.3901 | -43.5602 | 2025-09-08 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 7e80f975-0319-3b25-aeac-afb31d490896 | -5.9563 | -45.7915 | 2025-09-08 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 759db610-c63b-3fdc-a096-f824aecfabcc | -16.307 | -58.1055 | 2025-09-08 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 181645fa-ff09-37e6-96cc-e17f6a2399b5 | -15.044 | -50.1118 | 2025-09-08 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 192.9 |
| 4e600424-5436-3eea-9aec-8b416070befd | -9.9251 | -49.8898 | 2025-09-08 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ad93ef1b-195c-3497-897a-a8c7e1becedf | -5.7912 | -45.4433 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 197.6 |
| d5167407-93fc-3565-8c58-426587972f99 | -5.8081 | -45.6448 | 2025-09-08 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 270465d7-b05d-340a-857d-e8896ce56e6c | -16.549 | -55.1409 | 2025-09-08 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 5eeb77f2-b3bc-3015-aa57-515d56ddffe5 | -6.1848 | -43.3724 | 2025-09-08 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| c9db4081-e78e-3d9a-bba4-ccf198408bf5 | -12.8405 | -52.9413 | 2025-09-08 14:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 332.5 |
| 045a9384-eaaf-3a4f-90ad-0bbd36d5e3e0 | -15.758 | -53.548 | 2025-09-08 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 4fc81252-9151-3188-b11c-46a2e7fe1fa1 | -5.8672 | -45.3024 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| a1644ce9-eb6e-3dac-af39-634bcdd4b285 | -11.8637 | -50.7289 | 2025-09-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5df9340d-f7d4-3839-87d5-ee43cf6859e4 | -8.7021 | -45.3201 | 2025-09-08 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 771e8589-2e7f-30e1-9993-b2cea2c9e318 | -7.6559 | -47.9593 | 2025-09-08 14:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c039fa56-12aa-340c-af07-6d550c452b0c | -16.3541 | -52.9359 | 2025-09-08 14:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ea3ea08c-5966-3922-9dda-cd9fb8f9f95c | -7.6314 | -46.7507 | 2025-09-08 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 9ce7f0b8-f9cc-359c-910c-cf2ac7c4933b | -7.522 | -48.2318 | 2025-09-08 14:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 6b5026a8-9d54-3a11-a74c-2dc509390371 | -8.0594 | -45.4771 | 2025-09-08 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| e3db28a6-e7b7-37c1-a656-96040acdd4df | -5.9565 | -45.769 | 2025-09-08 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 3c7aaff8-c0eb-397b-8c42-de3f581c2233 | -15.7388 | -53.5295 | 2025-09-08 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 23da799d-bf44-32c3-8810-77dc7f572a3d | -12.6153 | -56.9742 | 2025-09-08 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 2a5da4f0-a90d-30ab-80a3-2931ff50541a | -6.4978 | -43.9732 | 2025-09-08 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fc4220c7-961c-3bce-bc22-38f360c6d8b4 | -9.7403 | -51.1189 | 2025-09-08 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7ad2b559-6e8a-363a-89fe-ea223f4bdfb5 | -8.0592 | -45.4998 | 2025-09-08 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 335.4 |
| 0299f8c5-8e47-354b-9874-d841384913ce | -5.938 | -45.7479 | 2025-09-08 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 199.7 |
| d32751a5-5d30-3b9f-bb8a-47cd66712ca7 | -6.1901 | -40.9911 | 2025-09-08 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 126.5 |
| 046beafe-65e9-3aa4-aed2-e4ca1f1b96a4 | -15.2496 | -53.7616 | 2025-09-08 14:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 5f7a3275-67e4-3c06-917d-ce465ef52a8b | -5.6792 | -45.4286 | 2025-09-08 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| bf430efd-c1b8-3433-99fb-7a27f755c954 | -12.884 | -62.1062 | 2025-09-08 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 86f4274e-66bb-37b2-9dcb-3a6f4663c5d6 | -9.7589 | -51.1383 | 2025-09-08 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 234.9 |
| 27b2d45f-8fe6-398a-9c0b-715ca8b498fe | -11.8827 | -50.7267 | 2025-09-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a1b593d5-cc27-3f0b-bedd-38228724b1e5 | -9.4809 | -60.5095 | 2025-09-08 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |


[Clique aqui para ver as próximas entradas](README102.md)
