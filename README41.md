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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d734ef6-05ba-3d01-a061-54f841c149e6 | -5.22183 | -52.02022 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cc49a10-1f1f-3839-b5c1-e53419b36968 | -5.98099 | -43.74782 | 2026-08-29 04:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08749d17-c63f-328d-b7b8-1e1d04c04532 | -1.11653 | -54.09109 | 2026-08-29 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91612f77-d947-33a1-9539-e729dd961b43 | -1.11738 | -54.08894 | 2026-08-29 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89872fb8-e5bc-33cd-9ff1-afb2f0a9372f | -5.41279 | -43.18911 | 2026-08-29 04:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ea944bee-9e08-322d-bbbb-f6ba7d822b14 | -2.72707 | -47.04699 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85b13d26-a5c0-346c-877b-fce34b3cc505 | 0.14742 | -60.3979 | 2026-08-29 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a0aeb3d-c680-3d37-b2fc-9e58d86c6c56 | -4.06221 | -56.29503 | 2026-08-29 04:51:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51d2b531-5266-35a3-9355-99d2961c98b0 | -4.47462 | -55.40557 | 2026-08-29 04:51:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e501267-dbe8-3479-a9fb-ff773181b48e | -3.75119 | -53.3537 | 2026-08-29 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73668673-b63d-3e6c-ab1b-f792495dd7cc | -5.41361 | -43.1836 | 2026-08-29 04:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0bdb44f7-b923-3656-8b32-ca29ac64a72c | -2.91484 | -54.1651 | 2026-08-29 04:51:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7d20085-0ba2-3498-886e-513554bfe7f4 | -5.28803 | -50.9413 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 761d43dd-7748-34cc-a6bd-5b4f15f527c4 | -4.28562 | -48.19149 | 2026-08-29 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd487796-4b78-3dff-8980-e994bced2eeb | -6.71354 | -44.42097 | 2026-08-29 04:51:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01a8e994-025c-3ede-b254-ad36ea4dcce6 | -2.50111 | -48.13189 | 2026-08-29 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2ff04248-a7dc-37a3-86d3-41462ab316f6 | 3.1143 | -60.71261 | 2026-08-29 04:51:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d5ed810b-2a0c-349a-a1c7-b4fda2cfa7f8 | -3.93747 | -59.33001 | 2026-08-29 04:51:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3349eb32-b7c4-3196-ab36-bb7b3f75977d | -3.20514 | -61.14364 | 2026-08-29 04:51:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2563a41-36d6-372a-a91e-f18ecd72b2bc | -2.12961 | -50.93302 | 2026-08-29 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b04c79ef-9a68-3f28-a453-2f0fd417105d | -2.74923 | -60.2389 | 2026-08-29 04:51:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30e2fd18-35ea-3a6b-be8b-9b27540cc5cf | -6.01333 | -45.81032 | 2026-08-29 04:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c8f08cf-3afb-3ca9-952c-35962696af9d | -5.22239 | -52.0167 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b912d85-a3a2-3c76-b74d-031568b365c1 | -6.62659 | -43.74119 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f2095de6-05e9-3b74-ba79-f257b0cd0051 | -1.45377 | -55.52368 | 2026-08-29 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f72c857a-0539-393e-82ba-8b94192302b4 | -1.86745 | -47.98034 | 2026-08-29 04:51:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4ee42aa-58e9-35e3-8cec-62ffca798d3b | -3.4286 | -52.77249 | 2026-08-29 04:51:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8eeee6a4-32b3-3cb8-bb05-ba6f037e34d7 | -4.69629 | -55.66837 | 2026-08-29 04:51:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07e1f151-2320-3ed4-a627-79d498a9c135 | 2.41392 | -60.88162 | 2026-08-29 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2396313d-6140-3d22-b47c-ec3464ef4c51 | -4.34363 | -55.44544 | 2026-08-29 04:51:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d2ec2c9-5a19-316b-9a12-4d17b3375aa4 | -6.62179 | -43.74056 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3edae56e-285f-3907-96d9-456747e01717 | -6.34524 | -44.09172 | 2026-08-29 04:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 061ae5e9-ed90-3a34-ae69-a512b60fd487 | -5.28858 | -50.93785 | 2026-08-29 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9b5c880-b61e-337e-999c-6684f6aca08a | -5.34003 | -45.15534 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40a3eb44-ab22-3f66-b864-c9d0d661db31 | -1.20878 | -54.17222 | 2026-08-29 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df4172d3-6018-3756-add3-dfd8b861c7ac | -3.54479 | -54.4896 | 2026-08-29 04:51:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f925472e-4aa0-3d82-9d7e-a1192c2d69f0 | -2.72331 | -48.80155 | 2026-08-29 04:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 527364f1-008a-353b-95a4-648e080bd7ff | -3.936 | -59.32919 | 2026-08-29 04:51:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a18e6366-57db-3982-84da-b766d33ab4c6 | -2.71743 | -47.03686 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32369247-fd78-34ee-b044-a337d547ff21 | -6.61624 | -43.74511 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a42ebe24-c742-378a-b58e-932977d632f9 | -5.47912 | -45.12128 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a053281-c373-33e3-a2cc-4fc6df2fb981 | -4.15056 | -60.69117 | 2026-08-29 04:51:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cebc0f9-9416-3d6b-b4ec-c12d0cfc853e | -2.50229 | -48.13274 | 2026-08-29 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 102dbf67-120f-36be-984f-46e0dbdff0c6 | -6.62217 | -43.73704 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4ab56d41-a685-39dc-abe7-a8ed3fc19797 | -2.71678 | -47.04108 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d057e15-3022-3c92-aabf-3ad21ae461b7 | -5.36736 | -50.56815 | 2026-08-29 04:51:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb867426-811c-3487-8d5c-e2dcccfbcfbd | -6.33662 | -44.08576 | 2026-08-29 04:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5099e63-5abf-38b8-aa74-e24d062c88d4 | -2.93618 | -51.48234 | 2026-08-29 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 082953e2-803a-3afc-97ab-333e047e2955 | -1.03722 | -47.5551 | 2026-08-29 04:51:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa7cc6a9-9356-3037-b39b-47b98db17c37 | -4.29965 | -59.47775 | 2026-08-29 04:51:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f106c5d-6961-304c-89d3-3b515a732a36 | -4.36892 | -47.77121 | 2026-08-29 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6a895a6a-3226-37c9-8432-fe0711c50d9c | -5.41107 | -43.18469 | 2026-08-29 04:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7fccb72a-7cb9-33d2-8725-2e25b3b906e0 | 3.23438 | -60.13536 | 2026-08-29 04:51:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b8ebc6e-a9eb-347e-a876-bd2366f72da3 | 0.14152 | -60.39888 | 2026-08-29 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39812b9f-6b30-3a65-8e0a-c7d61fb39c6a | -2.72276 | -47.05066 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2dc274a-1bdf-3685-b42a-017c175b5f2b | -1.63204 | -55.11953 | 2026-08-29 04:51:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db289aa1-ec25-3141-9ef7-295fb437beb1 | -6.9031 | -43.65065 | 2026-08-29 04:51:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 132c5ff2-b404-3954-84e8-48493cdff5d3 | -4.92592 | -55.76525 | 2026-08-29 04:51:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee40fc44-3e27-3b80-80d0-3f566ff7a449 | -5.14141 | -49.93287 | 2026-08-29 04:51:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03c8f42-6435-302f-83e2-025c570cb2e1 | -5.34012 | -45.16064 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ba2b09a8-4df3-3883-814e-7a919949ba10 | -5.1923 | -49.34456 | 2026-08-29 04:51:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 587da942-fcce-3416-9586-ca5a25643142 | -4.28151 | -48.19486 | 2026-08-29 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ffdad916-01a5-329a-a1b6-d259ca70068d | -3.7285 | -58.99764 | 2026-08-29 04:51:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e712adb7-d810-3c67-a256-63d3c9beb2a1 | -5.94161 | -44.78282 | 2026-08-29 04:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a60340f-49fb-3504-ab8f-107f6cf0d909 | -1.25412 | -55.71035 | 2026-08-29 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd3b81bb-866a-34c7-8689-dfab12a289cc | -2.72408 | -47.04221 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b077c0f2-b00e-32b4-ba8c-b686f1ace107 | -4.32731 | -54.90147 | 2026-08-29 04:51:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3ccdff7-6e75-32bf-b077-f721868cfd05 | -2.02044 | -52.10814 | 2026-08-29 04:51:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5c5e7bea-d591-3277-8cd8-5c0356153429 | -6.63138 | -43.74183 | 2026-08-29 04:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4058b1dd-7725-3b66-a573-12a7a4c6f1da | -2.89637 | -48.27688 | 2026-08-29 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ef8a2e9-08c8-3c65-9b36-90367e08d654 | -5.41766 | -43.18985 | 2026-08-29 04:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 377a025d-d7ab-3c1f-8fc9-33fc7d8f2460 | -2.89697 | -48.2731 | 2026-08-29 04:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4d409d7-a6ae-3770-b771-0b4f8f3333f1 | -6.90233 | -43.65606 | 2026-08-29 04:51:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4931de92-9ab9-3626-905f-6cb87e991bf9 | -5.9415 | -44.78407 | 2026-08-29 04:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53c438fd-fda8-3459-b534-1140cd829d33 | -2.72342 | -47.04644 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b8dcce0-a95d-314b-ac49-6fee8aa37e6e | -4.95881 | -56.27301 | 2026-08-29 04:51:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6fd58d8-ae09-3a3b-9a56-357130019782 | -1.63148 | -55.12299 | 2026-08-29 04:51:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a1be77-c9ed-319e-8433-cb533ac20d2c | 3.11355 | -60.70761 | 2026-08-29 04:51:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2b5350f7-0133-3541-a469-a20694e5affb | -3.20299 | -61.14556 | 2026-08-29 04:51:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7e406ab7-f58f-3967-8399-07ba86dcfd54 | 3.1104 | -60.7066 | 2026-08-29 04:51:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1bff995e-f251-3f8b-b3b4-731445f43502 | -4.62411 | -48.03809 | 2026-08-29 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db634026-392b-3e0a-9794-fb94c28ce8be | -2.71613 | -47.0453 | 2026-08-29 04:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 523d68ac-8896-39ef-8473-e32a1a926013 | -6.34129 | -44.0863 | 2026-08-29 04:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad01f4ae-3640-3ced-b96a-50401b08fb6a | -1.25475 | -55.70644 | 2026-08-29 04:51:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 426f04b4-a51d-3d50-8eb1-c5e5ff925086 | -4.56091 | -44.06045 | 2026-08-29 04:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7dbaddff-42e2-3c0a-a307-084ddd0998de | 3.11112 | -60.71161 | 2026-08-29 04:51:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| db52e833-6281-3107-b474-a06ff1c64c38 | -5.3437 | -45.15998 | 2026-08-29 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a25c2efc-6415-3e3d-86dc-8ad46149fd54 | -6.34451 | -44.09664 | 2026-08-29 04:51:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2570088-e95e-334c-afa2-4711682367e9 | -4.91067 | -43.47233 | 2026-08-29 04:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed39cb5c-4e34-3176-8605-379b459c4e1b | -5.98026 | -43.7459 | 2026-08-29 04:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 865c3508-031b-376a-b0c6-602add8b1d81 | -1.03373 | -47.55457 | 2026-08-29 04:51:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a8b1ba6-578c-352e-b0a2-070a58f77d2a | -6.17512 | -45.92796 | 2026-08-29 04:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77382a49-4484-3f06-8823-aa90f2ce93d0 | -4.36534 | -47.77065 | 2026-08-29 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c96b98ed-8d7e-3971-a18e-3a3d13a0199f | 1.28417 | -50.77546 | 2026-08-29 04:51:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fc54062-969c-364f-a064-93f49ca689eb | -5.41595 | -43.18547 | 2026-08-29 04:51:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0cb8e134-e37b-3983-925b-394c85997193 | -4.27405 | -49.91936 | 2026-08-29 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19fbb1cc-185e-362f-8e2d-e6d3f7c9e3cd | -4.96997 | -49.61958 | 2026-08-29 04:51:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d90fd8df-482a-3a7a-9215-7fd8482b2e4e | -3.97048 | -41.52005 | 2026-08-29 04:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 243bd5c3-0644-3425-befc-8eeae6323738 | -4.56477 | -44.06572 | 2026-08-29 04:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64b5b066-fc8b-3ef7-bf07-37aec24dc426 | -4.56545 | -44.0611 | 2026-08-29 04:51:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README42.md)
