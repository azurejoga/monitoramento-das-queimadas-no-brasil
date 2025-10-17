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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13bed088-ae85-3536-9b1d-743276310253 | -3.65458 | -50.26928 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ada655d7-3605-3a5c-a9ca-009a96cefb32 | -10.49576 | -43.39899 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b413b6e-c2b7-3333-85b2-a3edbc12259d | -8.16776 | -46.06543 | 2025-10-17 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d45f002-9570-36ed-984a-780a022bb625 | -7.18404 | -41.67929 | 2025-10-17 04:19:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12329879-771d-3193-b761-2f2d6ba51503 | -10.59029 | -47.38771 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d784dfc1-31b4-31e6-b91b-32655a0d7f6d | -5.81707 | -42.33865 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 09cbad34-2339-347f-97b9-074f63c73ab7 | -4.57318 | -43.51135 | 2025-10-17 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 065d8073-547e-3892-81da-baa8970bc9f5 | -7.05307 | -44.25867 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0af169b1-8d79-364a-b64d-0a159401081d | -11.46738 | -44.25409 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67a90ab9-4c7f-33aa-b68b-7e1d2530a343 | -5.24963 | -45.40479 | 2025-10-17 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e6f2a55-f345-3194-8949-acf9e320b4c3 | -7.11739 | -44.73952 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba3409f1-84e2-3fc4-9f07-db53ec9e6a49 | -8.24327 | -43.41198 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 938131e7-d1b3-3784-abb0-349625d6117f | -10.72656 | -47.58582 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5477698c-67a7-3767-b544-dbef3d5bc522 | -3.52933 | -50.31156 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 158794b4-1f3d-3e84-93d8-5941ce19fc8e | -8.20599 | -43.97276 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68ac75cb-0712-399a-b108-5cc96906a8c5 | -9.40852 | -48.64907 | 2025-10-17 04:19:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afd6c2f7-5b2c-3888-aa82-5accfeb0d66d | -5.61411 | -42.67843 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 95248fdf-095f-3daa-bdfc-c9de05d169c2 | -10.52824 | -49.55287 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 0158b648-83a8-303e-92a2-8549788cd3ca | -6.41311 | -43.57942 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5af21efd-76a7-3c14-b905-d358de2c8b9a | -5.77154 | -47.2908 | 2025-10-17 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe2508fb-0c87-3c8f-86a3-0208b3845dfb | -8.59712 | -44.93975 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 442a3cf7-013f-3bc2-878a-23ff51c0bfd6 | -4.30226 | -50.39835 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa37a6c3-1e03-30ae-b205-c3c57af5fa46 | -5.4713 | -42.94221 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f802404-e531-3048-8a76-4148ebe5465a | -8.56097 | -44.58149 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| afc3a422-53d4-31ff-8bc1-e4d7f58dc4f0 | -5.88999 | -43.90549 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d9e3a13-64ce-3491-99f9-9f8b3f1a426e | -6.58772 | -47.07606 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8b8f57a3-629a-34e0-acf3-4533cbe842b0 | -7.48732 | -38.99665 | 2025-10-17 04:19:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ed84a9a3-bc51-31f4-bdd9-99240e9873e9 | -6.04808 | -41.90789 | 2025-10-17 04:19:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 230110fc-3f64-3183-b47b-6c3c571b26b3 | -5.59883 | -42.70994 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c9bd6098-cb66-306d-93da-6c696ca04448 | -8.30416 | -43.42128 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f9f1515-4c6e-3fda-8bec-9d6c5505e8a4 | -7.27906 | -42.9431 | 2025-10-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 49505f53-7834-3439-acd3-c43e8fa7df67 | -5.46121 | -41.01414 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e747f734-f735-3941-b2e0-dc7f65d4c845 | -7.46198 | -42.66314 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 605d19f8-67fb-3ea2-bab5-65575726da6b | -6.43394 | -43.68712 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1223259-286b-3e66-baf1-84515b1b5286 | -6.35374 | -45.48318 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2cb461c-2427-3fbf-b4f1-1950d8ff3d33 | -4.51418 | -46.00705 | 2025-10-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a187606-f7e2-3ba8-9956-71dc7927984f | -10.26172 | -44.04396 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60cdf3c5-d707-32f1-9955-60cf2e7a06f2 | -6.96981 | -42.2089 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9773f26-97f9-3b44-a172-a44fe22fd8b2 | -5.06325 | -40.94611 | 2025-10-17 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea35e0ee-2459-36f6-adae-59178bf7db2f | -9.21982 | -46.8898 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dd52628-fced-3db4-bdfd-21aeb62243ac | -7.98298 | -44.16201 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dca31e0-c1c0-32fa-891a-73a29c41daea | -8.0876 | -45.43251 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d05ebb00-7ac7-3cbe-af5d-76e88929f800 | -8.21904 | -43.3112 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 910506d2-a7b9-3c4f-b38f-713c6e5b0659 | -8.20933 | -43.97329 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ef4275e-78ed-3410-8f83-b152700a4542 | -10.64228 | -45.21944 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04b3483e-0c67-3994-ad57-adce5a05f073 | -7.17492 | -42.52329 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 597207a6-8cb9-39a6-a477-4934b8340e4e | -9.34619 | -46.9102 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caf0a016-0e79-3212-b864-a78e3ce06c5b | -5.14643 | -46.05363 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6b4b993-57c0-3b34-bc82-0e72a114c31a | -7.95623 | -44.09303 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39a34735-6644-3b0b-aeb3-e831c8df1cf2 | -7.11355 | -44.74245 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5525fd3d-a4cf-36b8-8a73-2ebd0af0e35f | -5.24686 | -43.00766 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b724de5e-a7c0-3e53-ac7e-97b7d135d60c | -7.95569 | -44.09656 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e7367ce-1a6b-3129-bdb2-83566611fa1a | -2.87687 | -50.73906 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd7221f1-eb29-3480-8777-b0a4b37ff36e | -11.39452 | -44.1412 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 298b88cf-5626-3a13-8e52-37399d5223c8 | -2.9587 | -52.5061 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16f05282-2d7c-3f52-8c98-644d2beaaf8a | -6.20301 | -41.77033 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 890556f8-821d-3353-81d8-33da1cfcd154 | -10.08572 | -45.34093 | 2025-10-17 04:19:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dbc8684-58f9-33ae-9a10-9586d1a31036 | -6.76173 | -42.38126 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 79190d29-a642-35ab-9c0a-9ddc9462fdba | -6.70295 | -44.38783 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44148ec9-826c-3a5d-ba7d-5dba6ffba264 | -7.83877 | -45.45721 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45c6640f-0639-3a64-b16a-c74675ddf927 | -10.50783 | -43.41234 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e0fb7a3-ce53-3862-970f-badf8a564d95 | -10.49928 | -43.42237 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84658089-db56-3195-9fe6-b992a377b38f | -10.27966 | -44.03927 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c4fcb0c-17e0-31d8-ab67-33e4430ce524 | -8.5665 | -44.58949 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8848a2ce-7209-399b-a611-d42d8de02541 | -6.95765 | -46.13729 | 2025-10-17 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc035544-f5bf-37c2-b4fe-f6c8f5b7f437 | -5.88444 | -43.89755 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5e2be47-ea3d-3439-b3d4-ea08228c65ce | -7.20416 | -45.48726 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 049fa460-0506-3d12-8946-43aab3f802d9 | -6.14907 | -41.79275 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ccba867-5885-3af0-9d36-6b136efe3144 | -4.22234 | -48.35812 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56c3c7c8-968d-3258-bea1-279c29c474d9 | -4.43507 | -50.54876 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f7263c9-ad90-314e-8cc0-9cc3a0def36e | -10.26454 | -44.04807 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f061ad6-a65e-3b7d-b8a8-3f465f31a4e7 | -5.45807 | -44.64559 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3d3206f-d11c-3401-8990-c68a3dfa0ad6 | -10.23133 | -49.86375 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7137420f-d966-3363-86ad-a3fe0e2d2dde | -4.89534 | -47.63633 | 2025-10-17 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad960c33-8124-3cec-b1a1-4665eaf2b159 | -6.32288 | -44.31385 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86a31531-2783-3413-b08b-365ca4263af5 | -11.47752 | -44.27817 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d78711a0-743c-3608-a9fc-ed31245fa1d3 | -11.14566 | -45.85479 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 017a4137-33a1-3d95-b1a0-50795201d734 | -5.83934 | -40.81215 | 2025-10-17 04:19:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 93ae069a-4b50-3385-b4e6-e4e7d32200d6 | -6.94322 | -47.72197 | 2025-10-17 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fc50db4-a1db-3e51-8e85-789584797de5 | -4.61033 | -50.91178 | 2025-10-17 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f19bafe3-0edc-3821-bed5-e9f30b71d23e | -4.4546 | -50.89181 | 2025-10-17 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e79390fd-592e-3af8-b183-9c736f03bd36 | -11.39838 | -44.11536 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 059cd6d7-716d-319f-8118-814ffe42f898 | -7.52991 | -46.83764 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8803b809-2597-3007-8654-44c2b49b8122 | -7.95413 | -44.12875 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd5aa3fe-cd68-30e8-ada4-ca17e231a1d3 | -10.44589 | -44.57556 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3d48dfc-e3fd-38db-87a7-b1a25772137e | -8.26095 | -44.07882 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8374835c-d5b6-3f09-b79d-cab2a447b285 | -6.85246 | -46.9844 | 2025-10-17 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e662d8e-0ac1-3986-9176-e5b48288168f | -3.47613 | -50.02244 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52af3c03-dfc9-3194-b364-b64d650a2971 | -10.89005 | -47.90022 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a4c3fbd-dd95-3cb2-a15f-ff7087aee524 | -8.23604 | -43.43699 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8217dcc9-2cc8-3d07-8951-dca1d13282db | -10.62043 | -42.31169 | 2025-10-17 04:19:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c790a67c-535b-3d79-b37f-2e6fe79c648d | -9.14235 | -46.63885 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 651b66d8-2e24-3324-b315-078b472e63d9 | -7.83081 | -44.13413 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 060b6390-7c26-30b5-9f46-0b4a3537af16 | -9.72124 | -48.91326 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b98e0fc9-a8de-39b6-bfa3-6b85431a4ece | -7.28863 | -42.30323 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f3064b48-50e2-3685-80c3-7fd60c0db36a | -7.20582 | -45.49821 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71f9f543-26bb-3473-90ba-812a8e6332ef | -7.56861 | -47.14041 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a90ad6b-2277-37e8-ad05-ca981929b49a | -6.36951 | -41.47779 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c282a505-a758-3a0d-aaa3-d7444b8bef01 | -7.11978 | -44.28683 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df664870-ab6e-3716-bdf2-15c1570568b4 | -5.79261 | -42.50023 | 2025-10-17 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |


[Clique aqui para ver as próximas entradas](README41.md)
