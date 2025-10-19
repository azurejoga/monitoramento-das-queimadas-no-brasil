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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d4c86c9-a8b8-32da-a576-1c817c750595 | -5.54302 | -46.52414 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2694680-0dee-30d6-bc89-e6d2569c1d41 | -5.17151 | -46.11241 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 010544b8-f355-3867-bfe0-75431c6c901c | -7.05058 | -41.82305 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a6834c96-ea37-3146-a08e-97b124de97a8 | -3.1357 | -50.24932 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4247e360-9507-3b76-a3f1-385be0a8cd3a | -3.83686 | -41.77801 | 2025-10-19 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40244f40-e60d-31b9-9507-29d527b128d9 | -5.52195 | -44.11129 | 2025-10-19 04:10:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ba56a22-eda4-3a8d-b764-a8a52ea4413f | -7.16811 | -46.92459 | 2025-10-19 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e66b5491-2ba3-3111-aac9-b10ee7d30162 | -4.93989 | -41.54243 | 2025-10-19 04:10:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 86f110c5-dbbb-3efd-be37-23e007ea6f9e | -5.64247 | -44.81262 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 552494e2-7f86-398f-8f73-74dce8065fda | -2.74168 | -49.39278 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| accb1b62-5a81-3f3d-8d3a-4a5cef981f02 | -3.80253 | -44.15033 | 2025-10-19 04:10:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb3a80d8-8041-3e9c-846d-b7c9e2121f5d | -7.42097 | -40.07183 | 2025-10-19 04:10:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4b4eefc6-8d93-3d83-9d49-f4abc2de7cb5 | -5.83085 | -42.21944 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b6f7f1e-9af1-3dc8-8163-79bd91e2da25 | -7.15771 | -42.36895 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e4205355-b795-34c6-b93c-b23ca1543175 | -7.02505 | -46.66318 | 2025-10-19 04:10:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 948afd9a-1291-3e42-8020-9802c4a98c9e | -3.09158 | -49.22124 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9331575f-e568-32c6-8b28-6c2ed9d46e24 | -5.99583 | -42.80157 | 2025-10-19 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6cef2f1e-1724-39f5-a4d3-6faa9216114e | -7.19711 | -42.18527 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3f218ed5-5f86-34f1-8bed-9595a40d4338 | -6.05519 | -44.52112 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6480528e-c1a1-3a93-ba10-21ba751bd589 | -5.34459 | -42.55229 | 2025-10-19 04:10:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 706a75a3-0ba0-30f7-8625-9d9232f09408 | -7.31433 | -42.46613 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 999299fe-f090-3276-9298-6cd3ee2f0d37 | -6.0602 | -44.5206 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8caa7c59-4406-337e-9bf1-9721a86e3a1b | -8.01717 | -38.54866 | 2025-10-19 04:10:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2b8f5161-7ddd-32e9-a5b9-71fe2b5d7192 | -4.42225 | -40.17228 | 2025-10-19 04:10:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cd81c5a6-e83a-35cf-ad7f-62143c1403a5 | -5.91005 | -44.25233 | 2025-10-19 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bf69966-e883-33e0-a8cf-c4888619c15d | -4.85797 | -44.59247 | 2025-10-19 04:10:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf75f6aa-d6e2-3b27-87b0-04918a8554f9 | -7.9119 | -40.97406 | 2025-10-19 04:10:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d35465e4-2ef0-3fcf-a83f-9597c7960d19 | -6.86338 | -46.29476 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4caa8a1f-b4d8-3218-8a03-637f939a38bc | -2.69543 | -49.54311 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5069bcf7-f217-3845-875e-f7c959089e27 | -2.68913 | -49.54859 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dcfa2466-2bf8-30a3-9e2b-935a5652c066 | -5.78372 | -44.88683 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff0ac78b-95b3-3719-85fb-7d242c8245cc | -5.92464 | -45.44527 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2c946c1-7796-3dba-a8cd-9c2d2854fcb3 | -7.30228 | -41.94526 | 2025-10-19 04:10:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a2eed4f-3844-3cd3-9079-08c9ccf49f26 | -4.23908 | -44.67372 | 2025-10-19 04:10:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15e22827-7606-36cf-a736-be56d31ea221 | -6.17909 | -42.57827 | 2025-10-19 04:10:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5da875c8-ec80-32f1-8008-cd51abd0f313 | -7.41235 | -44.80478 | 2025-10-19 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c43ec7ff-9901-379a-b5fa-b5439c8d570d | -5.33785 | -42.55121 | 2025-10-19 04:10:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ea0da0c-658d-3b4d-a151-06759a9aacdb | -5.69559 | -46.4069 | 2025-10-19 04:10:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4af05b38-b561-337c-9d73-739c173f4dfa | -3.63805 | -49.96904 | 2025-10-19 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48bd5120-8e9a-3af3-b80f-eb865fa001cc | -3.59119 | -42.83649 | 2025-10-19 04:10:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6129daca-d6ec-397d-9602-1f4e45759e43 | -8.19864 | -40.45574 | 2025-10-19 04:10:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0281372c-0f00-3c17-aa5a-94271c54f306 | -2.73651 | -49.39182 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2efaa216-0cd3-3609-aca8-a76e0c63ec1f | -7.01211 | -41.81363 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d55b679-5158-33f8-a319-9dd4f19c39f0 | -5.31627 | -44.84451 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1d0a8fe-afff-3a3b-b19d-2cad75bdffdd | -5.30122 | -45.07801 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9a711b6d-c3e9-3ed3-96a2-21df2017d9d6 | -6.02383 | -42.76143 | 2025-10-19 04:10:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 99de3b84-f1b8-3ba9-b2ac-4c810ff2c3ef | -5.72996 | -44.05274 | 2025-10-19 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aaefe48a-4664-3a4d-94ca-0f276f5bf0df | -4.83694 | -43.01536 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15b2ad27-7310-3c7b-873b-6983a469b5a5 | -5.95083 | -42.23098 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a8d3d19-3bca-350d-bc79-9b415679c29e | -6.59619 | -45.87878 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d75efca-084f-316d-a0c8-560a59a85568 | -5.48271 | -43.12728 | 2025-10-19 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93b124b5-e6e2-37ad-82af-79aa4bc19a5c | -3.75945 | -44.98791 | 2025-10-19 04:10:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2b9d25d-768b-39e3-bbb4-37a4a622e536 | -5.95751 | -42.23203 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48ed87a1-87d6-3dc0-8086-b45c8289c910 | -3.41064 | -43.33367 | 2025-10-19 04:10:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7b92df5-6a21-30ec-9954-7a9baeb7c19b | -7.02565 | -46.65966 | 2025-10-19 04:10:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 443f1dd2-d83b-3ee2-9708-fb4a630f4690 | -4.58444 | -45.37704 | 2025-10-19 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 856a7e7a-2c57-3b78-a546-ac692e0eb3ad | -5.63511 | -44.81147 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 829f20ad-61d2-3568-8bd7-18144c4773cf | -6.14796 | -44.30061 | 2025-10-19 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 048df754-1fd2-3c2f-9e56-2c24eeb7f291 | -7.31711 | -42.47018 | 2025-10-19 04:10:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d9b9f7a-204c-3aa8-84fc-9bac8c3b586f | -6.42002 | -45.97662 | 2025-10-19 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f92d1d9-1695-3c45-a523-6181648e38f2 | -3.88074 | -38.39342 | 2025-10-19 04:10:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12a41d4c-6edb-3e76-8611-d3e796e2f823 | -4.30142 | -48.06398 | 2025-10-19 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26a3fe89-c6da-3e78-a8ef-08f537897961 | -3.39758 | -54.07142 | 2025-10-19 04:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f6e8361-1eee-3478-969a-e9ea9c970c88 | -3.1478 | -50.24408 | 2025-10-19 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1db9d525-9d88-3e3c-afb0-3f0260c11d62 | -5.60789 | -42.74001 | 2025-10-19 04:10:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 37d84567-b723-36f7-a20d-1884d48be070 | -2.7046 | -49.86633 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de366849-9e23-3c41-8135-10e2680cf4fd | -5.1755 | -46.11306 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| caaaa6cf-36eb-3cb4-981d-60d435505f70 | -5.28197 | -42.54618 | 2025-10-19 04:10:00 | NPP-375D | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f91511db-b7cd-3316-807c-b6808361d68a | -5.3584 | -47.2107 | 2025-10-19 04:10:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f1efb8a5-f28e-3b2f-a1ac-0438d78808c4 | -3.59295 | -43.04797 | 2025-10-19 04:10:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c3ee416-2f91-3aad-bbc1-f307ea8c7bac | -3.80186 | -44.15451 | 2025-10-19 04:10:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee986423-9b00-327f-8824-aab25ff4db34 | -3.85078 | -41.77661 | 2025-10-19 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 834e0006-4ee6-3103-a539-b78b3627e35f | -5.31184 | -44.84838 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4e751527-20c4-35dd-9b26-de6d8bf23f89 | -2.69277 | -49.55912 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 26740cd9-02e6-3b7b-957f-1c3d8755db40 | -3.40872 | -43.01154 | 2025-10-19 04:10:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 356a7793-5f4e-3a43-abe1-55f729c86712 | -3.81091 | -51.32431 | 2025-10-19 04:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f7aeb41-9d95-37af-9eeb-b5e601db1224 | -5.962 | -42.13941 | 2025-10-19 04:10:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2df5fe83-6937-3463-a834-bd856a55e41d | -5.93222 | -45.44651 | 2025-10-19 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33956200-9687-3c7c-9dc1-7417ab935469 | -4.98679 | -43.85028 | 2025-10-19 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4079d44c-268e-37e7-a6cc-874a1df3c62d | -5.36927 | -45.27793 | 2025-10-19 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01e11334-c813-3ef7-ad61-0a95a56b4901 | -7.2308 | -41.17719 | 2025-10-19 04:10:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c64213d7-3704-37c1-a953-d8dc2791a96c | -4.42148 | -43.97248 | 2025-10-19 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d59f724-1dc1-3d48-b61e-5613b9d97f75 | -7.05752 | -44.23438 | 2025-10-19 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b0b9274a-ba3e-3d63-8400-6d224f99d60f | -7.19924 | -42.18592 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1c340411-d840-3cc8-81ce-c620347fcde2 | -7.19101 | -42.18072 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d78b327f-2e3d-3f2a-a6c8-0c1bfbdf0e6f | -5.77674 | -42.73048 | 2025-10-19 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2a9b02bb-70f0-3ad3-970a-6a2e31976621 | -5.08532 | -47.18357 | 2025-10-19 04:10:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c5d7525-0b63-3b7c-a676-96124ae71f8d | -6.98317 | -39.69755 | 2025-10-19 04:10:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e6ef558-7189-399c-9e84-34e060d4b0e1 | -7.1616 | -42.36597 | 2025-10-19 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0e3dab4b-a62e-36df-b9bb-8c067ea00666 | -2.44512 | -49.36907 | 2025-10-19 04:10:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 326d2fd3-f12a-35be-bc60-7c13f66345c6 | -4.75691 | -50.69853 | 2025-10-19 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f3807c0-fcad-3e35-a9df-4a8245af7276 | -2.78827 | -49.66074 | 2025-10-19 04:10:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 657f3551-c8f3-3519-b0a8-86d351722252 | -7.19923 | -42.20739 | 2025-10-19 04:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 138a4962-bb8d-3e6c-8d06-036e8024d6de | -5.92854 | -42.24186 | 2025-10-19 04:10:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| faa71332-2edf-32d5-bec6-619abe95a42d | -4.91726 | -45.98582 | 2025-10-19 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd32bcb5-fba5-3f8d-9c6c-de3bcf5e9271 | -3.121 | -49.21946 | 2025-10-19 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fcce4ef-13c8-35de-bbb3-a495491990cc | -5.46854 | -44.88829 | 2025-10-19 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c861ff76-ab31-30bb-82b7-bee83f77cfdd | -0.98996 | -47.07877 | 2025-10-19 04:10:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4554c034-a43f-30e3-bd28-755d58923848 | -4.82636 | -43.05917 | 2025-10-19 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bba77f5-92aa-3d89-9a0d-b58a229ef28f | -7.06266 | -45.20542 | 2025-10-19 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README20.md)
