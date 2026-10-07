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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cad08f4-b579-39f7-8c50-150ee674a9b2 | -11.1988 | -49.4297 | 2026-10-07 14:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ef741271-4dcd-3c8f-bbb3-32951fc544a1 | -1.4752 | -54.7958 | 2026-10-07 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0b191e07-f919-312a-84ed-51f62df21b0e | -7.1814 | -55.1036 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 315d248a-4720-37b5-bd81-c48478349f25 | -8.7293 | -70.786 | 2026-10-07 14:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 5d2a622b-48a3-30b0-a4ba-1a2194b81dcd | -11.0863 | -45.6688 | 2026-10-07 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 51551a30-4dca-3fdc-bf67-2c42371885a2 | -8.8891 | -66.7445 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| aff6079d-ddca-3e75-8fba-f325ae0120f3 | -9.9175 | -65.0313 | 2026-10-07 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 29c24a45-0396-3d8a-bcd6-5497d9e27a8c | -1.4569 | -54.796 | 2026-10-07 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 349c0929-a5bd-3a18-92cb-fa2acfa4b367 | -2.1361 | -54.4471 | 2026-10-07 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 863b4ba7-fbad-3ba1-ad6e-138d3c7f87c5 | -12.2132 | -44.6991 | 2026-10-07 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 1ec356ef-6624-3c48-b63d-457bf45f81df | -11.3745 | -46.6948 | 2026-10-07 14:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 93907fdb-9bbd-31a7-a66a-d36776cd0f27 | -12.214 | -44.6524 | 2026-10-07 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 9066fb18-5dff-3179-8496-85a6c20c68df | -9.0058 | -65.4373 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b015f3a5-61de-37e5-95b2-422ab6b63599 | -5.7321 | -41.6349 | 2026-10-07 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 146.4 |
| 7ae01c51-095c-3cc7-b5b0-ac9b66589376 | -7.2 | -55.1026 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 442.0 |
| b5f6bf75-0390-3e46-b6e7-2a67e6bc9e9c | -10.9762 | -45.4094 | 2026-10-07 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| cc319d22-ef55-3930-bed7-7aa899c57586 | -4.3283 | -43.8263 | 2026-10-07 14:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| eed9a78e-e0b9-30a4-b0e6-8bd62b2ffe4f | -9.0244 | -65.4181 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c39e4b18-6399-3d62-9e52-abac5e60e818 | -9.9175 | -65.0313 | 2026-10-07 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 73f45660-3cac-3d30-9f00-48e7b2040ce6 | -10.5097 | -47.2733 | 2026-10-07 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 5ce8359e-873a-37c5-a192-4369e6a8a601 | -11.0935 | -47.6019 | 2026-10-07 15:00:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 25068ed8-24b0-32a3-a9fa-086396d592ff | -6.4568 | -55.4609 | 2026-10-07 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4050f350-83d6-3e01-ada0-7a585fe8693e | -9.0244 | -65.4181 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fb38c932-c24c-3e29-9111-0efdb378092d | -11.065 | -45.8084 | 2026-10-07 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 5cc0aec4-0d6b-39c8-9bdf-71f7d38ed22e | -9.1356 | -65.4145 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| d39e2c8e-2bc7-3106-ad6f-4e7f4a8bc6eb | -11.8315 | -43.5391 | 2026-10-07 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.0 |
| addf17da-77c3-329c-867a-94c645ee938c | -8.339 | -72.6194 | 2026-10-07 15:00:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 13a22198-562e-3f95-90d4-82035da682ab | -11.3745 | -46.6948 | 2026-10-07 15:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 60b71f94-6a53-3271-80ce-1f3a8500e327 | -12.1746 | -44.7051 | 2026-10-07 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 57d3c970-e88c-3751-b367-facdc8fec6ea | -1.4662 | -49.4625 | 2026-10-07 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 7b6f4c79-3794-3194-a4c4-a28e487d0a91 | -9.0046 | -65.6988 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| de9a8abd-b49f-3dc9-9563-53104772b1d9 | -11.7947 | -46.683 | 2026-10-07 15:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c37f2d4f-af61-3087-b520-cc4bcf3b2b27 | -3.0375 | -53.9066 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 5901c0b8-e605-3c30-871b-4d4d64232b13 | -1.7124 | -55.4283 | 2026-10-07 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 35cd9ece-bb33-3723-8cbf-74d3ce11da54 | -7.1813 | -55.1237 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b158fd6d-ade1-3d42-8037-e9ec91343301 | -3.2576 | -54.0418 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 77ac673a-42b2-36c6-85b5-388de5b20a25 | -9.1363 | -65.2835 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9cc981a7-bae8-3dd7-8fe2-a2ba3c56ca18 | -9.1174 | -65.359 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a7456200-0de2-356d-af0b-cab969de392d | -2.9819 | -54.0488 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 790da46d-57eb-3f61-94e2-5bdd36b5db7c | -3.0559 | -53.9062 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 484eed64-ddd1-3390-8b61-f100aae83043 | -6.3665 | -55.1461 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b0e503a8-5612-3852-a983-d13c5473cd89 | -2.9979 | -54.7692 | 2026-10-07 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| aa98efb4-ce8a-33b3-a0a7-04ad422a8d25 | -9.006 | -65.4 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5801ed94-1f01-3bdb-9f40-becebf8fb890 | -9.5313 | -46.8513 | 2026-10-07 15:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| dfb1e05f-b14f-35e4-9dfe-234f8253b074 | -7.7653 | -48.2334 | 2026-10-07 15:00:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 323446e8-5241-363a-97bd-b92291112a0c | -2.9271 | -53.9295 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c6f8dee6-eabb-3e04-a862-fb3e51182e16 | -12.214 | -44.6524 | 2026-10-07 15:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 04d90fae-742a-3673-8ac6-6272dd451fd6 | -9.0282 | -69.4217 | 2026-10-07 15:00:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 5ecb5840-2f9e-3a5e-8364-2faafaff6347 | -3.0548 | -54.2076 | 2026-10-07 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 25172390-8b83-3ff1-9324-e57a096471e4 | -9.3394 | -65.4638 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5e120d72-cd1c-362f-8f4a-4eb1ade12050 | -8.2621 | -54.717 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 66cf2103-9ef8-368e-9b67-50c62655bff3 | -11.2337 | -44.8446 | 2026-10-07 15:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 9e2c8a83-7857-3483-a604-dda84355c315 | -0.3952 | -52.0152 | 2026-10-07 15:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9ad693bf-a08e-30d9-b1c6-1a6a1ce1e67b | -6.217 | -52.6851 | 2026-10-07 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 11e2973f-f889-3cad-80dd-d9d301c4e843 | 1.7121 | -55.6261 | 2026-10-07 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| e634d19c-56be-365e-b5fd-e3c936e2a549 | -3.0184 | -54.1282 | 2026-10-07 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 06e7a339-1a08-370d-9121-05ef1a8f928d | -12.2136 | -44.6758 | 2026-10-07 15:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 966c4aee-d796-3c87-b040-7ec5ba3c6d62 | -9.1542 | -65.4138 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9b2f256f-71ed-38ba-b742-a7611a86d901 | -1.4301 | -49.0382 | 2026-10-07 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| a7f777d1-e0e6-3146-8126-cfca89e0df1c | -6.1041 | -55.7162 | 2026-10-07 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 229858de-0192-35ad-8b74-3ada2124ba14 | -6.3283 | -55.3276 | 2026-10-07 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f3414a2e-0968-3dca-9b0f-951634c4444d | -12.2132 | -44.6991 | 2026-10-07 15:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| c12a1dd9-563e-35fb-83db-5b658eecc532 | -7.3846 | -55.2124 | 2026-10-07 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| bac8c214-86de-39b4-9576-aefa069b6d5c | -10.8588 | -50.6906 | 2026-10-07 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| aa056eab-86cd-3d8b-8276-386779a20dc2 | -11.6374 | -43.664 | 2026-10-07 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| f2e5ec22-57f6-3b73-bb63-d00776e3bf15 | -6.1217 | -53.0584 | 2026-10-07 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| b600ef39-cddf-3d60-a246-d6169192a4cb | -2.9451 | -54.0698 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5f599210-ed4d-31d9-9a7b-2f1509078dfa | 1.6385 | -55.8047 | 2026-10-07 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| b0ccc964-c517-32f7-aee1-a8056dda0087 | -7.8789 | -72.3492 | 2026-10-07 15:00:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 93.1 |
| b2c01da2-655d-33a8-90b5-bf5cf98a7e6a | -7.89 | -54.7206 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| ef4afd65-951c-3882-a972-42844911adfa | -7.1814 | -55.1036 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4fff4cf7-0e76-3b6d-9b73-0b7d4a84508b | -11.1051 | -45.689 | 2026-10-07 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 5806203e-15cb-37b7-bcbf-b82354c1a2a0 | -3.2214 | -53.8818 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3eb63db9-b739-3102-892d-8030095813ec | -6.0076 | -53.4919 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e8ed5093-9220-3f10-8902-54445d196b2b | -6.1974 | -52.8295 | 2026-10-07 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 8df6677f-5d4c-3bbf-9d05-442abf6a9b34 | 1.7671 | -55.5859 | 2026-10-07 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ad3f011e-011f-3718-9cce-a55fa98840e0 | -9.0859 | -61.1437 | 2026-10-07 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 679d6f17-8a14-3f69-93bb-adf749217bda | -6.0075 | -53.5122 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| ed507a72-ecb2-358b-b617-48d887fbed14 | 1.6385 | -55.785 | 2026-10-07 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0f9478d7-aabc-3ba4-958a-77f59cd38c4b | -3.0375 | -53.8865 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ab6c249e-db3f-3c63-b922-ea2ecc630bc6 | 1.7671 | -55.5661 | 2026-10-07 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 07e8ad32-30cc-3908-9baa-ab17f852c65f | -3.0001 | -54.1086 | 2026-10-07 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 0f907a2f-f8b1-3601-993e-a3d437bf08b6 | -1.4752 | -54.7759 | 2026-10-07 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 225.1 |
| b7587f83-0d69-38f0-a83e-05db1bbcb36d | -8.8364 | -62.4321 | 2026-10-07 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f4d78689-da77-353c-9bbf-8453c3f754ed | -2.9817 | -54.1091 | 2026-10-07 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f195ff05-90eb-3128-a4be-30adca41e376 | -8.6291 | -67.0482 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4b1f8bfd-9f2e-324d-abb8-61268cdece79 | -6.2161 | -52.808 | 2026-10-07 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 601dca71-4b12-34c4-956a-92e1221b3fde | -8.7866 | -47.5713 | 2026-10-07 15:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| c1ec4a04-5bec-3a28-abef-71c99f373938 | -3.0558 | -53.9263 | 2026-10-07 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8fb669ba-2a6e-3a29-a805-65aaa7c44611 | -5.7319 | -41.6589 | 2026-10-07 15:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 205.4 |
| 9ded6f0c-5839-37c9-8beb-ddcc6b773989 | -6.2162 | -52.7876 | 2026-10-07 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| db9613e1-02d5-3e36-af79-794372a2ee45 | -0.4136 | -52.0151 | 2026-10-07 15:00:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9f2f22fe-3622-3941-9ece-90d709e463f3 | -8.9874 | -65.4192 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0315a813-c8c6-356b-ade0-d5626671913f | -5.7315 | -41.7069 | 2026-10-07 15:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 167.8 |
| 868ec8bd-d411-34ca-b0c0-b55a71721b5b | -6.0448 | -53.4697 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5a92e3a0-03ef-3b3d-8b69-558184d8aaa4 | 3.1098 | -60.5943 | 2026-10-07 15:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3b67c10c-12ed-31bf-9c83-d353d02c6570 | -9.4317 | -45.8519 | 2026-10-07 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 933d2a41-724d-3081-bda5-1be685615d88 | -1.4569 | -54.7761 | 2026-10-07 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 164.8 |
| 248156e4-e49a-317f-83d1-332cb84486a2 | -6.0447 | -53.49 | 2026-10-07 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 16ee3ca7-6857-305d-95c1-6603d6a698a3 | -9.0058 | -65.4373 | 2026-10-07 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |


[Clique aqui para ver as próximas entradas](README137.md)
