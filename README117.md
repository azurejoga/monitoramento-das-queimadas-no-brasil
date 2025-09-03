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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88528fcf-424a-39e6-b000-a929fb4b94ab | -11.9034 | -50.6175 | 2025-09-03 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 42b61e03-24bf-3fdf-904a-2e4d235d0cb6 | -8.0794 | -45.3844 | 2025-09-03 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 162.6 |
| ba0107dd-5bbc-36b9-bd47-04b96a0e6f1b | -8.0796 | -45.3617 | 2025-09-03 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 369.4 |
| 4efc1e7b-0923-3ab0-a048-2ab1653be534 | -9.402 | -48.0585 | 2025-09-03 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1c0b80de-3280-37d7-9458-35624bec9430 | -8.8842 | -45.822 | 2025-09-03 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e744b4c5-0e18-3c7a-af06-772798efca6f | -9.6226 | -47.0861 | 2025-09-03 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 93f1f467-3483-379b-95d2-fc10b15247f7 | -12.824 | -48.06 | 2025-09-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 330a9ac0-07d7-394c-b29a-1a8be33d4e59 | -11.3705 | -43.5868 | 2025-09-03 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 62d0c820-877f-3070-a501-19190ea1fc49 | -12.7926 | -47.6638 | 2025-09-03 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8d046345-e4bd-37da-b467-e9617fe5d537 | -7.4969 | -45.3495 | 2025-09-03 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| cf7a4882-3d10-3669-9e20-bea737545934 | -6.8367 | -45.6784 | 2025-09-03 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e95f2dcf-fca5-316e-8679-02a91ae7917e | -7.6646 | -43.8653 | 2025-09-03 13:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f7598117-0b6a-3879-a297-4e4c9b82c945 | -8.3646 | -48.2899 | 2025-09-03 13:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 11362109-6375-35aa-a27e-2c4fa50efe94 | -5.8642 | -45.6408 | 2025-09-03 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 641a45e1-5154-3d34-9b36-f15a0b2e57a5 | -9.6232 | -47.0416 | 2025-09-03 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b947462b-a54e-3fb9-9c74-aa4223dbd500 | -10.7688 | -45.2769 | 2025-09-03 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| be60fbbe-d894-34f7-9cc7-e073e2ce4c15 | -14.4071 | -53.3013 | 2025-09-03 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 59363d6a-0003-3945-97df-5ada3b8d5ca7 | -5.7181 | -45.2453 | 2025-09-03 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 302.6 |
| c8e23ddd-7f96-377c-a49f-5c87c45ed748 | -6.5546 | -43.9221 | 2025-09-03 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c9d4459a-3492-30f0-a7c4-426ca0d0a5cf | -8.8278 | -45.8054 | 2025-09-03 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| db83bee1-474d-3be6-92a4-84d297668928 | -11.8533 | -51.4318 | 2025-09-03 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 943ef446-ace4-392b-959e-b2f2fafc6d6b | -14.4068 | -53.3223 | 2025-09-03 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| e245e7e0-fb35-362e-a276-d1059027e894 | -5.2575 | -44.4581 | 2025-09-03 13:40:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| e23a7d52-cd0a-386a-b62c-bf1434f8099e | -8.5431 | -47.4849 | 2025-09-03 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 326620ef-c2e4-3453-9e5a-3d46ec6b1868 | -9.7429 | -49.3925 | 2025-09-03 13:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 6c9236eb-59fb-36ce-b717-831e139fe43a | -14.0502 | -44.5779 | 2025-09-03 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a665e12f-29c5-3af7-ad54-5d72416828e2 | -11.8518 | -51.5378 | 2025-09-03 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 8ec9a5f7-93de-3a51-a7c0-c5883b38dcde | -11.6647 | -57.3533 | 2025-09-03 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| e8153190-4bbe-3cd1-84b8-c8d971eb380b | -7.4654 | -44.8061 | 2025-09-03 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f0b24ffc-fb52-3954-85c6-103063ffd781 | -8.0203 | -44.0608 | 2025-09-03 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 3cc0c4c8-1c3d-3c49-bfb9-913dfc499c70 | -8.2006 | -49.5559 | 2025-09-03 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| ef92bec3-46d5-32ed-b504-dc01bef6344b | -8.3644 | -48.3116 | 2025-09-03 13:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 87654679-55c0-3568-8427-5fca6ac8866e | -6.1234 | -45.9139 | 2025-09-03 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b42c67c2-494b-34e1-b0c1-0091ed3457b7 | -15.1576 | -52.3586 | 2025-09-03 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2e794b66-2289-3d23-a01e-706797cf1eb3 | -6.7597 | -45.8871 | 2025-09-03 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 37990377-43ab-3aa4-a319-b1d0bfd342e8 | -11.0181 | -51.5001 | 2025-09-03 13:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| a183bb08-4e5f-32b0-9973-f13ced805f28 | -7.484 | -44.8272 | 2025-09-03 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| eed7f45f-3c6b-34e7-ab77-7c8988fe49c2 | -6.3502 | -45.6498 | 2025-09-03 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| e032cc3b-9c91-3c0c-8f30-744e57a7bf1c | -5.8455 | -45.6421 | 2025-09-03 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 03de7971-463a-3e61-b758-ae6834c3a38d | -6.7595 | -45.9095 | 2025-09-03 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2d30fa12-0bbe-36dd-a095-174501b8ce38 | -5.8884 | -42.9753 | 2025-09-03 13:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 490a3675-7306-3878-b19c-b6c3fc6d31c3 | -5.7183 | -45.2226 | 2025-09-03 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9cbf433a-d0d7-3844-b3d3-1bc14be0fcd3 | -15.1771 | -52.356 | 2025-09-03 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 2a86850b-1649-3e60-969e-808ff1db6c61 | -11.9606 | -50.6108 | 2025-09-03 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| e7418039-91d4-3e25-a43b-783fafbdedd5 | -9.6229 | -47.0638 | 2025-09-03 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 6b2ed4b1-e160-347d-b00b-6e0df8ca6858 | -11.3709 | -43.5631 | 2025-09-03 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 50e254c6-e21c-3faf-a6bd-d49fee0e6874 | -5.8882 | -42.9988 | 2025-09-03 13:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 3f13eade-a6bd-36cb-9d37-f5c86b0b7cc2 | -6.6982 | -48.4035 | 2025-09-03 13:40:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 4e12d663-ab5f-3162-afac-bf271c4a94d8 | -11.3897 | -43.5839 | 2025-09-03 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.2 |
| f43022e9-3a85-313b-9def-88b66d73cd0e | -9.7613 | -49.4337 | 2025-09-03 13:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 3873f18c-04c5-3ab9-8ad2-994804a2053d | -5.7343 | -45.5375 | 2025-09-03 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| afcdbfdc-1936-38fe-91d3-0bb6bb2fa6f5 | -9.6226 | -47.0861 | 2025-09-03 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 219.4 |
| e9eb4009-50c2-3b7c-a13e-28a0c2ecfc2f | -11.8537 | -51.4106 | 2025-09-03 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b6cf4187-66e6-3a6e-83a9-82fb49144825 | -14.0703 | -44.5508 | 2025-09-03 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3edbd97e-742d-3e8c-9c9b-c199909fa871 | -8.2006 | -49.5559 | 2025-09-03 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| abca05da-3084-311a-830d-cc37f67ceba3 | -8.02 | -44.084 | 2025-09-03 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 92b7cfa9-a635-36e2-b697-de3514b43f29 | -11.6836 | -57.3518 | 2025-09-03 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| a88b78bb-28e0-3539-af22-3f5b8df83349 | -6.7967 | -44.1091 | 2025-09-03 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| caa16bae-ef6d-3128-a5fa-b6df84cb995a | -5.7152 | -45.5838 | 2025-09-03 13:50:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 758341ab-b16c-39eb-8c52-f4c8d2a5e196 | -5.2575 | -44.4581 | 2025-09-03 13:50:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 83e3bbf8-0c9c-376d-b6a3-c9e1fbf32697 | -12.824 | -48.06 | 2025-09-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 16b0ab0e-f4bd-34e5-9047-3ef8d88120ec | -5.7343 | -45.5375 | 2025-09-03 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 1ef2e586-6320-3e42-a588-f1b8cda6eafd | -11.5969 | -52.113 | 2025-09-03 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 5f29f880-e32a-3483-8341-39d1d3191f25 | -12.793 | -47.6415 | 2025-09-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| c86dd01d-eb6a-3a3a-a0b0-65f7eacb92be | -6.7928 | -44.4776 | 2025-09-03 13:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 97936ffe-30f9-3f52-b777-898f850d105f | -7.484 | -44.8272 | 2025-09-03 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ec75bbf7-520f-35f1-be89-b9ffbe366d61 | -10.9524 | -50.7658 | 2025-09-03 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e9e98728-d4ab-3e55-8f7e-126fcabef3fa | -5.7154 | -45.5613 | 2025-09-03 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 9dceed95-0c89-3b6f-b75c-adaf77238209 | -13.5162 | -47.0393 | 2025-09-03 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 127.8 |
| e0d0c90b-96c8-3304-97c4-46bc4ade67ff | -11.6156 | -52.132 | 2025-09-03 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 29dd82f0-7a0d-32cf-b08f-e3405d48ee3c | -7.4842 | -44.8043 | 2025-09-03 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 390d56f1-1022-3bf2-8c9c-2181ba5996f8 | -9.402 | -48.0585 | 2025-09-03 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 135bf842-a179-3434-b5ca-84eba05109e4 | -15.0258 | -50.0491 | 2025-09-03 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ef86fad8-b600-3537-ac18-0fa32eb59964 | -10.9136 | -50.8336 | 2025-09-03 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 2065fa30-2954-305a-8572-cf94f84a9c40 | -9.1373 | -49.6659 | 2025-09-03 13:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 4e781657-1b6a-3d9d-9e21-dbfbe3d0d3c3 | -7.4966 | -45.3722 | 2025-09-03 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 262.2 |
| 7c590706-0ff3-35a7-9355-3a4c7c473505 | -6.1234 | -45.9139 | 2025-09-03 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c1ccff73-283a-3186-a4f6-bc1e6fe6c41a | -5.7736 | -45.3091 | 2025-09-03 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 174.9 |
| da50910a-c1ab-364c-9826-e03bc0372f56 | -8.0796 | -45.3617 | 2025-09-03 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 310.5 |
| e9ae71fc-3ddd-37b5-8c59-58f77a2bfbd9 | -8.0197 | -44.1072 | 2025-09-03 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 6b0c0433-d3ed-30d6-b0b7-db7c94c5e00f | -14.5655 | -53.0503 | 2025-09-03 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2ee3f3f8-0988-3833-9207-6fec50cb668b | -8.1807 | -44.8043 | 2025-09-03 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 797fa0c6-e970-3719-b0dd-171a1bdeb3f9 | -8.3832 | -48.3099 | 2025-09-03 13:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c6dd86e6-0cf9-35e7-af82-610280403901 | -15.1221 | -48.1527 | 2025-09-03 13:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ac9dc6d9-712b-377b-a1ee-83f481118013 | -8.0794 | -45.3844 | 2025-09-03 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 176.5 |
| aea1f907-c1df-3370-a1cc-e2a7f2985936 | -9.6232 | -47.0416 | 2025-09-03 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 696d5bfa-6ca2-3341-a3b0-08ef84d2de51 | -11.8533 | -51.4318 | 2025-09-03 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 4f7632ad-ac16-3e35-8eba-fe95f8ca5fab | -14.4068 | -53.3223 | 2025-09-03 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 72366d7a-8295-3661-8aed-4a811b9677e2 | -8.8845 | -45.7994 | 2025-09-03 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 05af4f38-6cd5-3ef2-b939-31b220fc3df7 | -10.1454 | -46.265 | 2025-09-03 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 38eee5fd-b653-32a0-b50f-9cf2ae91e0c5 | -7.4969 | -45.3495 | 2025-09-03 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 266.6 |
| 6c127fea-44ef-391f-8153-959088b5d661 | -11.3897 | -43.5839 | 2025-09-03 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| b103d20f-77bc-3c81-9abb-89c23a8003e0 | -12.8432 | -48.0573 | 2025-09-03 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a09af71e-5c85-3b8c-b635-63c42499d491 | -9.6229 | -47.0638 | 2025-09-03 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 193.6 |
| af9cfa6b-303b-32ca-98c5-45774a48dd6d | -5.8455 | -45.6421 | 2025-09-03 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3a749f31-429e-3cd4-a860-fde0aeb38263 | -10.0932 | -54.7667 | 2025-09-03 13:50:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 153.6 |
| 7c683eaa-c6b5-3634-af47-a54505fa9468 | -9.9235 | -45.885 | 2025-09-03 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f5ea1f36-3585-3b76-b381-64c08277bf93 | -5.7738 | -45.2865 | 2025-09-03 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| dff32848-5abb-3718-8f61-5c31e99039d7 | -11.6647 | -57.3533 | 2025-09-03 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 31a3e599-732e-3cd4-b3e2-110bbf68d307 | -8.8839 | -45.8446 | 2025-09-03 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |


[Clique aqui para ver as próximas entradas](README118.md)
