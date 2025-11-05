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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f096408-a310-3451-a188-d42e903d68e1 | -5.5112 | -41.1464 | 2025-11-05 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 141.1 |
| e169e459-a943-3aff-b4bb-3e764f232591 | -12.8534 | -43.4653 | 2025-11-05 14:30:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 62b1bbab-8ba0-3c17-a9f9-3be30977408b | -3.5833 | -43.6108 | 2025-11-05 14:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1de42c50-f9ec-3058-919b-268c31f4a571 | -10.2554 | -44.0506 | 2025-11-05 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 042e277b-7bec-3632-8db5-52f19540a90e | -3.6603 | -43.1891 | 2025-11-05 14:30:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c97050dc-6242-30a8-afb2-76059717128a | -3.1767 | -42.9079 | 2025-11-05 14:30:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 3ebf9ec3-4b2f-342a-a22e-df1edf8acd87 | -5.9229 | -41.354 | 2025-11-05 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| c8de149e-fa2c-3bf6-ad41-41c19e0330d3 | -10.285 | -44.581 | 2025-11-05 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| be112ba0-e999-3b80-a89a-726e1e3af885 | -6.1271 | -41.6253 | 2025-11-05 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| b896d13a-378d-3073-b5db-6f3375597a25 | -3.4729 | -43.3377 | 2025-11-05 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 9f1cdbf4-0e1a-332f-a153-39d4bdd812bc | -6.701 | -40.8206 | 2025-11-05 14:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 563bb856-9a85-3666-bdca-cd22d71ccc9b | -6.0461 | -44.1484 | 2025-11-05 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 83db08ad-3382-3b1e-9fa4-0a82a5fa380e | -3.6986 | -43.0238 | 2025-11-05 14:30:00 | GOES-19 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c5c35a6b-926c-3b49-8a75-5519761a55a5 | -3.5085 | -43.6374 | 2025-11-05 14:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| b703388b-8076-3e1f-8fc8-51463536fdc5 | -5.4155 | -43.4552 | 2025-11-05 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| a4706e3c-a250-3c0e-80df-fb5bc7d5786b | -6.1281 | -41.529 | 2025-11-05 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 0fb3899b-0faf-3f5a-ab6d-a6878bf226f6 | -3.7359 | -43.0453 | 2025-11-05 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| dd267057-4cdd-3ca3-a280-84dbd067f615 | -3.1745 | -43.3277 | 2025-11-05 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 0edd1a63-c22f-39c5-a689-54c799af71f3 | -3.1763 | -42.978 | 2025-11-05 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ee1c98a2-275b-37b9-aa00-c7ee12b11971 | -19.0519 | -57.5356 | 2025-11-05 14:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 145.5 |
| 630fff99-ade4-3ccd-8e49-05bcdc41875a | -3.9469 | -42.1631 | 2025-11-05 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 673e2c76-ac6d-331e-a1dc-30ad199570b6 | -3.3423 | -43.3436 | 2025-11-05 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6c6cc070-a5f1-320a-976e-4cc1aebaa1a7 | -3.2299 | -43.4414 | 2025-11-05 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e7848598-efec-3dd5-9663-988cd8eaa484 | -3.6261 | -42.6524 | 2025-11-05 14:40:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2058baf4-6d0c-32cc-8ed0-815313a86edc | -5.7966 | -40.8068 | 2025-11-05 14:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 154.4 |
| c4b37970-51db-37da-86d2-ee38db785578 | -2.9344 | -42.8477 | 2025-11-05 14:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 74735ee1-f699-3750-869a-2074e0f936d2 | -3.5833 | -43.6108 | 2025-11-05 14:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 456bd838-1c10-3176-8792-9791983e241a | -5.9229 | -41.354 | 2025-11-05 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 26ee8a37-10ee-38f2-8c3e-80a3d0cb99f5 | -3.4729 | -43.3377 | 2025-11-05 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f39681b8-458a-3a86-8cd3-c3387f569945 | -3.7359 | -43.0453 | 2025-11-05 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5990e1b1-e60e-3958-ab0c-a9de96d5632f | -11.0216 | -49.8814 | 2025-11-05 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| bf2bcfd2-6a55-381f-8878-d2911cae67d5 | -9.8821 | -44.8402 | 2025-11-05 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| b38ce415-3664-31a3-a0dd-5eb233e6b9bf | -4.3872 | -43.406 | 2025-11-05 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 03c99139-8264-3468-909f-e63be507f3be | -3.6986 | -43.0238 | 2025-11-05 14:40:00 | GOES-19 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 8fbc4826-a570-36ea-95cc-08f19fbb2e5e | -10.285 | -44.581 | 2025-11-05 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| e8ea2456-919b-33b1-aa4e-dacffb2321f4 | -5.475 | -43.0774 | 2025-11-05 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9117ca21-496d-3e01-a32b-e791309ba01f | -5.4155 | -43.4552 | 2025-11-05 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 73e9189b-4e16-335a-9b09-c6f32592b48f | -19.0519 | -57.5356 | 2025-11-05 14:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 158.3 |
| b0d7933b-4740-3dc1-8d6b-86c56e99e0bc | -3.0078 | -43.1018 | 2025-11-05 14:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 94a4c470-0df1-3c0e-ac92-6854283c2c4d | -3.6603 | -43.1891 | 2025-11-05 14:40:00 | GOES-19 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 8a2c1f43-f398-39ea-bd12-87dc0aeb3555 | -3.1763 | -42.978 | 2025-11-05 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| bec2fd63-ee12-3d8e-85aa-cbfc739d6889 | -3.9219 | -43.1525 | 2025-11-05 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| eef65d29-6e60-3b78-8cd2-b2cba48d9c79 | -3.1956 | -42.8602 | 2025-11-05 14:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0fc33b4c-374f-341a-b880-93156b08b157 | -3.1952 | -42.9305 | 2025-11-05 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 51efafd0-be7e-32b7-bf3c-f1575934e20f | -5.5112 | -41.1464 | 2025-11-05 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 185.8 |
| 8ef9bb52-7068-362e-9a83-776e63b26ef4 | -5.9234 | -41.3056 | 2025-11-05 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 153.8 |
| 893c878e-6f49-3681-a058-651abd66d945 | 3.7153 | -59.7641 | 2025-11-05 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 23a0d15d-56df-3c9d-9d21-5df23e53678c | -3.3319 | -53.8385 | 2025-11-05 14:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8cb72ee9-dbb2-305d-9e4e-34fcfa108de1 | -3.8856 | -42.9909 | 2025-11-05 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 546edec6-1b1b-3b83-9df4-01c6d38454d2 | -3.0265 | -43.1011 | 2025-11-05 14:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| ee92a017-6fff-3b59-bc99-b8798f3aade7 | -5.9231 | -41.3298 | 2025-11-05 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 138.9 |
| 2f02d6c2-23ed-32a0-b75a-3a8d61ac2463 | -4.0949 | -42.4152 | 2025-11-05 14:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 15c17744-a446-39a7-afd5-883e3ea93024 | -11.5908 | -44.1177 | 2025-11-05 14:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 97b17ae9-8da3-3c51-9b25-fef765c81493 | -5.7777 | -40.8084 | 2025-11-05 14:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 128.9 |
| b2abb81b-4783-3a64-b7f0-c185bad87d4b | -19.0323 | -57.5174 | 2025-11-05 14:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 144.7 |
| 6ba1bd58-73cc-365d-a50e-fa4b76001cbe | -3.8885 | -42.5211 | 2025-11-05 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |


