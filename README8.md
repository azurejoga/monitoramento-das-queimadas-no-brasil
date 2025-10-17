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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a54bd22-0e34-3864-9046-231253b2c829 | -10.83054 | -43.93969 | 2025-10-17 00:13:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0925beec-1ae2-3dea-8712-90f268dba289 | -7.71757 | -47.84645 | 2025-10-17 00:13:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b5f7ef7e-b79a-32e1-9485-2a1c18639ed4 | -7.00072 | -46.99094 | 2025-10-17 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 223f979e-4dca-329a-922c-05b01e187b5f | -6.18413 | -42.62601 | 2025-10-17 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b68a4e74-b8d6-3b6a-b346-769a5b92efef | -6.13553 | -44.30098 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 59b04e22-5d29-3608-9e63-e7dabbfc1536 | -4.87789 | -45.93773 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 93014dc6-5e59-3d85-ae6f-c4d1df1964d2 | -6.05484 | -44.3183 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e8bfd30d-3abe-3007-acb0-f9de5688c011 | -10.61263 | -42.32029 | 2025-10-17 00:13:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| cdefe978-98b8-36b6-b83b-76b15c85729b | -4.39869 | -43.42059 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 28d57d48-e3b5-3232-bda1-bc207fc7b627 | -4.4227 | -43.40091 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 17a93a3d-b0df-3259-b01b-65de0f4b2c9d | -5.87971 | -43.66215 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 397416f6-4cf4-3afc-a6ca-b9bfc2f36923 | -10.83794 | -43.99328 | 2025-10-17 00:13:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1cc538b8-c6bd-38d0-b400-5c130230acca | -4.39735 | -43.41101 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 281.1 |
| 2447b4ae-6c7c-32a8-b981-f2e2eea62955 | -9.92951 | -43.42448 | 2025-10-17 00:13:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| fbd52243-6a56-305f-88db-f89bc5f5e941 | -4.38954 | -43.42194 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 30e9335f-dc36-3b2e-b3b0-4aa9a3bba223 | -6.60112 | -44.80452 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| a62148fd-d18c-3f8f-b1f2-a24f212a0b47 | -7.95596 | -44.1354 | 2025-10-17 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f38cabf3-58c4-367a-8fb8-a95a50c58224 | -6.13903 | -41.7467 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| aa0611c4-5a5c-3fad-a256-689a1c58a19c | -4.87851 | -45.54724 | 2025-10-17 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0088efcb-7231-348c-9013-a0c85fc2a5d2 | -6.31614 | -42.77211 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 130be48c-8b9f-3722-b8ac-773a76087b0d | -7.74497 | -42.5146 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 02f18e72-8f0f-3a7d-8d75-e94d74b088c1 | -6.17261 | -43.45154 | 2025-10-17 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a1bd8670-a962-3df4-b3a7-8b3770b25fc2 | -10.10272 | -44.61097 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6aaa2a84-76ec-3954-9443-9229f52e776f | -7.33662 | -43.86762 | 2025-10-17 00:13:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e3f9188a-4242-38c5-bfb5-12eaca4732ba | -5.51577 | -43.30624 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ffec0abd-5298-312a-8ef6-7b7da244172f | -6.35734 | -41.48826 | 2025-10-17 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| fb02bd27-5c03-3860-ae2d-d1043531f467 | -10.81167 | -43.93331 | 2025-10-17 00:13:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c3e94b9b-f0bc-3644-8439-80b60657d4c4 | -10.49412 | -43.37866 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90dec8ef-4437-3dca-b5f3-636ed0f9ca82 | -10.57316 | -43.60711 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5b455821-4632-3a3f-8e01-5a13b94bc1be | -4.42296 | -40.18179 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 72d84b5e-f1ba-3e1c-8a8a-f6bff85c32f8 | -6.26459 | -43.90624 | 2025-10-17 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c6ad21ad-c4d9-3ae0-9a90-e91decc205e2 | -9.71996 | -48.90273 | 2025-10-17 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 4c953389-8502-3a48-8f6b-13e55d2eb0bb | -6.17047 | -42.5974 | 2025-10-17 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a1aa4628-d52e-356a-8284-3496feb80c90 | -6.75697 | -42.36176 | 2025-10-17 00:13:00 | TERRA_M-M | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 909ade91-e61d-3c0a-a6b7-8a54eda69a71 | -8.41455 | -46.29389 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a114d7ca-4f03-32a0-a0de-90706afabc36 | -9.88913 | -47.68121 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| d8b3eb11-f964-36a5-a285-b4e35996ad34 | -5.25471 | -44.20609 | 2025-10-17 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| c54edd47-3cad-3fb9-9b7d-593bfaf4ab11 | -8.83097 | -47.2999 | 2025-10-17 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 01b22d46-7d24-30f2-99e0-0c8b9853bfd4 | -10.13536 | -44.5723 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1f072c4d-bbfe-3c92-a71f-b2dda62ed822 | -5.95454 | -42.24427 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 320f0f04-6be0-30e2-a9a6-6a841cc3c623 | -5.71282 | -46.45699 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| be736617-12ac-354f-ac92-0b0048134ecf | -8.4072 | -46.29074 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9f95d142-e752-36b2-b0b8-bc1a8ad513bd | -10.05599 | -43.86426 | 2025-10-17 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3a88b34e-a04e-3269-9905-59d3821a0fd8 | -7.66397 | -42.59206 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 56e3bea5-4bc3-3eb5-92e9-713d7481f6ad | -10.57259 | -44.53489 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 164d150b-59bd-3161-8bd4-8152176b2dd5 | -8.25369 | -44.02896 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5bb4fd91-09d0-3787-a489-130da821ad0b | -5.23388 | -41.79137 | 2025-10-17 00:13:00 | TERRA_M-M | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 94ebcfb2-28ec-31c0-93c3-89be8cc3b327 | -4.42133 | -43.39137 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 05472ebb-8490-3cf7-a661-92e71cde0e2d | -6.31716 | -43.62482 | 2025-10-17 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ae785ca1-a6a3-3fbc-9c05-023b5bf153ee | -7.18078 | -42.37168 | 2025-10-17 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 5616cd0b-0ced-326b-a352-57afc3041570 | -8.1904 | -44.10762 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1568ca25-93e7-3658-95af-1185e5b42d70 | -5.85276 | -43.86693 | 2025-10-17 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| acc553b4-2002-3350-bc45-33acf64a57bc | -8.22228 | -43.99728 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 99f33b21-3b5d-32a9-afd9-7acbe2d43cab | -6.55957 | -48.04489 | 2025-10-17 00:13:00 | TERRA_M-M | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 13ba8277-5b0b-3b0e-9a66-7f212a3b9040 | -8.47746 | -44.18349 | 2025-10-17 00:13:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e8f67aec-9d3a-310d-a16f-4722fc8b4de0 | -7.90713 | -44.98612 | 2025-10-17 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 874b6084-858a-3755-b1ba-e093bcb8c39a | -7.47089 | -42.15964 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d5d9713e-a9a7-3b16-ab08-380fc7f086ae | -6.1719 | -42.60732 | 2025-10-17 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 2896a78a-bfe3-3470-99a4-72a84faefaf9 | -7.05996 | -45.05165 | 2025-10-17 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 60caf316-92dc-3e85-b8a4-7e65a66a37e5 | -10.53061 | -43.36704 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1f3fc7cb-a993-3853-9dac-01c84244ef79 | -5.64882 | -44.71299 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4ec63a13-53cc-36e2-9a6b-b80a576e8f8e | -9.66411 | -43.89097 | 2025-10-17 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 40a02b18-d5c1-3833-87a2-4ce19b32cb3f | -9.05467 | -46.9966 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d56d0e3-6f6b-38c5-83ac-73fa587b1983 | -4.50945 | -46.00471 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 8eab0fd9-df93-3ea6-8783-ee2061f43aa6 | -5.70631 | -44.52771 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6982cfc5-d653-3305-b635-b361eb936b9c | -6.60993 | -44.80328 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 83c05cdd-9a2c-3001-bed5-ff58e144677e | -6.74406 | -44.37619 | 2025-10-17 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d645ffb4-de73-3c46-8e04-5c4ecd29a05e | -6.43606 | -43.68515 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59060414-48e6-3905-935a-435ce3dfe763 | -8.46742 | -44.1759 | 2025-10-17 00:13:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fb247f5a-16d5-3c26-b572-a52425c76270 | -6.95691 | -47.72633 | 2025-10-17 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| db444439-0bd0-3ff4-b74b-7a52760564dd | -8.4464 | -46.24944 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| b3ff1254-cd65-36ea-b8a5-c516be6adb06 | -8.25245 | -44.02009 | 2025-10-17 00:13:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 608ea851-3447-3956-8fe7-15f48d040e2b | -7.40415 | -44.74353 | 2025-10-17 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f9a6afa5-ecdb-391f-95a2-33a6dcfd369a | -6.20787 | -41.73624 | 2025-10-17 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 7c388810-4c6e-316f-9b67-95ab7b885713 | -9.58398 | -47.59663 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 58498559-fb5c-316f-ae77-4ca08ec05e38 | -10.14053 | -44.54394 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 854da084-9300-3720-8088-df7403faf9fa | -7.11691 | -44.73089 | 2025-10-17 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 354dd2a9-a09b-333f-b894-ef24a4e073de | -10.10662 | -44.57361 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b365038a-5ed1-3b89-82cc-9eda767319bb | -4.40385 | -43.39058 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 64205e91-de82-3950-931d-1df51d691dd4 | -4.38283 | -43.37414 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a4248b3b-3c0d-3c95-af15-1f3dab884074 | -4.92733 | -46.77473 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 330d4e7e-1a5a-3d1e-8e1a-a03e76b25b30 | -8.08033 | -46.66568 | 2025-10-17 00:13:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a2c9e5b6-152b-3322-bcde-e3415f436950 | -5.71513 | -44.52647 | 2025-10-17 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 02ec5c02-7999-346c-b709-64d440c3f574 | -10.71019 | -44.53652 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 60879cb5-3f40-3a3f-afd9-cf4f10daa39e | -4.95451 | -44.95869 | 2025-10-17 00:13:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| f5355326-5627-395c-8aa4-9d804fb335a1 | -8.82038 | -50.052 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d6ec196d-1594-3b76-8fa8-b4e7d3ecd8d7 | -9.24035 | -44.36915 | 2025-10-17 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 00990152-fe6b-3ff8-8bb0-e2d564b8286b | -5.20658 | -46.18774 | 2025-10-17 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b3eb4698-d9e0-37b8-a32f-f76925b4fced | -10.10787 | -44.58268 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 69d66f9c-1f20-37aa-a43e-179441388154 | -9.97899 | -47.0209 | 2025-10-17 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ef515edb-956f-3552-842c-f3951098cd79 | -10.50036 | -43.4233 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 9331cd88-e8ad-35f2-ab83-df14e7a1aaca | -10.15703 | -44.53249 | 2025-10-17 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| ca7fb3c6-7f3b-3fad-9e07-b24eedc04518 | -4.40518 | -43.40014 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 6f7e4a0f-0c46-3da4-8375-4766e770df14 | -6.23554 | -44.16278 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f5d19b8-a43c-3eec-8d72-900482565f8f | -7.46356 | -42.14573 | 2025-10-17 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 93799cb4-a258-360b-8232-4094a47b973e | -11.14431 | -45.8563 | 2025-10-17 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 45701c83-c320-3b73-a6a3-fc587113e8a4 | -10.88067 | -47.93257 | 2025-10-17 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f6c85a92-5b2b-35a3-b134-acf9b66aebfe | -7.46305 | -42.67369 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 50dae29c-6a1a-3ae8-97d4-0f5954728c7c | -6.14204 | -44.21844 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 846cdc32-f529-3d33-974a-87856f965c81 | -8.40044 | -46.2411 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |


[Clique aqui para ver as próximas entradas](README9.md)
