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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6f9e357-7767-32dc-8162-e0887a3ccd6c | -9.043 | -48.1384 | 2026-09-23 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c789182f-2ce2-36a2-a3a2-64afbaa6d84e | -11.0241 | -49.7088 | 2026-09-23 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 02b1e64f-3c39-3d7d-a34f-75daf93a6f24 | -8.8105 | -44.2757 | 2026-09-23 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ceb6c107-a5e7-3ef5-8c4b-cca8fff4f1d8 | -6.3198 | -59.9572 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 66a75704-47ee-3525-9f27-de34197eb9f9 | -9.9163 | -45.0885 | 2026-09-23 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| e0ef75cb-cfcc-38c0-b25e-5bd92e5d85f8 | -6.4368 | -48.4436 | 2026-09-23 14:10:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 917c727d-b4e0-3174-af34-add072094b1d | -7.5704 | -57.6766 | 2026-09-23 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d1aaa7e8-cced-33b6-b210-d54e9b84ac15 | -11.8559 | -49.979 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 6abe0cac-bdfc-3961-a7f2-2818a5387a62 | -9.5854 | -48.4549 | 2026-09-23 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 680c325d-293e-32c2-8e3f-4dcd8fbbaa9c | -6.9741 | -43.3497 | 2026-09-23 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 9981eda6-5ae7-3b08-9f32-dbf9284ef57c | -6.6127 | -43.7549 | 2026-09-23 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| ef347e0d-92d6-3d26-a0ea-37453695c8f3 | -6.9738 | -43.3731 | 2026-09-23 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| d1f60877-e114-3c5b-92ce-fc95067b148a | -6.4486 | -59.9717 | 2026-09-23 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| c3a4031d-1eb5-3f60-a38e-0331de784079 | -11.6986 | -43.4654 | 2026-09-23 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 78d4b93a-6822-3a36-876d-b9d59a53b8b0 | -6.6317 | -43.73 | 2026-09-23 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 174f9d03-cf33-3b7c-989f-918a3a605ae4 | -6.6148 | -59.908 | 2026-09-23 14:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 0e7b43b9-7a83-3a76-a23b-d6f0dc0fd1be | -11.7406 | -50.0572 | 2026-09-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ff8888ad-3942-3329-b8e9-48c3a0437227 | -4.2816 | -55.4297 | 2026-09-23 14:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f3fca5d1-e833-3ca8-abb0-d7c5f04d7b3a | -7.2693 | -45.5511 | 2026-09-23 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8e8ae6d7-d866-3721-a1d7-9d78a3227403 | -6.8951 | -59.2235 | 2026-09-23 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 06a6be09-64eb-3a05-a838-2adcc18aa1c9 | -14.7231 | -41.601 | 2026-09-23 14:10:00 | GOES-19 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 109.3 |
| e92ba7f8-30c6-3f62-977e-5e6f3ce374f6 | -7.8773 | -44.972 | 2026-09-23 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 1ca6cc72-fd99-3fca-bd84-2f531b25e470 | -10.3788 | -54.4183 | 2026-09-23 14:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 9ae73a4b-ba66-3bbd-ad8d-1a590dca69e2 | -10.0259 | -45.3724 | 2026-09-23 14:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 07ec8e0a-3ed5-3ccf-bafc-ff5fb3182ec2 | -8.754 | -44.2589 | 2026-09-23 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| c409b1bf-8772-387b-baf1-94112540b8ad | -7.1203 | -42.083 | 2026-09-23 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 241a160b-d59b-302b-a053-9702a48c4745 | -3.7167 | -54.1896 | 2026-09-23 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 266.5 |
| bbcf5691-86ee-3b1e-9105-a7df8236afc7 | -9.6043 | -48.4529 | 2026-09-23 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 1af005aa-eb62-3f21-8e0f-ccbd3b795bd7 | -9.5857 | -48.433 | 2026-09-23 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 40f011b7-53c7-33cc-81b8-9e1d741e0c47 | -10.5087 | -44.8748 | 2026-09-23 14:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b07157c7-a60b-32a5-9aa2-bd367b950350 | -9.8494 | -48.4709 | 2026-09-23 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| feab6294-26f2-3f3a-8827-63c8c7d00bc5 | -5.65 | -51.62 | 2026-09-23 14:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78157bb4-a275-346e-8174-6ebe37d0ca2f | -5.62 | -51.61 | 2026-09-23 14:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f430a8-c94e-3de4-9698-9d1027b50483 | -7.1392 | -42.0811 | 2026-09-23 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 132.1 |
| 8055523c-bcdf-3944-a15b-9f689e451aca | -11.782 | -49.8368 | 2026-09-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 939efa9c-dc48-37f6-996d-0275da1c8c6d | -11.3054 | -44.0198 | 2026-09-23 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 423.8 |
| 52e164af-4fb0-3ff7-a7d5-9e436b8063ff | -7.0352 | -44.6396 | 2026-09-23 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| b05bbeda-e541-3398-a60b-62881a160d5f | -9.1525 | -49.9639 | 2026-09-23 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 493be676-bf7e-3532-99ad-742fab1ddb28 | -6.3382 | -59.9566 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 29609a9e-7ecf-302d-950b-7a726ddd8119 | -6.2949 | -41.7785 | 2026-09-23 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 110d716c-108c-397b-b72b-8ef0ea3d1964 | -7.9904 | -44.9608 | 2026-09-23 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| c0191c2b-ff9a-3cad-abe1-1164d31aa1ab | -7.8811 | -61.1779 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2910a47e-ab23-3e70-b82a-99747ada4031 | -7.1088 | -43.0792 | 2026-09-23 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| f822a041-9abd-3780-84f5-143b390c903a | -11.3547 | -43.4001 | 2026-09-23 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| ffaa5025-5af6-302a-b06d-d31a3a9335a6 | -6.5639 | -44.8628 | 2026-09-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| bcd622c0-e738-3230-80c6-53a07381a122 | -9.1771 | -46.5101 | 2026-09-23 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d0a98d90-4ae3-3d36-b26f-3407b25de01d | -9.0242 | -48.1403 | 2026-09-23 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e34dbc97-e200-312f-bd27-3c74d40bf0ac | -7.1277 | -43.0774 | 2026-09-23 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| fe1d5518-6b55-30eb-9a35-d0dd234fdca0 | -11.7406 | -50.0572 | 2026-09-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 26868caf-cf8a-3276-b09c-f191d9a03ea5 | -6.4486 | -59.9717 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 477607e3-bbce-3599-a89c-47cd45c4500d | -6.5756 | -45.5645 | 2026-09-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 21bacd00-f069-3c17-b5cd-7c10e6982918 | -6.5759 | -45.5419 | 2026-09-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 8fa75981-6afc-3a29-8fa8-ea5978d7fc34 | -11.0614 | -49.7477 | 2026-09-23 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 24837f6d-c591-3aae-afd2-39c6d45b7029 | -11.8014 | -49.8129 | 2026-09-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| d7af18b5-ea79-3662-a4d7-df468db8f9ca | -10.3976 | -54.4167 | 2026-09-23 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 4a1f39cf-d1fd-3c4f-8094-bd4659b72698 | -12.0507 | -42.1381 | 2026-09-23 14:20:00 | GOES-19 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 25712c9d-3b26-3a41-bd6f-05dd2b36e09b | -6.1359 | -59.9446 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b49e431b-260f-39ad-bf70-d3f3a2c466a9 | -6.2205 | -41.6891 | 2026-09-23 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| f861ed74-f8ff-3ebc-92ae-6d4b289e449f | -6.2219 | -45.3665 | 2026-09-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 3e255607-392e-3d39-a228-61c308526af4 | -2.9525 | -57.72 | 2026-09-23 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0671377b-e5b8-3959-97e4-27f161ae71e6 | -7.4286 | -44.7409 | 2026-09-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5b812281-9666-3338-b05c-350d6c4e1de8 | -6.6331 | -59.9265 | 2026-09-23 14:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 364.5 |
| c499451f-64f1-39b3-ae63-89d936c59417 | -6.4302 | -59.9724 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3e7b921a-a992-3e84-a04f-3cfc28303ab3 | -9.8497 | -48.449 | 2026-09-23 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| c0127225-6652-3723-884c-fe9c06e10850 | -6.2208 | -41.6651 | 2026-09-23 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| bdb22380-04b1-326c-9acd-895cbb5673d3 | -6.5636 | -44.8856 | 2026-09-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 9589f558-33d6-3ba4-bbcf-b9873180fea7 | -9.1708 | -50.0049 | 2026-09-23 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b1531bf5-8704-3502-b428-722021abfdc6 | -10.5561 | -46.7095 | 2026-09-23 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 54cbedf9-19d5-336b-8641-6b9c22a13359 | -6.3014 | -59.9579 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| e6dd06e8-2c2b-3474-ad06-88df40f34928 | -3.3138 | -59.4472 | 2026-09-23 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ee01f198-e77b-30a7-b83c-6395025c99da | -9.6043 | -48.4529 | 2026-09-23 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 4d2762dc-b3bc-323a-98fa-66df484c8f84 | -6.4671 | -59.9711 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 0226159a-cfd9-3442-bc55-dc2c2722c8bf | -3.7167 | -54.1896 | 2026-09-23 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 777dcc0c-6db0-36f4-92a6-f430f9b70433 | -6.2396 | -41.6634 | 2026-09-23 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 18b3fbee-b37e-3686-b14e-1f78f5731d94 | -9.5854 | -48.4549 | 2026-09-23 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 458.2 |
| 80886d86-5987-39d3-8731-94629df2e82d | -6.3199 | -59.9381 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0c519460-e3f0-36f3-83e1-cbfd8c7da7f8 | -6.6332 | -59.9073 | 2026-09-23 14:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 8ae3aeac-c130-3770-ab9f-4ebb104f4370 | -6.3198 | -59.9572 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| d245cfc8-3636-36a9-b506-11ff74ff66dd | -10.0259 | -45.3724 | 2026-09-23 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 309.6 |
| 6e279e4e-adaa-3820-ae88-a92e721ab5f4 | -9.406 | -47.7507 | 2026-09-23 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 34edf6b0-6dc9-3fdf-9635-aaed5c10cd29 | -7.41 | -44.7198 | 2026-09-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| c77b2692-89cb-3e40-a29e-1652417f0af2 | -6.202 | -41.6668 | 2026-09-23 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| f63ca1ef-4d74-3127-8579-c386e0927185 | -6.1849 | -45.3241 | 2026-09-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9c056013-6f52-33d0-83a2-7d84b318cc82 | -6.9138 | -43.7049 | 2026-09-23 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 36cd5710-695d-37f2-a25b-4364f1f89ffd | -11.801 | -49.8345 | 2026-09-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 23a25942-a6e7-35a3-aa75-a7d990efb2b3 | -8.3591 | -45.6056 | 2026-09-23 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 37731b88-63bd-3c02-8679-b5ec1fdcdb5b | -10.3978 | -54.3963 | 2026-09-23 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 7e3d5b12-9665-35d6-9267-cc0face6a409 | -6.5962 | -59.9279 | 2026-09-23 14:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| feb299b6-cfce-3ca8-b25e-6b62c915c406 | -11.4162 | -45.3486 | 2026-09-23 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| e551c414-e7bb-31eb-832d-6a51715e84ef | -9.5735 | -46.5337 | 2026-09-23 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 456e416b-52fa-33e7-8ac5-8665663bbf22 | -11.2862 | -44.0226 | 2026-09-23 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 430.8 |
| fa8b6d65-b9fc-3c43-8f2c-f57103233ba6 | -11.7784 | -50.0743 | 2026-09-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 9f4c031a-43df-359c-9a5e-029d9fd23ef2 | -7.026 | -42.0924 | 2026-09-23 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 22c815f1-640a-3686-899a-eb0bb7a5f72b | -6.6515 | -59.9258 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 0fcc27b1-05eb-380f-979b-0c9ded62662e | -6.9927 | -43.3714 | 2026-09-23 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 23353da4-0f23-3428-866c-7dc730f5104d | -8.0921 | -44.3538 | 2026-09-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f94d97c8-f283-3257-bfe7-956f485200ee | -5.9985 | -45.2476 | 2026-09-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 9e82ec79-1aed-39d5-a7de-ddcaacaf2d06 | -11.2858 | -44.0461 | 2026-09-23 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 417.3 |
| 03c849c1-774f-3fca-8d1f-1fdf4567e366 | -6.2036 | -45.3227 | 2026-09-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 49307299-abdf-3d86-a02b-99f0b37ee89c | -11.699 | -43.4416 | 2026-09-23 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 399.8 |


[Clique aqui para ver as próximas entradas](README141.md)
