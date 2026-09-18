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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2205a33f-3d5b-3b59-ace5-689d96cae8bb | -12.0676 | -47.4974 | 2026-09-18 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d3196520-eb9f-32fe-8791-bdee5e4367ae | -7.6574 | -46.1013 | 2026-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| e9df7a38-ded5-31e8-86aa-5d876b6b3f9d | -13.6341 | -46.9304 | 2026-09-18 13:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e957d810-d1c4-3a2a-8223-141f16b42269 | -8.246 | -45.617 | 2026-09-18 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8695c33f-b4ad-3f82-9a15-403638eca044 | -8.4503 | -45.8448 | 2026-09-18 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 30975cbf-01f7-3a05-afc3-6119a48e5979 | -9.9505 | -45.336 | 2026-09-18 13:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| a95ba1b3-1f54-3a3a-992f-683caaa1baa3 | -12.5497 | -50.7332 | 2026-09-18 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 3a864f92-343f-32b1-b956-f684c8035a8b | -10.6944 | -50.26 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8b469244-f83a-331b-8571-966a0131cf66 | -7.6765 | -46.0771 | 2026-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d8b568dc-7c24-3f85-b9c3-93d7462a5447 | -19.5539 | -47.6346 | 2026-09-18 13:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 258951c3-0ea5-365a-ab9f-537d26ca3935 | -7.6762 | -46.0995 | 2026-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 85f03677-7d30-32a4-b887-5235b9f69ff7 | -10.6758 | -50.2406 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 97ce0b8d-3045-30b2-8910-b5c817ac7318 | -8.58 | -44.5552 | 2026-09-18 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 19f81be7-80bf-3aa4-96a1-fa66f41f9026 | -7.6577 | -46.0788 | 2026-09-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 29b61362-6220-3363-aa6f-46fea82d0891 | -9.8505 | -48.3834 | 2026-09-18 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ef73fd35-e3c6-3a25-82db-d555918d0a14 | -11.3437 | -44.0141 | 2026-09-18 13:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| d1856951-5af1-33a5-9f41-d7862adfabed | -10.6726 | -50.4758 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 4d947941-6018-33c7-8614-8b263ee1da3e | -11.2783 | -43.388 | 2026-09-18 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| dbd0a4b0-4ce9-3af2-9f02-07d830f1f94a | -12.5345 | -47.0738 | 2026-09-18 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 86fa2a99-713d-3555-84e5-7f9177b83aa3 | -14.1737 | -45.1641 | 2026-09-18 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8fa02e26-dbf8-3408-9655-72e8a609bdc4 | -9.8316 | -48.3854 | 2026-09-18 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 1c109f73-5930-396b-a0e8-c06600623b7d | -11.083 | -48.2875 | 2026-09-18 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f6620c5a-db7d-33bf-ba56-44622746b8d1 | -10.6536 | -50.4778 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 8adb1fbf-1061-3687-8322-6bc0b825fbbd | -7.0352 | -44.6396 | 2026-09-18 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 2fcd7d8e-7231-30d8-8a92-300f70554a0d | -13.4303 | -51.9036 | 2026-09-18 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 463efee7-4080-3caa-84c6-b28d071e9807 | -12.5688 | -50.7308 | 2026-09-18 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 5cdcc12c-aa6d-30e2-93ad-635e979ff5f9 | -8.6817 | -45.4359 | 2026-09-18 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 01534897-2efb-3be8-96bb-c0275b99eeae | -7.1389 | -42.1051 | 2026-09-18 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 8cd3245b-bd9e-3485-be8b-a73398512302 | -11.4861 | -45.7279 | 2026-09-18 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 12357027-41b5-3a32-9505-98418ebe5f8f | -12.0267 | -50.0231 | 2026-09-18 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| a85e5079-dd1c-33d4-ad0c-5ad79fa5b642 | -11.0636 | -48.3118 | 2026-09-18 13:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e29094d3-bd13-3d8e-a93e-a580394d5097 | -12.0672 | -47.5198 | 2026-09-18 13:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 1e3580a0-530f-3de7-9c54-46cb83421f9c | -10.6187 | -50.268 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 1fe5a2bb-d84e-3704-9718-973bf0400dfe | -10.6723 | -50.4972 | 2026-09-18 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 3ff38916-6b55-3d39-ac9c-44a67b9dd0e0 | -12.55 | -50.7117 | 2026-09-18 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 674ca25b-0d5f-3fef-bbe0-d7939bef3f8e | -8.58 | -44.5552 | 2026-09-18 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d1ed34fd-e82a-357d-b690-ad5d64e5b876 | -4.9183 | -47.4295 | 2026-09-18 13:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 90dfc0c9-4f13-313a-978a-d6794ab85f3a | -10.5472 | -44.8466 | 2026-09-18 13:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4ace38dc-8d90-334d-9505-424d85a0db25 | -13.6341 | -46.9304 | 2026-09-18 13:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| caa0633d-93f5-3394-80b1-9594ebff4b1b | -11.0048 | -49.7325 | 2026-09-18 13:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| fefc73f6-103b-3ed9-8b4f-66d877307021 | -10.3116 | -45.3136 | 2026-09-18 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 890771fd-4c56-39f0-bb3d-112b300979b7 | -19.5539 | -47.6346 | 2026-09-18 13:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 2df225e1-c6c3-35a2-b29e-99af64037938 | -11.3621 | -44.0582 | 2026-09-18 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| b3ed2fc5-b1c7-3d0d-aa87-3f940f238e2f | -10.3307 | -45.3112 | 2026-09-18 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 823a4f03-775a-3fd7-854b-73cf0ba2d547 | -12.5688 | -50.7308 | 2026-09-18 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 978a0337-215b-315d-a276-3fcb69ad3718 | -10.6944 | -50.26 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 98ba7677-8d14-3bf5-9187-e4d6770528d4 | -7.6577 | -46.0788 | 2026-09-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| c0e36523-fe1a-3506-b832-c5e985d9cec3 | -10.3303 | -45.3341 | 2026-09-18 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 5e9181a1-dd11-32a0-911e-57b1d07442af | -10.5966 | -46.5474 | 2026-09-18 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| d33bf2e8-43fa-3802-b46e-7342b87e2ced | -11.2971 | -43.4088 | 2026-09-18 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 26912f4a-404f-34a2-8352-7e61110993a0 | -10.5181 | -46.7142 | 2026-09-18 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| dd7f93c6-ade4-30f3-bec8-e7564e6cde5d | -10.6376 | -50.266 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2560d1bc-b820-3ac6-a5d9-63fbac363b17 | -10.5963 | -46.5699 | 2026-09-18 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3852ad3f-3919-35b1-b9d0-c2de7eaf2573 | -11.3617 | -44.0817 | 2026-09-18 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 214.8 |
| 1fcd6fdd-2151-3e3f-928d-95abf46073e9 | -7.1389 | -42.1051 | 2026-09-18 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 97a0ea55-e6fc-379f-8ab4-b35dbb906e2b | -7.1384 | -42.1529 | 2026-09-18 13:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 085fe05e-f2da-3dd5-a39c-d544f7336444 | -4.5587 | -42.9523 | 2026-09-18 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| c52f91e6-f097-3767-a36e-1f9eab6a7587 | -11.8115 | -46.8158 | 2026-09-18 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 3aaaf84c-6f29-3060-ac15-e99eb5e3a9fd | -14.7105 | -50.314 | 2026-09-18 13:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 97b43315-fe2c-3af0-9caa-63a85b836968 | -4.596 | -42.9734 | 2026-09-18 13:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 219.9 |
| 1c6eb9bc-ef68-3aa0-a603-1a9af6f6e686 | -12.55 | -50.7117 | 2026-09-18 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| bccf1e65-5d58-356f-948d-2cae72452fc0 | -13.2485 | -46.9226 | 2026-09-18 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 3604afe1-7394-3819-b76b-5483e2b46c21 | -7.1012 | -42.1088 | 2026-09-18 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| c9722a59-c690-3d4a-8e7c-802e574a0c80 | -7.0451 | -42.0666 | 2026-09-18 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| 25c1512b-52d6-37ec-b930-3e2da16a7bf1 | -9.8505 | -48.3834 | 2026-09-18 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 41c24f82-6725-3dd9-a5e8-8724257c81ef | -10.6187 | -50.268 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| fe13bfe6-558d-37a2-8c0f-6ff9f4f27eab | -12.0458 | -50.0208 | 2026-09-18 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c9567079-9cc8-36e4-a468-82962429ea12 | -11.3809 | -44.0788 | 2026-09-18 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| f1ad14f5-0f6c-3a95-85dd-a5a2c04fc3ec | -12.5879 | -50.7285 | 2026-09-18 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 9926a5a8-c610-3fb7-a3f9-109cf74d2470 | -11.2783 | -43.388 | 2026-09-18 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 341ee07b-9530-39b1-bc0a-231818f7d9a0 | -10.6533 | -50.4991 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 980cb9e2-a59c-35a9-b7b0-9f3dd76ce60d | -7.6574 | -46.1013 | 2026-09-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| d0e690b8-5aeb-304a-90dd-227a23f3dfe7 | -10.6758 | -50.2406 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 4fb42361-0d00-37f9-b146-31a49606544c | -10.6726 | -50.4758 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 91f9fe1e-a68c-3184-b973-c667c8cec897 | -11.064 | -48.2898 | 2026-09-18 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ba5c0e80-f49e-3a22-b696-0217cd1d0049 | -14.1732 | -45.1875 | 2026-09-18 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 3d044c3b-2ca8-3eb3-9898-04f771139a3f | -12.998 | -46.9381 | 2026-09-18 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 4b51bded-6c0f-3805-86c4-eca18f8e0c0f | -10.6536 | -50.4778 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 17f6ea0e-9773-325a-982a-b616a1a91856 | -14.1737 | -45.1641 | 2026-09-18 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 6cfda54d-af68-3544-8e70-7d08c97cd298 | -7.1386 | -42.129 | 2026-09-18 13:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| b9083272-0b0e-3d62-bebc-cfebe36805cb | -10.6189 | -50.2466 | 2026-09-18 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 6dffcf14-2e87-3a86-8a2b-578be6f73eeb | -12.5341 | -47.0964 | 2026-09-18 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d93828f6-9f15-3bfa-affc-d33f1f409de1 | -5.915 | -53.5168 | 2026-09-18 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 657f6705-cf55-3bb9-a762-eb198bab915a | -11.3437 | -44.0141 | 2026-09-18 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 4602479a-b303-3d30-8677-c249f662e4dd | -7.8036 | -44.8422 | 2026-09-18 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| aecb6a75-1bfe-3bde-972a-5e2dcd3e734b | -7.1198 | -42.1309 | 2026-09-18 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 552114e3-b514-3080-811c-a46c3187b5a8 | -11.0636 | -48.3118 | 2026-09-18 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 3c6c28e8-920d-3bbf-85da-0861ccaca855 | -9.9516 | -46.5577 | 2026-09-18 13:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| ac8bc9fc-baf8-3736-9768-5e023f066e14 | -12.1527 | -46.9933 | 2026-09-18 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| d36c5af5-4a8f-3c72-899b-8591f12d461a | -11.2975 | -43.3851 | 2026-09-18 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 410.4 |
| 52768534-2bfa-3b65-9b30-cefd33b53e7c | -9.9505 | -45.336 | 2026-09-18 13:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e4218f75-697a-3173-a699-3ba7424c3dc1 | -11.0643 | -48.2678 | 2026-09-18 13:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 3115d30b-3640-3e2f-8513-c5162268ea39 | -7.6762 | -46.0995 | 2026-09-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e2c73545-7d74-3c33-8c82-9acb463dad6c | -10.5178 | -46.7366 | 2026-09-18 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 260.6 |
| b4342404-6a38-3f4d-a73a-c10a15d28136 | -12.6235 | -50.8953 | 2026-09-18 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| bbb22b89-1f46-3d55-8336-6c96601b0121 | -7.1203 | -42.083 | 2026-09-18 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| be83e51e-6fd7-37ed-83ae-43324cc37ec1 | -11.2979 | -43.3614 | 2026-09-18 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| a701ac8c-e8dd-3733-89c0-5b8cd967f976 | -8.6817 | -45.4359 | 2026-09-18 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b8313265-feb9-3a03-aa29-ff9ae8276ada | -7.0352 | -44.6396 | 2026-09-18 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 00735041-6843-3019-a1bf-9f0b965c1d6f | -15.6752 | -52.7339 | 2026-09-18 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |


[Clique aqui para ver as próximas entradas](README97.md)
