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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89e51696-5e78-343d-bb06-65966cac1498 | -14.4394 | -47.3206 | 2025-09-13 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1804b091-2dd1-3494-80de-0267f64fc829 | -11.7579 | -46.5979 | 2025-09-13 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 361.3 |
| b7d0a399-0969-3189-9f6e-3ef3c23e0410 | -7.2799 | -44.5945 | 2025-09-13 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f1cc56be-d99d-3cd3-b634-31a2e6084752 | -12.9595 | -47.9963 | 2025-09-13 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 42361bdd-bc40-3b26-b1c1-e4e6a6344dbf | -9.9946 | -50.3529 | 2025-09-13 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 46223405-61fc-3f16-b7c5-c43bfa338246 | -10.8976 | -45.5572 | 2025-09-13 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.5 |
| a9c82270-d615-359e-8f74-82e864fd5c37 | -11.2692 | -51.1354 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 19076954-528b-3ba6-aaf6-6bf00f164b01 | -10.5295 | -49.8704 | 2025-09-13 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6266057b-ce1a-3f59-84fa-1ddec0036f75 | -22.197 | -49.5962 | 2025-09-13 14:30:00 | GOES-19 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.1 |
| f68e1983-f5ac-3ad9-b4c6-8452cec380c6 | -8.9176 | -46.1565 | 2025-09-13 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 80addf37-5824-3d6e-8a96-5823361bbc3c | -12.8837 | -62.1449 | 2025-09-13 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| ffabccc8-7837-3f71-8bc5-5bea3481b7d3 | -12.998 | -47.9908 | 2025-09-13 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 4052b5d7-dad7-3a9c-8419-b71ab35dff31 | -9.8646 | -50.1951 | 2025-09-13 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 271ef19d-b8e5-34d8-92bd-0f14e7db009a | -9.2656 | -59.4191 | 2025-09-13 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| f021fea9-d2ec-3c78-9e7a-af7d45d50e9c | -9.1145 | -46.9629 | 2025-09-13 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 80eef1cf-1324-3683-9489-962ea366fd32 | -14.2905 | -46.0693 | 2025-09-13 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 92c3bfc9-d5c6-3387-b19d-e70f74291957 | -12.9103 | -54.7352 | 2025-09-13 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 65432ecb-c5eb-32c5-a6c4-f398f60b85c7 | -11.3117 | -50.8122 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 446ef3cc-d4a5-3285-b015-398ca4273f0b | -9.9757 | -50.3548 | 2025-09-13 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 817fff23-5808-3af4-b349-68fa1ffebb2b | -16.4903 | -55.1484 | 2025-09-13 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 48c9d086-f0da-32df-823c-f84c2ae163c5 | -11.8698 | -46.7627 | 2025-09-13 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 117f42ba-741c-386b-abda-1afae3d723ec | -13.8974 | -48.3027 | 2025-09-13 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 883e6d07-8f84-3eb2-be31-8b6fdcd953c2 | -12.8649 | -62.1268 | 2025-09-13 14:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| cdaf5fb1-db15-3744-8e5d-b7eb07b3864a | -13.9168 | -48.2998 | 2025-09-13 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 2ee6c191-8022-3e60-8257-64a2121a4692 | -16.5679 | -55.1801 | 2025-09-13 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 167.2 |
| 71e99ef3-dc23-350b-93ff-8cf67ca01458 | -12.8456 | -47.9236 | 2025-09-13 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 19cf691c-b3b2-37a9-85db-20ad464f8b0f | -9.2844 | -59.3986 | 2025-09-13 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 52f7f73d-b88a-32e7-818f-88e93f7c61b0 | -15.1435 | -48.0594 | 2025-09-13 14:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 2ba23662-7ae8-3847-8bf6-240607678e5e | -11.751 | -50.6351 | 2025-09-13 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| ce336bc6-d03f-34e5-bfa2-f5645604a97c | -18.046 | -45.4418 | 2025-09-13 14:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 7027862e-bf9f-34f1-856f-8cc9fef30afa | -10.3397 | -49.9333 | 2025-09-13 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 00f9a806-8e20-31ec-bb76-5d4f023ff6dc | -10.8785 | -45.5597 | 2025-09-13 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 24896a5b-39d0-3793-8f27-3451f3336c54 | -7.5269 | -44.3644 | 2025-09-13 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| a4a9605d-360e-3b58-8dfc-3aacd26aad9e | -11.8468 | -50.5813 | 2025-09-13 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| d965cf64-46f1-3698-9394-2002464ba330 | -13.9366 | -48.2745 | 2025-09-13 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| a0675a6a-f207-3db3-808a-a19b7f752df0 | -16.08 | -49.9709 | 2025-09-13 14:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f7b080df-1a01-39e3-bbcf-f19eac092443 | -18.0661 | -45.4373 | 2025-09-13 14:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e1b5325e-6f61-3101-b08b-5525eb26aabe | -12.9292 | -54.7538 | 2025-09-13 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 284.0 |
| b78fe5c2-4471-3395-a4e1-7b5d6db45418 | -16.3422 | -51.5217 | 2025-09-13 14:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 135.4 |
| b702aef2-b433-350c-b81c-5e5f1749b3e1 | -16.0257 | -47.9294 | 2025-09-13 14:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 95.2 |
| ead89379-f097-393f-8002-8035892b7dd8 | -18.0071 | -46.9266 | 2025-09-13 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1292b425-e6f8-3a1f-a07f-c79c4b493b88 | -9.5006 | -55.9588 | 2025-09-13 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 335.8 |
| 9f893567-b403-320d-80d5-8da4536a765a | -14.29 | -46.0924 | 2025-09-13 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1ccd83ed-0454-31b6-991f-81863da7b13d | -11.77 | -50.6329 | 2025-09-13 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a8105a5b-1b48-3c8a-8cb7-6712d2596d3c | -12.0852 | -47.5842 | 2025-09-13 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| cc4be340-8278-3a16-92f3-c5274b3a8098 | -8.9749 | -46.1054 | 2025-09-13 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 215.0 |
| ea22914a-4e4b-3254-a5b9-ec87575a8086 | -15.8845 | -47.2286 | 2025-09-13 14:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 38cb1d27-02b6-3ad8-8ec2-31ce56af125e | -9.9762 | -50.3121 | 2025-09-13 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b0f5dda7-bb68-3b71-897b-5bb3f68990c8 | -11.7391 | -46.5779 | 2025-09-13 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 580a87a4-2d30-3895-85d4-91507864419f | -8.9368 | -46.132 | 2025-09-13 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| c51495bf-9a2b-34a7-b84c-c6517bda3d24 | -9.9948 | -50.3316 | 2025-09-13 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| cd967223-413d-3f35-88f0-e60f314f1114 | -5.1746 | -40.9545 | 2025-09-13 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 0326e577-c902-3f05-abc7-e82eb1fe8b43 | -11.331 | -50.7888 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 0c60e261-344a-330a-85bf-1e699577c20a | -12.0307 | -51.0083 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| a6899e5f-c904-38b4-90df-d2641742329d | -10.107 | -50.4057 | 2025-09-13 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7602a42b-7bc4-3112-ab84-bd0a2de3f279 | -11.7388 | -46.6005 | 2025-09-13 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 191.4 |
| b49e857f-df7e-3a42-8ce3-9ea38f9bc402 | -11.1423 | -50.7242 | 2025-09-13 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 49acd1e4-eac6-32ed-b967-d92a5859a0ac | -6.2123 | -42.5006 | 2025-09-13 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 63aaffff-65b6-3911-81c6-a7b07034ec0c | -8.9371 | -46.1094 | 2025-09-13 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| faf89b97-9205-3b67-9e84-e9e7f876e6f1 | -14.4588 | -47.3174 | 2025-09-13 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 64906dc4-272c-3d43-bb07-52c5e5097d51 | -13.9172 | -48.2775 | 2025-09-13 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 94654620-ddd9-37cf-8c48-32d7fbeb1855 | -11.4849 | -43.6166 | 2025-09-13 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| dddc93db-3d65-3057-8504-c136e045a11f | -15.601 | -54.7822 | 2025-09-13 14:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 22f13b84-1d55-3ac7-91f3-584b8c876f3c | -14.4939 | -53.8973 | 2025-09-13 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 967129d8-9372-3a76-b493-81be75ffaaf7 | -14.1703 | -46.2505 | 2025-09-13 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 880b7eb1-4a35-312a-9429-8b5955e4b555 | -8.956 | -46.1074 | 2025-09-13 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 261.0 |
| 6eeffb30-81ca-38f9-bf4f-ee8c8ed12210 | -12.1044 | -47.5816 | 2025-09-13 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| d462f6da-20c2-3244-a4c3-115685708b65 | -16.4906 | -55.1276 | 2025-09-13 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 165dd3c0-5e85-3516-bd24-e5be1e531214 | -9.8709 | -63.4118 | 2025-09-13 14:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 329671d4-ff1c-3080-9d8d-3724a37d365c | -16.5099 | -55.1459 | 2025-09-13 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| b0c236c7-c199-355c-a7d5-8f4314eb7a04 | -12.0117 | -51.0104 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 3ae9808b-221b-3362-b279-837148b70d9e | -13.9185 | -48.2105 | 2025-09-13 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 9eb102c0-75bc-3f12-a5fe-64869ab14121 | -12.9294 | -54.7333 | 2025-09-13 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 404.5 |
| fd068a11-9f4c-3ac9-a799-44334283b4b6 | -18.0466 | -45.418 | 2025-09-13 14:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 281.2 |
| fe99241c-d196-3861-b2eb-977d844dcbb3 | -9.976 | -50.3334 | 2025-09-13 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f4c9c87c-9e6e-33ee-b0ec-329098733b7c | -11.1152 | -51.3211 | 2025-09-13 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| b10b718d-7290-3a45-a4d4-9c429bf67dd7 | -14.4584 | -47.34 | 2025-09-13 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 2116823d-fe93-3ba8-96f1-8ec6b9ad645f | -11.1237 | -50.7049 | 2025-09-13 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 48fac77d-7466-3e53-ac0e-c93a07ce30cc | -9.4817 | -55.9801 | 2025-09-13 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 8fc26705-4026-303c-801f-1f4b9cf83145 | -12.0311 | -50.9869 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 7bfb6a76-e988-3a16-bd05-b97e79320657 | -16.0796 | -49.993 | 2025-09-13 14:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 207f6fa3-f75a-3607-a117-3d5e06801716 | -12.9398 | -48.0213 | 2025-09-13 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| bc18b0a6-7a58-3d0a-b676-3a576a73451b | -11.8281 | -50.562 | 2025-09-13 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3e79a686-bcf4-35aa-b072-1eeb597580cb | -11.312 | -50.7909 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9df928a3-36e5-36c9-9fc3-bde9e78e81a6 | -7.261 | -44.5962 | 2025-09-13 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| e34767fd-04ae-37ca-b5e2-92d6bf633c34 | -14.3095 | -46.089 | 2025-09-13 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 162.8 |
| bc51f8de-3295-3095-b840-a61c9ad73d15 | -15.2065 | -52.8825 | 2025-09-13 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 7350dffa-ac0b-38c3-aa83-a8f67b7beb44 | -9.2658 | -59.3997 | 2025-09-13 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 250.7 |
| 33a40e23-a66d-3858-8162-e04122154861 | -12.012 | -50.9891 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 5b07ba5f-95cf-31c3-bde4-9e8a047f6a2d | -12.9787 | -47.9935 | 2025-09-13 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| bc9b36b6-4715-3645-92d5-826956dfc5aa | -16.5682 | -55.1592 | 2025-09-13 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 190.1 |
| a7acaeaa-6e9a-3fc0-befc-233d731bd8ad | -9.5004 | -55.9788 | 2025-09-13 14:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 285.6 |
| d6c86128-e9d4-3859-a2e2-3e3e4a441492 | -11.1896 | -51.419 | 2025-09-13 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| d604465a-f8ea-37ba-825b-0ff185a472ae | -15.1363 | -52.4679 | 2025-09-13 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7fddc781-151e-3edd-9567-7ec8cbc7c64f | -8.9365 | -46.1545 | 2025-09-13 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c8d53bc3-0bc0-38f3-8713-1ff29443b726 | -15.8845 | -47.2286 | 2025-09-13 14:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 39da0f04-438d-3644-bdc0-03d1626574c9 | -10.4252 | -50.6078 | 2025-09-13 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3e0b5278-1629-35f9-817d-293916d38d1b | -11.1066 | -51.9538 | 2025-09-13 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 582bcf05-fdf8-372b-842d-2a4ceaf47962 | -15.1435 | -48.0594 | 2025-09-13 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 3f17650a-652d-3754-a53c-a8f856a62a3b | -14.2905 | -46.0693 | 2025-09-13 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 215.7 |


[Clique aqui para ver as próximas entradas](README135.md)
