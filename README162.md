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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eca4b85b-2b59-3026-ade4-a0097306953c | -3.17923 | -41.41021 | 2026-10-05 18:19:00 | AQUA_M-T | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 01329778-9a8c-3659-9c85-aa771319e097 | -6.49541 | -43.21763 | 2026-10-05 18:19:00 | AQUA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 63bc3e54-406c-382e-9346-e41a97154b6b | -11.6955 | -43.67484 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 309.9 |
| e4bc5342-c8f3-3cce-9fa2-0f76d798cc99 | -2.99961 | -40.57152 | 2026-10-05 18:19:00 | AQUA_M-T | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 18dadb2e-6618-3d4a-bcbb-d78942d7ba1b | -6.60691 | -37.888 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 05ee5fb3-9e1a-3315-9148-19dc6a7c9e9d | -6.93111 | -43.69347 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 305ce2ee-e0de-37ea-b0d4-53c8516c1882 | -5.98082 | -44.85023 | 2026-10-05 18:19:00 | AQUA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 5072c6e5-be6d-3577-a6e9-2e2fe9d9caa5 | -3.92908 | -43.94572 | 2026-10-05 18:19:00 | AQUA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 9235580c-fa2d-3b5c-aa16-8b45de7d4df9 | -5.94922 | -41.34949 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| a3021363-0394-3594-a2d3-20352204ca1a | -5.96392 | -41.37692 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 8a3f0914-9b3b-3d12-bc56-ba14f7c57672 | -5.9706 | -41.35246 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| db329574-b990-3b57-a4a9-b3da7ed52767 | -10.06357 | -43.108 | 2026-10-05 18:19:00 | AQUA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 253315f2-25b8-3350-8859-0494d4d201c6 | -7.15913 | -38.43783 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 52.4 |
| ba214d27-061e-3ebc-af43-2fca3bd86e66 | -11.78437 | -43.55201 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 201d185e-1b04-3741-98a8-5fa1c498dfff | -4.91957 | -41.74114 | 2026-10-05 18:19:00 | AQUA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 475b043f-4507-3d88-be53-172608897434 | -7.10322 | -38.23932 | 2026-10-05 18:19:00 | AQUA_M-T | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 5dce216d-6b55-3ba8-90d9-437b14044970 | -5.99154 | -40.91297 | 2026-10-05 18:19:00 | AQUA_M-T | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 14f5dad2-3384-3f71-bfd2-c64507ebdcfb | -4.01182 | -44.18977 | 2026-10-05 18:19:00 | AQUA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0995249a-1d2c-3e87-a6a9-ac1cdb0014fe | -6.92178 | -43.67004 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 9e1aadf0-a7e6-3581-8186-32774ce2af75 | -6.47579 | -43.89302 | 2026-10-05 18:19:00 | AQUA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9b37d05f-0d71-3bef-a64a-239ea9b5b670 | -3.16814 | -41.40114 | 2026-10-05 18:19:00 | AQUA_M-T | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| cf49a4ec-5940-3e27-a5ce-29153a952fde | -3.36724 | -43.38971 | 2026-10-05 18:19:00 | AQUA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 214e42ef-91b1-31cb-bccd-e77f9d7cb666 | -5.49453 | -44.65217 | 2026-10-05 18:19:00 | AQUA_M-T | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 20a64687-234b-35ce-9bda-b18eba948a1d | -5.12369 | -42.64655 | 2026-10-05 18:19:00 | AQUA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| db75de3d-09c0-3767-95e5-3b28f8602377 | -7.55017 | -46.73322 | 2026-10-05 18:19:00 | AQUA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 8bc97190-b296-37a8-ae51-99061f89a26b | -10.51421 | -46.05987 | 2026-10-05 18:19:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c04325b3-5a1a-388f-bfc5-e0361eaec141 | -11.2567 | -43.51079 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| a1399118-5e5d-3e3f-835d-7267ec15a959 | -6.42421 | -43.47474 | 2026-10-05 18:19:00 | AQUA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 7dd58330-cc42-3e57-9ceb-15f71378bc59 | -5.46786 | -43.77645 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 185d3a8b-e908-399a-a49e-0636d390ca1d | -3.11549 | -40.1605 | 2026-10-05 18:19:00 | AQUA_M-T | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| aa9a82a1-f7e6-3a6c-9efb-b71aa717475d | -8.78093 | -47.56795 | 2026-10-05 18:19:00 | AQUA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e57ef4f0-b4c3-3195-ad52-6d417932c1c1 | -6.48175 | -43.90559 | 2026-10-05 18:19:00 | AQUA_M-T | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 8cd4f08a-7d19-37b2-8066-369ab4bf7dee | -4.34015 | -43.83025 | 2026-10-05 18:19:00 | AQUA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 131f3a05-1c04-39a2-abc1-9b53e368eb69 | -6.61806 | -43.28635 | 2026-10-05 18:19:00 | AQUA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 44.5 |
| a63765da-1f20-3521-a370-783ab413c96a | -5.99618 | -43.70052 | 2026-10-05 18:19:00 | AQUA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 63b18d29-4d9a-3472-b8e3-5655df2c7b51 | -7.22376 | -37.0609 | 2026-10-05 18:19:00 | AQUA_M-T | CACIMBAS | PARAÍBA | Brasil | 2503555 | 25 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 139ebf2f-6f04-3959-b8df-7f180b916caf | -6.22076 | -41.60146 | 2026-10-05 18:19:00 | AQUA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 684523a9-0327-3afe-b333-145318758fb4 | -6.04506 | -43.3859 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 4af6bb2d-8b59-3661-9779-845cbcb2b094 | -8.31534 | -37.00304 | 2026-10-05 18:19:00 | AQUA_M-T | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| da82d41a-04ee-391b-a03f-36c8e231f83e | -8.70767 | -35.73884 | 2026-10-05 18:19:00 | AQUA_M-T | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| fd1d9156-b03e-3cd6-bbeb-e909dc7bd202 | -6.62439 | -37.88538 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 21638ed9-4e41-3349-ab43-60faa34f5afa | -7.12916 | -39.18314 | 2026-10-05 18:19:00 | AQUA_M-T | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 61.2 |
| c3a37b15-2acf-3b8c-afd7-30e7c6fcf000 | -11.23169 | -47.14072 | 2026-10-05 18:19:00 | AQUA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 160.4 |
| a85e7976-97f8-3cd1-b8de-b7ca0820f3fa | -3.79677 | -41.76655 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 45ac5931-3dc3-38e7-8f0f-5179d5ff9915 | -3.69377 | -42.19622 | 2026-10-05 18:19:00 | AQUA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 06a5e218-7019-3f49-b3ad-e0ab3c1e60be | -6.6957 | -45.26855 | 2026-10-05 18:19:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 449.8 |
| 98a7202b-00a0-30cc-88bd-e5c032204388 | -8.3385 | -37.27961 | 2026-10-05 18:19:00 | AQUA_M-T | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 41ebb248-f324-3e16-a4ab-e27d54639971 | -5.95081 | -41.35545 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 4d5b4d24-528d-3848-afa4-30409340a939 | -3.53901 | -39.89998 | 2026-10-05 18:19:00 | AQUA_M-T | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| cf2b0cf1-d446-33f7-af56-62cc774c1740 | -5.98213 | -41.36254 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| c5ce51f4-577b-3cd0-91ee-12c7bdcd5ded | -5.7862 | -43.2471 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| b1598732-aea1-3814-b8ad-10f7716bc27b | -5.53151 | -41.01653 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| 8d946be6-2b13-3466-a82d-409af87676eb | -6.77372 | -39.0276 | 2026-10-05 18:19:00 | AQUA_M-T | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9913cacb-ca64-3075-9a1a-0ebc37e87378 | -6.61565 | -37.88668 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 57.1 |
| fee7dbd1-713e-3edd-b4eb-882a9c62bef6 | -8.01538 | -42.9303 | 2026-10-05 18:19:00 | AQUA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| c7fc6fda-2205-3515-bc68-2a0bfbf46b78 | -6.42202 | -43.45838 | 2026-10-05 18:19:00 | AQUA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| a3914a2e-1ded-3c1a-805f-43a196dfdaa9 | -5.97884 | -44.84383 | 2026-10-05 18:19:00 | AQUA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cef6584c-e260-3eb4-8704-f8fd14ab342a | -5.96231 | -41.3654 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 270.6 |
| 71ab88f2-5a05-3d7f-9922-835163093811 | -9.1076 | -67.703 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| fdc779d3-c8fc-3b71-9932-06c183f19918 | -9.3381 | -65.7255 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ef77889b-4097-3ba9-9d67-3893c818b586 | -9.1222 | -64.3843 | 2026-10-05 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.7 |
| f8398012-1727-3f74-a791-dfc15ef58f3e | -9.0585 | -66.0887 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3f48edaa-4e73-340e-bb5f-7d7c9dde91ce | -8.8519 | -66.8012 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 77790b9c-5dec-3f20-8185-e39f65e6e0ed | -9.1257 | -67.8322 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 2bca3fdd-05f9-33ea-9c73-aed31ec88bb5 | -8.537 | -66.9764 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| fd7f5052-9f0f-3226-9da6-dd11500ef48b | -8.5183 | -67.0139 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 728c16dd-6396-332b-8490-4b400e156fde | -12.8181 | -43.3047 | 2026-10-05 18:20:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 967aa7e8-e49b-3716-83f6-30a5fd0961be | -10.7181 | -69.4057 | 2026-10-05 18:20:00 | GOES-19 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 47.7 |
| e8f16e67-6fe6-3d0a-96aa-3b5d0c3965ce | -8.5554 | -66.9945 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 5dd1362d-f8d9-3a93-a7f6-0f8fcc1c8e5f | -9.0584 | -66.1073 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c243e96b-2101-304d-9b18-e924297aa319 | -8.3526 | -62.8302 | 2026-10-05 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 100.1 |
| af918e70-54a3-3612-b3fc-27c0108776c3 | -8.7521 | -68.985 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5e609a4c-2d9a-3454-a80f-eb6976afe965 | -9.2366 | -67.885 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 78c6f677-d7ec-30b9-8903-e2bd65a69402 | -9.0429 | -65.4361 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 66935594-fbad-32f0-9cbe-bb711d3db820 | -9.2251 | -66.1209 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 76001228-1184-3b1f-97b5-08dd7bc8413a | -8.5554 | -66.9759 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 83346cd0-bed7-30b1-b29c-adc8b7467486 | -9.1241 | -68.2946 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| f0890998-78b7-3380-abd4-35c47941da5f | -8.882 | -68.8166 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a675fe43-f24a-3499-a8ce-1a236e980797 | -6.6217 | -37.8923 | 2026-10-05 18:20:00 | GOES-19 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 87.8 |
| e14ea873-1a0a-34eb-a717-0dd8d2ec316e | -8.9239 | -67.3372 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b2522dcd-088c-3ebc-bf00-5211d53d388a | -9.1257 | -67.8137 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| ef23a981-fac7-33f5-9068-bc58974f2817 | -9.0982 | -65.4904 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 1900f66b-779d-37c9-884a-1cfc794665d8 | -9.4783 | -67.6752 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 20d8097f-b03b-393f-b874-41f2d7e6f4d5 | -2.5353 | -65.8819 | 2026-10-05 18:20:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 2cdc17bc-b54a-35af-892d-347eb42d5083 | -9.2828 | -65.6526 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 9a178c8b-7ee6-34a2-9b62-b3b2042c7a1c | -9.9175 | -65.0313 | 2026-10-05 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| ce7f34a7-f126-3056-a1a1-df30f026ef02 | -2.5353 | -65.8635 | 2026-10-05 18:20:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 3911d202-df7a-37fb-98cf-5860a044f2f6 | -9.1243 | -68.2391 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 61d24883-14be-3228-808a-017879c239d5 | -5.9417 | -41.3524 | 2026-10-05 18:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 176.8 |
| 51468bab-7118-35d3-8112-219a80865f7a | -9.4751 | -64.3336 | 2026-10-05 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 72757993-8270-360a-a583-adf6d6a406b9 | -8.8704 | -66.8007 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 51767ac9-25ee-3975-a033-a242976a1853 | -9.1072 | -67.8141 | 2026-10-05 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 225.7 |
| 370817a7-2a4a-3936-8a5a-f6fdd50d20fc | -9.4565 | -64.3344 | 2026-10-05 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 135b433d-68de-3b28-b718-e816b33138e2 | -8.852 | -66.7827 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| d7e97dd2-1f24-36e1-8c3b-080fbb35f2f3 | -8.871 | -66.6521 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 196e3b59-d6d0-3ec7-8aa9-4ae5928a11fe | -9.7499 | -65.075 | 2026-10-05 18:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| c8ab3f8e-ecac-34ed-8866-9f2a02de9a60 | -8.6493 | -66.5839 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b269ac3f-03f7-3180-9a7d-afc80541b223 | -10.6087 | -68.6852 | 2026-10-05 18:20:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 39cefc19-b419-3e1b-b9c5-9281c0f6af8f | -9.3629 | -68.8988 | 2026-10-05 18:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 2801ad28-ebd2-3914-89dd-2aaf7729f834 | -8.5738 | -66.994 | 2026-10-05 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |


[Clique aqui para ver as próximas entradas](README163.md)
