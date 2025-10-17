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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85e1ca33-2b39-35ae-84a1-96793d2b1986 | -11.36554 | -45.27525 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 4807a6d4-e988-3bd5-9faf-f5aa594fdf6e | -13.3892 | -46.93156 | 2025-10-17 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c9496f6f-c8ef-36ca-b022-6ed19046dc8f | -12.95525 | -47.92542 | 2025-10-17 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4deeee1d-8d1e-3880-bed4-bbbdcf4f156e | -11.146 | -45.86446 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 8e9b4041-4ea3-3c7d-9038-a3de1ab865c4 | -10.94345 | -45.42229 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 118387bb-360a-349d-8bbd-c9cebf4587c5 | -10.62614 | -45.24697 | 2025-10-17 12:38:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| c157ba16-86f4-3ec8-ba3a-f45e31a16eec | -10.86303 | -51.28786 | 2025-10-17 12:38:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| cb79f049-773d-3a6f-888f-718f1f59f4dd | -14.31583 | -51.42113 | 2025-10-17 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ada11d2a-744c-358f-abe5-3f82fb794e41 | -9.62973 | -45.92985 | 2025-10-17 12:38:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b51a34c6-67ae-39f9-a35f-a41377d6d7a2 | -9.62442 | -45.93475 | 2025-10-17 12:38:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| edfcf3e3-78d3-34f6-ae8d-9a5dd0a73e15 | -10.14512 | -44.58827 | 2025-10-17 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 315.9 |
| b4a3707a-8443-3141-8452-d2a08eabb106 | -10.53197 | -49.5502 | 2025-10-17 12:38:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3b0ec811-d422-3756-a243-eab2fb836635 | -14.34897 | -51.49743 | 2025-10-17 12:38:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0a14b309-e5f3-3e29-a432-6d700163dc8a | -13.0472 | -47.29392 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 232d793b-d5d4-3d08-9b02-b0832f27c190 | -12.09108 | -47.42417 | 2025-10-17 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 641ed238-3f0e-3416-bf8b-fd7da580d760 | -13.0449 | -47.31367 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0f0e602f-c5f1-3bc5-8740-2ff38fa48d23 | -9.89468 | -47.67211 | 2025-10-17 12:38:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| e9e03b6a-0c48-3186-ba4f-4e835fed9d38 | -9.43059 | -47.90715 | 2025-10-17 12:38:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4fa08309-68dd-30b7-8676-d9e1913f6e9e | -13.48561 | -47.97342 | 2025-10-17 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 0e4d1d3c-d33f-3625-b4e7-4b17e20d7750 | -11.33073 | -54.92581 | 2025-10-17 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a9d88e2d-649f-387d-8fce-58fb41b71360 | -10.63133 | -45.22601 | 2025-10-17 12:38:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 9c51c754-9388-3ac2-8c3f-b96accf04e23 | -11.57836 | -44.04763 | 2025-10-17 12:38:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b2c84f38-6a52-3254-b074-d05d23d86203 | -11.71623 | -54.18692 | 2025-10-17 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 562aeb51-1518-31bd-91ea-25f60cd63e56 | -13.05533 | -47.33494 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 338c88fd-0da0-308d-9f22-b340b13f0e38 | -13.26208 | -47.12706 | 2025-10-17 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 99be42a4-0c8a-34fa-85a1-995f53586d79 | -10.6294 | -45.22025 | 2025-10-17 12:38:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| c28f3165-e43f-37d3-a39f-347f3cc8a5ae | -12.49351 | -45.4832 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 34942deb-8fd3-38db-b57b-1507a5337291 | -10.92621 | -45.41361 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 356cd41e-9771-3440-9cce-9c938f9bd210 | -10.15206 | -44.53052 | 2025-10-17 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 22b40a65-d3fa-35ec-a78c-fd7a30b9c94a | -13.47337 | -47.97255 | 2025-10-17 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 2e305cb8-a872-31a9-93a0-9f7355ef14f8 | -13.93299 | -45.60955 | 2025-10-17 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 7bc5ba3a-06d1-361c-b2f5-be78e335e75d | -13.42924 | -48.59433 | 2025-10-17 12:38:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| eeaa3f95-dada-3edb-a2d0-76f35d4e66f9 | -11.4146 | -44.1873 | 2025-10-17 12:38:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| bb01d75b-1569-3095-ba27-1732f0933900 | -10.10551 | -47.64346 | 2025-10-17 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| bb70cd8d-7048-3c8e-b950-81a534038889 | -10.93754 | -45.44088 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 21878c34-77ea-3db7-9899-a9c09f8c0f86 | -9.36378 | -46.99747 | 2025-10-17 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5aac3e30-b338-3482-a015-1c3478197790 | -10.99017 | -47.88639 | 2025-10-17 12:38:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| b4cd8dbd-4d5b-341c-8fc7-6ea03168369e | -11.48042 | -44.26662 | 2025-10-17 12:38:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 00e9358a-a088-3959-a8a2-83d41f06956a | -12.07865 | -47.42259 | 2025-10-17 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| ea9b5f08-ea3e-3efd-b032-c8a47e3fd111 | -11.40167 | -44.21252 | 2025-10-17 12:38:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 389.6 |
| 3e9be008-6882-3fe3-a21d-671478298b9a | -10.53363 | -49.53787 | 2025-10-17 12:38:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fe4cb801-a7eb-3d7b-89e3-3a15187586ae | -10.75094 | -47.30555 | 2025-10-17 12:38:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| a5a48285-9920-3676-ba54-78cbbeaa0e9e | -9.62707 | -45.91234 | 2025-10-17 12:38:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 1efe94ed-9671-37f8-b7c4-deaaced0ae95 | -11.47172 | -44.19905 | 2025-10-17 12:38:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 2c12c2b3-bca2-3b85-82d8-b031f2a71b61 | -9.86864 | -49.54407 | 2025-10-17 12:38:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9f0db96e-af50-3bba-bf1a-759725c7460f | -10.98617 | -47.91817 | 2025-10-17 12:38:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 1434d987-b081-3433-9c31-a6f0d89a567b | -9.60917 | -49.02126 | 2025-10-17 12:38:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 63ee549f-a859-3a0a-9e2a-c570ce2e9d77 | -12.94758 | -47.93108 | 2025-10-17 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 1d60787c-62cb-3a34-b99b-dffb27d58258 | -12.96233 | -47.13097 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 24e29f06-6148-36dc-b625-7f4bb4216ba5 | -11.36694 | -45.28085 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| f42cb3ea-2e12-3daa-aea1-bfe7cc14c406 | -12.50813 | -45.48498 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| bb75058f-823d-3edf-9f8e-e7894e86d18a | -9.97533 | -47.02338 | 2025-10-17 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| b0d43b9f-bde6-3d2c-ad5a-d8a9e9feb6da | -13.4113 | -48.57056 | 2025-10-17 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 90ac4654-b165-3017-949a-369d74040b61 | -12.28435 | -57.61801 | 2025-10-17 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 461b3787-7e33-3c9f-985d-d1029a8fdbc1 | -12.95282 | -47.94475 | 2025-10-17 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 88ca3b0f-d62f-3eb2-9d81-901592f60ca5 | -11.02088 | -47.33923 | 2025-10-17 12:38:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 468623d3-660c-3869-bd67-3acf768584e9 | -11.01866 | -47.35758 | 2025-10-17 12:38:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| af5e5cdf-927e-38b4-b67e-049fd0539bbe | -9.99011 | -47.00602 | 2025-10-17 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 8054e19d-f89d-3680-bf23-354fafe538ea | -13.37883 | -43.73273 | 2025-10-17 12:38:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 72ae1a3e-2b04-3fe1-92ce-5c9d7a164148 | -11.92642 | -46.85268 | 2025-10-17 12:38:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ec674ab9-cd25-318f-82a4-35ad1f6fbc51 | -11.59449 | -44.04944 | 2025-10-17 12:38:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| a8014cc6-49c6-3508-8892-16700ac6d0ce | -14.1705 | -47.94027 | 2025-10-17 12:38:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 2e6ccd45-91d3-3d31-90b2-9d0109c28ea2 | -11.63131 | -52.85413 | 2025-10-17 12:38:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b59a17b1-1932-3024-951f-6056e07f42ad | -10.94046 | -45.41637 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| bdde48cc-70ce-3941-80ee-644ee2bdd93d | -12.97658 | -47.11714 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 93471df1-5d29-35f9-9505-cfd7d273cae8 | -10.50446 | -43.42194 | 2025-10-17 12:38:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 9d5a8292-f3fd-3920-8569-c09df849524b | -11.3978 | -44.24531 | 2025-10-17 12:38:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 2bac1498-80fb-324d-ba3b-75e2d7d5b287 | -12.96135 | -47.13554 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| aa986d26-62ee-3753-9d50-a6683a03e555 | -11.10165 | -45.88212 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 0820c87b-a2ab-33bf-acb4-783d248461de | -11.3235 | -57.92933 | 2025-10-17 12:38:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4c546550-50e4-3010-a632-9d0638a71b7a | -12.28015 | -47.1657 | 2025-10-17 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 65cf6631-318d-386a-948c-c30e1f2ecb35 | -9.43796 | -51.14431 | 2025-10-17 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 82d98269-33ef-3e35-975d-228bf32f33e0 | -11.26954 | -52.74096 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9748fe29-978c-385c-ab76-d59449ee8b67 | -13.42677 | -47.9491 | 2025-10-17 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7932829a-2fda-36ea-8d72-0a99bc2d5b23 | -9.3661 | -46.97909 | 2025-10-17 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 49882213-c57a-3208-85ff-dba0160a0387 | -9.4393 | -51.13452 | 2025-10-17 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9bdf60aa-2903-3996-8950-b7f7b3e5de60 | -12.82009 | -57.34649 | 2025-10-17 12:38:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 004ab76e-1603-33e7-bb89-2618e3c7069e | -15.2576 | -50.21036 | 2025-10-17 12:38:00 | TERRA_M-T | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6dfcddbf-c8f0-32a7-adee-62b3099cdb08 | -10.85573 | -51.29062 | 2025-10-17 12:38:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| e7f353f5-7d99-3d5b-a0f1-0f28b3d5aee2 | -13.12469 | -46.96917 | 2025-10-17 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 5c1b64af-3f23-338c-aaaf-3d436b4946b2 | -10.2723 | -44.01558 | 2025-10-17 12:38:00 | TERRA_M-T | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 69bdc3f0-6f74-32c5-9ca5-a905de28b063 | -10.46963 | -50.86397 | 2025-10-17 12:38:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3c26f885-bd35-3423-8813-e19afb8d3633 | -11.36992 | -45.25459 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| a2e3e0ba-5e93-354f-bbe3-9739e78c75fd | -13.1966 | -46.41934 | 2025-10-17 12:38:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 69db994e-d69d-3812-a052-45bbcc06aba4 | -10.14661 | -44.56476 | 2025-10-17 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ec7364be-112c-3f7b-9022-8eaf4f0e41e3 | -11.41092 | -44.2203 | 2025-10-17 12:38:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 317.3 |
| c3e017d1-a65f-3c42-b3f7-7fedbdae94aa | -10.28821 | -44.0171 | 2025-10-17 12:38:00 | TERRA_M-T | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 3894dec9-dbaa-3caa-9588-ddf4d9fec491 | -11.5921 | -44.0472 | 2025-10-17 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| b2aa8659-2a0d-323b-995a-529b16d59069 | -12.4866 | -45.4895 | 2025-10-17 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 4b3c3c5c-8ce3-3329-b377-c5e9d9b75a9e | -12.487 | -45.4664 | 2025-10-17 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 1d9b6814-227f-3874-85c9-8a66e2b20122 | -12.9607 | -47.9294 | 2025-10-17 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 8d5b8ecf-ea78-314e-bf7d-053c4a60249c | -13.0488 | -47.3131 | 2025-10-17 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 2d9775b8-dbd0-3130-8268-f7e7375dca49 | -12.284 | -47.1544 | 2025-10-17 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e5d0417d-8bf3-3aad-a30f-a377d2c99143 | -11.1212 | -45.8691 | 2025-10-17 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 6c879bf4-d9a5-39f9-8689-997481e79352 | -9.9828 | -47.0234 | 2025-10-17 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| c5591b87-4bd3-3d46-b002-c6f03737a6f4 | -10.6363 | -45.2257 | 2025-10-17 12:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 7dcecca5-ad8d-3dbb-8818-0bca6dfd57dc | -9.9831 | -47.0011 | 2025-10-17 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 39ea1f41-54c8-3ccb-aac0-7b8252bd8e11 | -13.4416 | -47.9259 | 2025-10-17 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5dd939c4-deff-3e77-979e-a5cb23f26474 | -10.1063 | -47.6525 | 2025-10-17 12:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 75df8ba0-c343-37cf-b08a-2905b9645eca | -13.4794 | -47.9649 | 2025-10-17 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |


[Clique aqui para ver as próximas entradas](README121.md)
