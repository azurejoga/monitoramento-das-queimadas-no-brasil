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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e7ce07b-efb2-3cea-821a-58e69f8441ef | -11.1064 | -51.9748 | 2025-09-12 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| d9831cc2-1659-329b-bdea-53594733f570 | -8.9749 | -46.1054 | 2025-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 236.4 |
| a3cc0754-c700-3595-8949-4fd8bd117ce4 | -9.9004 | -51.8811 | 2025-09-12 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 43d3dfa5-0dd3-3360-8b2a-e409151736d8 | -10.0754 | -47.1686 | 2025-09-12 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| bdd0180a-7ad9-3e82-8ec6-aa86c5e3f70d | -16.4325 | -49.0698 | 2025-09-12 14:30:00 | GOES-19 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 6ba12d7c-55cd-3df4-bd83-3449a116d667 | -9.3436 | -45.3853 | 2025-09-12 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 9a9bf881-e241-37ca-94dd-478ccd338eb7 | -11.5037 | -43.6373 | 2025-09-12 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a1bc7c7c-3186-3b91-9cb2-49eb5163d6dc | -18.9101 | -46.8474 | 2025-09-12 14:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 779a39b0-bc26-33b1-bc5f-56ebf6d40a9d | -10.3171 | -48.8127 | 2025-09-12 14:30:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ffd64f6e-626e-3bcb-a537-40ba4a76f300 | -6.1911 | -42.7387 | 2025-09-12 14:30:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 2bf076e3-f1d9-3573-a2a1-27c65729d06c | -12.7696 | -44.7737 | 2025-09-12 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 2b5beadf-8fbe-3e53-a043-c3153c137585 | -10.8785 | -45.5597 | 2025-09-12 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 50d869b6-69fd-33c0-b2ca-45c68f0e35d1 | -14.1912 | -46.1782 | 2025-09-12 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 3dca0e46-4f6c-32c3-a219-16861ed6028d | -13.2027 | -51.7618 | 2025-09-12 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e77011bb-24b4-3973-8b0f-66ef40ae03a1 | -7.3954 | -44.3539 | 2025-09-12 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8e38b935-7f26-304c-83d8-033484dee1a6 | -9.5135 | -54.6494 | 2025-09-12 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 5369408a-0f98-3a27-a60e-0c34ba7dac0c | -6.3278 | -42.2294 | 2025-09-12 14:30:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 213.3 |
| b4221385-311a-3f80-93bb-2b5e3f942a21 | -10.4441 | -50.6059 | 2025-09-12 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 8a0678cf-9794-3134-834a-e957ea36b869 | -7.5232 | -44.6862 | 2025-09-12 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 31f07b0d-4d65-3502-8560-85bd0cbd38c0 | -8.9365 | -46.1545 | 2025-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1f3b92a7-5901-3277-9028-095e42843937 | -10.0943 | -47.1664 | 2025-09-12 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 435.0 |
| 20c8b45f-838b-33bf-8d74-47590754bb9b | -8.4705 | -47.2712 | 2025-09-12 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 191da5cc-b87e-30c4-90f5-3a72c0b7d441 | -9.77 | -46.0163 | 2025-09-12 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| dd8ca649-9197-31df-af78-758fde29ccd0 | -11.9907 | -51.1405 | 2025-09-12 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| bba88494-fb65-3727-86c9-26305ff9abfc | -11.6626 | -46.5884 | 2025-09-12 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 22ca4c59-7602-3f2b-a69c-5e2c51e00d84 | -9.7197 | -46.8972 | 2025-09-12 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e9b7b1b3-3212-32bb-9978-0fc9670c4c4d | -12.9294 | -54.7333 | 2025-09-12 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 5b3e7b76-cf2c-3e69-9878-0f19c6786b16 | -16.5287 | -55.1851 | 2025-09-12 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 7abbd369-017a-3412-9496-c51dfc55680a | -11.972 | -51.1214 | 2025-09-12 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 76956aad-5f87-3606-a8d5-db93dc25c238 | -6.1923 | -42.6205 | 2025-09-12 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 2f22077c-cbbf-3699-9695-29b37ae60558 | -9.0793 | -49.7997 | 2025-09-12 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 422f8658-3e1c-3128-845c-f42534b7253f | -10.0943 | -47.1664 | 2025-09-12 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 229.7 |
| cb9c6cfd-f1a6-3de5-9ca9-8216cfe19c69 | -6.1805 | -45.7975 | 2025-09-12 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 514f95af-ea1c-31df-8610-0fa7a61445ab | -8.9749 | -46.1054 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 34d6de8c-454f-38e7-af54-02685102f601 | -9.075 | -47.1002 | 2025-09-12 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 176ed426-962e-3203-95f6-fef832d6156e | -10.4438 | -50.6272 | 2025-09-12 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| bf4e9273-3a4f-3a69-baea-19a3b3804256 | -8.956 | -46.1074 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| a841cb8a-33a6-3827-b2df-718c41f48adc | -11.4477 | -43.5514 | 2025-09-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| c2564bf2-0e9a-30b2-95c1-e70db079eebf | -6.1705 | -41.0658 | 2025-09-12 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| aac70125-19ea-318d-85e3-8321f8491332 | -15.7344 | -53.7826 | 2025-09-12 14:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 6e2dd259-1dcd-32e8-8bf9-17efa45794ed | -8.414 | -47.2766 | 2025-09-12 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1fdf24d3-9a1e-3d9e-b953-620bc2b28263 | -11.4473 | -43.5751 | 2025-09-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 8b5ef455-b09a-3dbb-aabe-815661aa63a8 | -11.6629 | -46.5658 | 2025-09-12 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 8b385515-d36b-35eb-ba0f-865602452130 | -9.6473 | -48.0548 | 2025-09-12 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 446d4a44-2ce6-320d-899d-121337d2c43a | -7.5643 | -44.3838 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 8ab8e86f-2184-36ae-84b4-0c55c8460e63 | -6.1911 | -42.7387 | 2025-09-12 14:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 480c6f09-da4d-390d-a568-65dd765b4601 | -10.3888 | -50.5051 | 2025-09-12 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 41c43c93-1712-3ebd-8e8e-be05fd267b37 | -6.2588 | -43.4828 | 2025-09-12 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e2a12da2-e244-3da0-ab64-762bcdf953c5 | -8.4331 | -47.2527 | 2025-09-12 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 2e54fa75-0633-3745-9940-9c7952671a0b | -9.5322 | -54.648 | 2025-09-12 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 9525cb4f-86ad-3167-8d37-dfdcda61c661 | -10.3361 | -48.8106 | 2025-09-12 14:40:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1b829670-a6f6-3643-bd76-d5d05756bb72 | -8.2085 | -45.5981 | 2025-09-12 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 161.1 |
| a44cb99f-74c4-3716-b67f-eb6f5418e4fb | -9.8061 | -48.8888 | 2025-09-12 14:40:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 19cf8858-7d12-3d87-9d25-ce545b29f027 | -10.679 | -48.6633 | 2025-09-12 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ee56ee52-f19b-3d88-a969-38270c29ec0b | -8.4143 | -47.2545 | 2025-09-12 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 28874a68-297c-3ba4-849a-145da972961b | -12.8651 | -62.1074 | 2025-09-12 14:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 2c8b1eac-3f5f-3cee-a636-80b7ef481ed4 | -10.1405 | -47.9133 | 2025-09-12 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 8e88ca06-6266-32de-9240-30998a442a30 | -12.9482 | -54.7519 | 2025-09-12 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| a8c6a18e-f105-32f2-93c9-5cb316a6f0fc | -7.5455 | -44.3856 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 1b196eb4-0232-3f8e-bf81-2327558faccf | -9.0382 | -47.0375 | 2025-09-12 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a29a9592-2a38-3b80-982f-1cc895b6afb8 | -6.684 | -44.1189 | 2025-09-12 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3307c895-aaf5-3766-9c3d-2d516567e8e9 | -11.429 | -43.5307 | 2025-09-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| b815b892-4273-32b4-babf-505bf4664cbb | -9.0379 | -47.0597 | 2025-09-12 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| d03301d4-d688-33c6-a14e-834393a7853f | -6.2592 | -43.4362 | 2025-09-12 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| fe1d0cef-afdb-39d0-a259-c2e1f6f229bd | -17.3566 | -46.691 | 2025-09-12 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 52f63294-157c-3f01-8597-63e4bfc57f2a | -11.6622 | -46.611 | 2025-09-12 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 20b936dd-14e0-343c-afcb-ee0cd70a99a1 | -14.74 | -59.679 | 2025-09-12 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8427d5fb-3e7a-3a80-ba2b-7cafcc727390 | -7.4508 | -44.4407 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| dec3cf03-8a33-336b-8254-30114aef9477 | -11.4281 | -43.578 | 2025-09-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 9e6605b7-a79f-3ffa-bbeb-270d8b68dd31 | -11.4398 | -48.5733 | 2025-09-12 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 57603668-da33-31c4-b502-066f32420105 | -7.5452 | -44.4086 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 057e6313-7346-3270-8c0a-26cbe3020f67 | -10.7172 | -48.6371 | 2025-09-12 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3102e434-de97-3031-9bc8-a5c6c2ec3888 | -9.751 | -46.0185 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3d60ee5c-36ee-3c42-aa2e-a2e2450322fe | -9.77 | -46.0163 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| d40a530b-2f27-3d7a-ba9f-81e009f9a4ce | -16.9621 | -45.8176 | 2025-09-12 14:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 153.4 |
| e4d4e68f-6544-38ca-a53d-241005c50d90 | -10.0754 | -47.1686 | 2025-09-12 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9d82c5c0-7fd0-3b39-afc8-19b748affb1f | -6.3278 | -42.2294 | 2025-09-12 14:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 7b78cf4d-72af-3bec-9c8d-d6f62d933f03 | -12.9294 | -54.7333 | 2025-09-12 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d99ac1e9-7999-34f1-bf52-70ee79d9e883 | -11.9717 | -51.1427 | 2025-09-12 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c0ad9160-985a-31a9-8c5b-bbdf8301eeda | -9.0127 | -46.1014 | 2025-09-12 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| b4ff9bc1-ca49-31dd-8fe5-1b1ce4285403 | -6.3092 | -42.2072 | 2025-09-12 14:40:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| f7418fd4-c858-3792-ae18-7f3241446a21 | -7.432 | -44.4425 | 2025-09-12 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 7bf6b1fb-8537-3f77-8eed-3583a250c28c | -7.45 | -51.8256 | 2025-09-12 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 18d7296a-58fd-30ff-8fa3-3971b70079c3 | -11.972 | -51.1214 | 2025-09-12 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b11c26e3-1c2c-3c55-a730-6721236b90fe | -9.0936 | -47.1205 | 2025-09-12 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 9ec4bcd5-338c-3a20-b3fc-2ee99e63b2f8 | -12.9292 | -54.7538 | 2025-09-12 14:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 309.1 |
| 7a875075-c468-3972-9782-ea12cf239ac0 | -11.3718 | -43.5157 | 2025-09-12 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| d7f821cc-bc89-399a-a640-941131f67eff | -9.5137 | -54.6292 | 2025-09-12 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 275.1 |
| d5ccafab-c054-3dfc-adbf-8c6456e09dbe | -9.1164 | -49.839 | 2025-09-12 14:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9db720e3-af09-3d4a-b387-83c79ba5509b | -8.0441 | -61.7617 | 2025-09-12 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| b438fc8d-9297-38f9-b3c9-cfcace110487 | -6.1703 | -41.0901 | 2025-09-12 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1248.3 |
| 08532a0b-2631-3d67-a817-b56160d40749 | -9.0376 | -47.0819 | 2025-09-12 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| ccc31bf7-c649-3c94-9c65-d18b7c2788d7 | -11.5425 | -50.5947 | 2025-09-12 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 267bba81-4b09-38bf-83eb-4a6f1f1f61da | -10.3171 | -48.8127 | 2025-09-12 14:40:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| bdb511cc-79ae-3ec0-80f5-e85f6fa63059 | -8.0817 | -50.1836 | 2025-09-12 14:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1a22712d-4aa9-3b86-9fe9-0ae791d9b88c | -16.5287 | -55.1851 | 2025-09-12 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 159.0 |
| f677abaf-8c60-33e4-8087-6b7336c8dbdb | -8.8899 | -49.945 | 2025-09-12 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4bcbe2e5-5eac-38ca-b7f5-6cecd235ec8b | -16.5483 | -55.1826 | 2025-09-12 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 125.8 |
| c0ac3710-0daa-3ae7-9f14-4b19095cb7ce | -6.3808 | -44.4205 | 2025-09-12 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5237872c-d0ce-3ec5-baee-dedf2b19e51d | -8.3539 | -47.5908 | 2025-09-12 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |


[Clique aqui para ver as próximas entradas](README139.md)
