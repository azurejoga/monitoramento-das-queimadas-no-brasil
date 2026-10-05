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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a1ab28a-180a-3ef6-86b1-3b4f00bbbb05 | -5.47124 | -41.23445 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 965bf6e2-5782-3ca7-a569-2aa162c6c5ad | -3.79322 | -59.37542 | 2026-10-05 17:15:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ced825ee-62b2-34d5-8cae-2dbedea78823 | -5.96108 | -55.35469 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8b91d976-4b3e-3a4b-ae1b-12682ca2dcee | -3.5041 | -54.61154 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2161a556-7daa-3d18-b463-d9ec216bde69 | -6.36986 | -55.15142 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0c1d5faa-aab8-35c9-8764-a5a9f727c291 | -8.16895 | -44.42093 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c22f168-f6c0-33c2-a0bd-067c5728a28f | -3.25734 | -54.2797 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 597c706a-19c9-33f5-8e82-a74b1d1d876d | -9.30662 | -60.89619 | 2026-10-05 17:15:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 50992b42-0534-3c03-9ca7-5f61b8cd1edd | -4.5837 | -39.87709 | 2026-10-05 17:15:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 192e079a-1d69-33af-9213-b98732dbcefa | -9.40245 | -65.90249 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7164b210-d002-368a-b692-22d0b406679a | -10.86811 | -61.41456 | 2026-10-05 17:15:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b1720bbd-1880-3b5b-8625-813df17af98d | -7.0825 | -45.51249 | 2026-10-05 17:15:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 678f458b-630f-375e-ab51-f9dfa59dccd4 | -8.73532 | -55.00439 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 70cabbff-3602-3e09-a72c-be4694372a85 | -3.47291 | -55.4317 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b624c81b-9cdc-33a5-ad12-c1d4fb01479e | -6.43564 | -55.617 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a10475da-4e27-3fcf-99d8-33717269f9d3 | -3.08916 | -54.175 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 85177630-dc81-3340-9c0f-64830b5313ab | -7.92285 | -41.09912 | 2026-10-05 17:15:00 | NPP-375 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 05666698-1782-307e-a485-cab56e88c9e5 | -3.84115 | -59.55557 | 2026-10-05 17:15:00 | NPP-375 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cdc59275-d08a-386d-bb26-2091216daf28 | -8.28483 | -49.91199 | 2026-10-05 17:15:00 | NPP-375 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8c289325-e83a-34e4-a3ea-3611f0d68fcd | -4.19108 | -59.41006 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 122bc6a4-2b49-39be-982a-e8500aeeaf40 | -8.62654 | -66.99728 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 245933fc-5709-3d38-a43b-e348331b5582 | -3.57107 | -55.41269 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 98c227a2-418f-37fd-a7a9-2610e6ee10d0 | -3.07483 | -54.17011 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c90fe1a3-0b14-33e0-b83d-d74f033b19d9 | -8.6226 | -44.9095 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 110fc774-2a0f-30f3-87f4-a0b67a20ea28 | -7.791 | -45.49321 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 54210732-6340-35cb-8d4f-6cec1e47ebe0 | -6.72811 | -44.2784 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a8b42241-46bd-37ee-80a7-78d5ce9ed224 | -3.082 | -54.17256 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24014d5f-9421-3928-b0c6-3248f796ddfc | -6.59164 | -41.57981 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 24511395-676f-31b6-8f95-d4b0ba82b2de | -8.42803 | -54.9974 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f0464c8c-a350-3381-93be-fb0e9f2b51c7 | -7.90808 | -44.1969 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| edf871a1-c496-380f-b209-b4eb25b1964c | -5.26747 | -47.91298 | 2026-10-05 17:15:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| a6673602-7a27-3e9a-9e40-0f612e72ff07 | -6.79128 | -66.6679 | 2026-10-05 17:15:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6c1c3efa-f48c-3ad1-a0a3-cfac3a0cd1df | -6.15287 | -45.71503 | 2026-10-05 17:15:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9404d3c4-d28c-3857-9608-937fe7a2b19d | -3.05943 | -54.15833 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e70fb938-6a5c-33a3-82b6-29cd8f940563 | -8.53546 | -54.59384 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 254c742c-96b7-38d8-a218-95f227fd7a91 | -5.51753 | -44.1138 | 2026-10-05 17:15:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e2e665ac-f8c0-376d-b473-b8ff4ab090b6 | -5.55309 | -45.2654 | 2026-10-05 17:15:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7a66f9b0-c396-344e-bd9b-d512dbf91c9a | -5.9556 | -41.34529 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 7346eedc-3867-382c-8705-25652c47bf90 | -6.89513 | -43.66674 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e9b5b97d-dd7d-3d87-90ef-f3b55cf5e373 | -7.61321 | -45.2953 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f8d2e0be-6645-3854-9c8b-634d80d755e2 | -3.07603 | -54.15581 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0b5c08f6-adbf-374a-b437-456579bfa002 | -8.52668 | -54.58746 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3be832e4-29d3-3dd9-b54e-c93d7bd95fe3 | -3.1923 | -54.09896 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b4a6f232-43c1-35ad-8c41-316bfa3776d2 | -5.95862 | -41.36197 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 174.8 |
| 4a5737be-5f53-3202-a900-2f36dbbbd736 | -3.47105 | -54.59534 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3ce0aac8-9ed0-3970-a03a-42fb0cf39dc5 | -6.71399 | -45.22633 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6ad9ab13-e6e6-3e7c-9e56-d12197961641 | -3.19509 | -54.095 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fcee3a32-ef5c-3095-95e4-51d31e4f7088 | -9.50645 | -46.81748 | 2026-10-05 17:15:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 49ac703c-9904-30ab-9488-f617a079fed3 | -3.11502 | -53.70685 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 962b3e68-5bf1-308f-9cab-427e2c33fd11 | -3.09599 | -53.73143 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 452e75c4-6614-3a54-a9f6-64487c0bd3e0 | -3.07589 | -54.17701 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 7689612f-bb4e-3d90-96ef-53c4a98727d4 | -9.9698 | -65.11792 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5d9c4cf0-1883-36fd-a37b-ed31a0e99ae9 | -8.1074 | -40.24019 | 2026-10-05 17:15:00 | NPP-375 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 953f4fd7-6d8a-3680-9775-96095d7ba0a4 | -4.85147 | -42.20287 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 32e3fa9e-5be3-365d-8fb5-8149f3940c62 | -9.12415 | -65.9082 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ee0b0810-f267-30c9-ba25-1e3e25ba9d28 | -4.80692 | -42.14673 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| ffc11f6e-1fc6-3261-a2a7-72e249c9593b | -3.49572 | -54.62343 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 022b1407-b337-3747-a1c6-93034ead4e80 | -6.15084 | -45.46564 | 2026-10-05 17:15:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c6d90fa2-5ca2-31c9-b456-4d878f3bfc83 | -9.39625 | -65.89539 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8ba447ad-d8f0-3d36-aafa-855bf96e734e | -6.87833 | -43.66933 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c3188f5f-de22-3f94-91e2-fa4ce7507d98 | -3.82061 | -55.61132 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 61282cad-b1d4-304c-9d98-0000fb5beb6f | -3.0958 | -54.17399 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 479cee93-21e7-3224-9471-02aa446bd6c0 | -5.68617 | -53.49422 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 727a485b-6c9f-3aad-a952-2cbc38920f33 | -3.10277 | -53.71582 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| a6bb3cd3-b382-31ba-addc-6b8ef079f1c9 | -2.68795 | -49.03641 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| f18e636b-6ba6-31a3-890a-e1fde6b11251 | -8.53939 | -54.59696 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f5414286-d5a8-3805-8f1b-dd63957584d7 | -3.35783 | -43.38543 | 2026-10-05 17:15:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 744df6c1-e318-3c83-83fc-34cfc0929c5d | -3.99602 | -56.26497 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| a896ab42-6459-369c-8724-479a17fec8ec | -8.00661 | -42.92226 | 2026-10-05 17:15:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 5e2f30ee-f487-33c7-bad2-1cc704a96c63 | -7.2236 | -55.19759 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e347a67-39a7-32ff-ae65-94b6205743a8 | -8.87318 | -67.00528 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3eb59f40-042c-3dbb-821c-f0e3e8ba9d28 | -3.28269 | -42.25982 | 2026-10-05 17:15:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a9af6bbb-ea66-3fbc-88a5-5b8da2090c30 | -4.28064 | -44.73446 | 2026-10-05 17:15:00 | NPP-375 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a872d84-b2de-3017-a7ff-61cae2e4f49d | -7.90436 | -44.1989 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abbc7736-fc5a-3315-82d7-2926856c499f | -2.86631 | -48.56527 | 2026-10-05 17:15:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60882a54-72c9-3375-9c4c-fc8619dcd90e | -6.45629 | -55.4727 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b45dae8e-1399-3479-8c05-d5db92d78c2a | -8.28119 | -49.91257 | 2026-10-05 17:15:00 | NPP-375 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 919b802c-aeb8-3b24-a905-ed851279a7bd | -8.42406 | -54.9942 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a93d6435-f2f1-3456-ab87-bffcba105cbb | -4.8673 | -43.47149 | 2026-10-05 17:15:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7bc24847-ce13-3b9d-add6-d3e91134f4af | -3.37567 | -54.10494 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bb2b12d6-a7c3-31bb-b715-dec4b1b39006 | -8.24083 | -54.65371 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c92cae4f-be87-31b7-a20d-1d2be0cf5eaa | -4.4378 | -43.42487 | 2026-10-05 17:15:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ebff8f23-305d-350c-bc10-5f8d2d17e797 | -5.12346 | -43.98998 | 2026-10-05 17:15:00 | NPP-375 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6a4cbeea-6bd8-34af-a0fc-83f810fe010f | -3.18845 | -54.09601 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 80737732-bd53-3f61-b1ee-64dccb7bf3c1 | -3.55551 | -54.48289 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0596350c-95d6-3943-8d2e-03138b19b2ef | -3.96387 | -55.47643 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d04adec9-16d3-3cb9-9379-9fd521172163 | -2.78058 | -49.45307 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d743c439-3e24-36cd-834d-ada3f69622d5 | -9.45914 | -64.32793 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7840366c-e513-3bb1-bf6c-b43b6ef96bef | -3.04847 | -53.88776 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 858b8dcc-39b3-3d5b-bab0-02bc5f6fb78e | -6.24256 | -52.84831 | 2026-10-05 17:15:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d1741864-42f8-33e8-bf8e-9638a9dce6c8 | -9.5115 | -46.82097 | 2026-10-05 17:15:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 94de2c2c-4e45-3221-b945-bea81edb551a | -4.2016 | -53.58115 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 393ecda5-cda6-35d0-9147-9ba4db1f7e98 | -9.48908 | -65.63934 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c2701c6a-7764-3ea0-8bfd-427b464b7068 | -3.27835 | -50.01771 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5c6ee87b-e755-3f57-b8ad-16488d60b243 | -5.90729 | -43.36964 | 2026-10-05 17:15:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 13c8a6a9-9158-3bc7-8008-ae751e057a68 | -3.08252 | -54.17601 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f1123b1-ca34-3bfc-88ab-a8f17152f312 | -6.34212 | -42.54703 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 5acdf47a-4c07-3039-be5c-2f2f463f1ac3 | -9.39696 | -65.90149 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2cbaf3a9-d4b4-3094-af59-5d33d4d8966f | -3.63713 | -54.50585 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 07f4fde0-c0e9-367d-b7bb-3a22c8b626b3 | -9.10991 | -64.37424 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |


[Clique aqui para ver as próximas entradas](README118.md)
