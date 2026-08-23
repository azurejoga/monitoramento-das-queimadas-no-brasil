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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acbdd97c-43b3-3ffc-9d8b-4c9afd34dac8 | -7.01662 | -59.56881 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3226a66-f94e-3374-bed7-e740124bf53e | -7.29773 | -42.99931 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c45b893-6689-3f9b-9cac-ff2630853757 | -6.76791 | -59.44719 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e0171d4-ac77-30c2-8794-aba6bc4e0037 | -5.77268 | -57.58131 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 771e1169-f8b3-3d0c-9e44-12ffa767da0a | -6.19006 | -53.5149 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1791fe66-371f-347d-9ca6-b552770f8a42 | -6.90073 | -55.70526 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf652ea1-efe9-3ee1-b5a6-069066591d17 | -6.97653 | -59.06674 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74f40ea4-8817-3b94-b5c7-30320eadb5e1 | -7.01375 | -48.01778 | 2026-08-23 04:44:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 764cd7a1-f1ee-3326-b0d7-240b8dc50842 | -6.76929 | -58.67672 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a4fafb2-e9c4-3686-97d4-3776d2d32a7d | -7.48993 | -55.33073 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e79e9f2-acd3-3ee7-a362-f4386c5cd5ac | -1.7458 | -55.25255 | 2026-08-23 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53fa57e4-650d-3ee9-8547-2aed472983fd | -6.67384 | -58.74622 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 0b126b20-c081-39d0-9479-4d90ebabe4f5 | -5.96392 | -53.62323 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e784fca-11fc-33d8-9b3e-953f3124e6a9 | -5.94914 | -52.12895 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1328eba3-ae97-3fd7-98b1-135b5a613d79 | -6.75605 | -58.683 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4ca32a3-56e3-3972-aa45-5e5e5839f80c | -8.92729 | -48.54417 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ac9a74ef-6022-3e37-89c6-aab1df26bf93 | -7.98295 | -45.26216 | 2026-08-23 04:44:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e335cbc7-6e6b-393a-8ff4-77180483a216 | -6.61168 | -58.39364 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f081c86-9c7b-35c7-911f-ceb9095ba2a7 | -6.19167 | -53.50628 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f51610f7-50d1-3450-ba7f-35f6b192b397 | -5.62041 | -45.69179 | 2026-08-23 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2752266-061f-37ce-ba8a-fee50ddc135a | -6.55737 | -55.09817 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 766d0128-25ad-3d96-89d7-f08c9056434b | -7.26512 | -49.91109 | 2026-08-23 04:44:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 781623fa-6c5d-3259-8e27-b0528938f16f | -5.77817 | -46.11846 | 2026-08-23 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af2327e7-9dcd-3d8a-bc3d-78b22eaf9b21 | -7.42168 | -44.6856 | 2026-08-23 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3206c4a-c584-36fc-803e-9e5365ed9aa5 | -6.17188 | -55.56601 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26a97f3f-ea8f-3436-b69f-97f6dd927625 | -6.17434 | -55.5734 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc35797a-e62f-3429-88e9-6d524ef21beb | -6.54075 | -56.2607 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5f4b2a1-8e5f-3f34-a9af-7d462430f433 | -6.75333 | -45.25666 | 2026-08-23 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b387d1f-282c-3b57-bb46-f92c78d186c3 | -6.67899 | -58.73896 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ea720574-c006-3d99-a9d2-4473474466bb | -5.77333 | -57.57761 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44b29600-8884-3d9d-840d-4dc3144d33ce | -4.26365 | -48.19577 | 2026-08-23 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07c70597-aacb-30f0-9f7d-c88ba4eafa48 | -6.92283 | -46.40872 | 2026-08-23 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8a5e9f-376c-3f7a-bb6b-18564a122c28 | -6.94842 | -59.08474 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7d3cadab-fed3-3bcb-b1b9-180f84235407 | -6.94576 | -59.06569 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89d34f84-44ba-3238-935d-14333e34c9b7 | -2.96224 | -48.74993 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1bbe1c3-56d4-3da4-b32e-5ca4a5249cbf | -2.5628 | -47.24932 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9c8a0b4f-99cd-3fcb-bd9f-7a789097fbce | -6.20161 | -53.08856 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 221a8bc1-480f-332b-b059-a972792aded5 | -6.1974 | -53.52308 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d9dc8cd-550c-3897-b2e3-10ccbee4ee08 | -6.69235 | -58.73261 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1736c8b1-9bf9-3bf3-8990-c6d3bca38a61 | -6.19674 | -53.52694 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c66ff341-c8c0-3930-baaf-3fc4718826ef | -6.78685 | -59.65633 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25c4a480-9284-3b7e-acb1-c5b713e97f14 | -7.69373 | -44.81248 | 2026-08-23 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e107fcd1-70e4-3d4f-bf52-f16f97e01249 | -7.47764 | -45.13236 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32066c70-c2a5-39d1-b5ef-a91dc026fffa | -6.78717 | -59.412 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7257096d-a095-3bf9-863f-6cf614e8f258 | -6.79611 | -59.79698 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 950fd94d-eb5a-32a2-b37c-4cb4e8a5032a | -7.47699 | -45.13666 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f227ebb4-2178-31f9-9ccf-d40f6a69f23a | -7.01224 | -59.55789 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aed852ab-9af2-318e-9a41-98808174dc2c | -6.94217 | -59.07754 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 459dd8de-f883-3ad5-b608-d943193ee1d7 | -6.80897 | -58.98083 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a951b1f-50c8-3d46-a474-99e2a2b41214 | -6.7933 | -59.41314 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6c37241-3eb9-37e8-94f3-3f378a12bc16 | -6.69155 | -58.73694 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b452f71-4a57-335f-8b7b-cf04c3ff4923 | -6.81109 | -58.64574 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5c65cd0-cacd-3727-9f85-5158ee68c2bc | -6.67157 | -58.74616 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5982f784-9c11-3381-8b71-4df6e4a9ac14 | -6.66203 | -58.74409 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e6cdc43-21e4-3540-bca3-96d903e97784 | -3.69041 | -50.93169 | 2026-08-23 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bc848dc-8c22-355e-9b00-7dec45e46f5d | -6.55347 | -58.51797 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38deacfd-7431-358f-9a7d-48da30e2b203 | -6.11632 | -59.92925 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a101b1-2621-3d9b-9cbc-edc55ece31fa | -5.61096 | -51.67154 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3471a7c3-5eb9-389a-9183-6d8c44d46d23 | -6.79871 | -58.64749 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cb92d16-6f0b-3c17-9dbe-32e247071476 | -6.18901 | -55.43488 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2400c98e-8694-34fd-a241-8ada1da94357 | -6.67976 | -58.73479 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4cad31e8-dc69-3d23-9469-dd35a226496f | -9.45494 | -40.32688 | 2026-08-23 04:44:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2fc10de4-24fb-3a46-8dd4-4a89dfca5cac | -6.81035 | -58.64996 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cd650310-6e30-3368-89ea-1257854ad13c | -6.76854 | -58.68089 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7651aced-abc3-3f48-982b-6cb12684317f | -6.79839 | -59.6637 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61164009-cf9d-3b3a-8b52-8c1e531bb766 | -6.77885 | -42.67295 | 2026-08-23 04:44:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca8eeee5-6960-3bf7-8ce4-35e44c116509 | -7.30452 | -42.98187 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e71a7688-2c33-3439-a213-4aacdb09a895 | -7.30289 | -42.9927 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dc3160b8-e80a-30fa-9a97-61924c8fe808 | -6.79689 | -59.42807 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2279fe04-e588-32cd-8638-87aca191c0ee | -6.93609 | -59.32038 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec8affda-f4be-3c4e-b2f9-4fac71aba319 | -6.6812 | -58.73905 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| adfba12d-9ebc-3d91-b4ca-56d92de3f63c | -2.53836 | -54.01079 | 2026-08-23 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e310417c-3880-3b7c-a0f9-8a63badbb183 | -7.47044 | -45.13109 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 951ee31b-5f58-30ad-a9ab-3a3e1c449b30 | -8.03507 | -54.00582 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eae5cdd6-1375-37b0-b392-1afcf087d556 | -5.67565 | -47.48955 | 2026-08-23 04:44:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 700693fb-2f08-35a1-96b2-543bbf7f994d | -6.96456 | -59.06453 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| dcb17f81-c811-3319-9eda-d51d92b6f4b6 | -6.19806 | -53.51924 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5378d101-cc56-39af-8c9b-1f58ea3ee12e | -6.91886 | -46.41186 | 2026-08-23 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50df0e95-6b37-3dc6-bebe-cea644f0d64b | -7.75692 | -46.1828 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a595c2bb-1eee-370f-9f02-7990f2d8e4a0 | -3.87439 | -48.04854 | 2026-08-23 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab10072b-78ad-335d-899b-b98f3e4fecfd | -6.68411 | -58.74426 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| cc50d1a3-1d04-35a4-b758-62215dcab66c | -6.78143 | -59.75656 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ab3b9b2-30b6-3bc6-ba3b-e02b35695ded | -6.97487 | -59.07578 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9690cf13-abec-3c07-b611-ff7862b70d6b | -5.17772 | -44.65499 | 2026-08-23 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2abdd95-773a-3720-aaa7-0cc54bec56db | -6.96972 | -59.07012 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 10256f2d-e2be-345b-8471-6febbb346381 | -6.80549 | -59.66006 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9559aa9b-815a-3052-a490-f51741f780c3 | -6.88168 | -59.4152 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2424fdc-8fb5-3d9b-92e0-531022d5583c | -7.69169 | -50.74866 | 2026-08-23 04:44:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfebb96a-bd96-374b-a339-d79d4595aead | -5.61201 | -51.78457 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 410061f0-5359-313b-a2cf-cd2dd487d88e | -6.75398 | -58.66089 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d067cdc5-2e24-33be-94da-006bac641baa | -6.18524 | -53.51799 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7096a3cc-432a-36d1-b05f-caa221fcdb58 | -6.80505 | -58.66806 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 51cf0854-1cce-3092-80dc-7e5e5a045a08 | -6.66431 | -58.73134 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84227b51-7e6f-37bb-9f72-4a55aa90a751 | -6.88046 | -59.41596 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f99e876-a8e1-335c-bdd8-ce34045a9da5 | -7.58895 | -57.69343 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d0dae1-7f76-3d10-84c8-06e26e0a203e | -6.11582 | -59.93476 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 260d5541-5c00-3190-88c1-26e5582a812d | -8.81853 | -46.63036 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51d97441-d373-3903-89b2-5f7bc03d9cb8 | -1.98565 | -47.96588 | 2026-08-23 04:44:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a272b35b-a91c-35d8-8799-6fa488e3f67f | -6.38216 | -54.97496 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b31e70e5-865e-3b5e-a043-d0567480465f | -8.45946 | -46.98967 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
