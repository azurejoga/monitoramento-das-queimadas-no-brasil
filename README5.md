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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecb29f17-239f-3f80-82fe-89f5580aa0bf | -3.0873 | -49.5271 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 293e2457-a29f-3ec7-9ce0-39f5daf8c821 | -3.3454 | -43.374001 | 2026-10-04 00:09:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81946b7d-d2da-34c4-84da-056b2fd52a71 | -3.2915 | -53.826099 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 054c8422-7b87-375e-b17a-3ec3b853860e | -3.8984 | -49.693802 | 2026-10-04 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed5c1168-69e0-3311-97aa-cde7ef2487ba | -5.5789 | -49.012001 | 2026-10-04 00:09:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b9ee60-fab9-3820-a45c-558cbd3d9d5b | -4.4643 | -50.968601 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2209fdc-0c2d-3f58-9249-3a6a8561cab1 | -3.8617 | -55.798401 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c4dd6cd-17f4-3cb6-bd25-7c9a76a5ed02 | -3.0692 | -51.270401 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02db67fe-8893-353f-af16-b68364320cdf | 1.7707 | -55.646599 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21f7573e-e226-37f0-81b9-fde139453d31 | -2.8092 | -46.7752 | 2026-10-04 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c40fb107-1c26-3006-a79c-8b56128516e1 | -2.8454 | -51.283798 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8243a7c-c6a5-394f-aacc-a64e84a366fb | -5.5417 | -49.757999 | 2026-10-04 00:09:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b32704a-7770-32d3-8399-71b412fa3582 | -5.368 | -56.041401 | 2026-10-04 00:09:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9999f990-3b2a-3298-8798-54c17ce2d077 | -5.1861 | -45.473301 | 2026-10-04 00:09:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a4cadf3-620f-3b6f-8d7a-619c5221b023 | -3.5788 | -55.305698 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b0f067f-eea1-3b8d-ac7e-b97750637652 | -5.5491 | -45.2631 | 2026-10-04 00:09:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9077617-413f-35c2-af9d-ad6a11cf4303 | -4.1076 | -49.071301 | 2026-10-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7ac1001-69ec-313e-988b-5382f8468bd3 | -4.8131 | -49.863499 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b79754a-db2c-3303-b784-0dd7cd668048 | -3.3043 | -52.9613 | 2026-10-04 00:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d386de2c-6797-3fd9-bfc6-d284a7362bb8 | -1.1609 | -49.2607 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d614d60d-de05-3b00-b9e9-0bec3feb1142 | -2.906 | -54.125801 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40536e96-c878-3965-84f2-a4c0a8dc6a15 | -2.7809 | -51.363098 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60a23034-4cd1-3874-876a-54d7feabb229 | -3.1379 | -53.7365 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acf013fa-909d-38ae-9cca-399ffab66c8f | -2.6 | -51.841 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b41da71-4c20-3a6c-baf8-c231f46afffd | -3.0775 | -49.529301 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f0c7781-f05a-3681-8d45-162dafa01b1a | -4.1175 | -49.069099 | 2026-10-04 00:09:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b20ecb33-4eff-3872-8ef5-62b3e31e45fc | -1.9297 | -54.3578 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c4a458c-8b36-3433-b6d8-d452503ee9ae | -2.8237 | -54.125599 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1caeb8d9-9d9d-3aa0-8f2a-638cd1558d86 | -1.0137 | -48.793598 | 2026-10-04 00:09:00 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a86f43e-d320-3511-888d-36624c1e3ed8 | -2.9669 | -54.076199 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcae1e1d-b2ef-3fef-a9da-ea0f1b004d3a | -3.1299 | -53.747002 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abf79c72-19ae-3dec-8691-a4b5899209f4 | -2.9314 | -54.147598 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3fa2410-386c-31f5-b4e9-f193bd6ae453 | -4.1448 | -49.689301 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03adc546-de3f-36ba-8528-d41b3b7c52dd | -2.5819 | -51.852402 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33f0b77b-aca5-372a-b19c-12cbaaa3dd07 | -2.7707 | -57.671501 | 2026-10-04 00:09:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdf1d647-671d-3092-90c4-bd1d0fb26835 | -3.1726 | -54.076599 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7db5d51b-1cc5-37b9-b663-bfde83d00308 | -7.2829 | -49.251999 | 2026-10-04 00:09:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5feb824b-e829-3bb5-9468-73af80b3e911 | -1.0897 | -54.099499 | 2026-10-04 00:09:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef6bc76-e863-3703-afd1-816a1ae5f34d | -3.0677 | -49.531502 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc31c0d7-f603-3843-85f3-ba738f9c1e35 | -4.013 | -44.817299 | 2026-10-04 00:09:00 | METOP-B | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dd83c1a7-81b1-3ea1-8cb2-a7bda988a2dd | -2.6114 | -51.205799 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fade2d1f-5dcb-3018-a89a-34de9a161447 | -4.8162 | -49.2855 | 2026-10-04 00:09:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2d0bb6-7f97-3965-ae53-1b1227ff529e | -3.3051 | -53.8409 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b40bb3e6-ffe0-3b05-8794-77af215cbcf0 | 1.7612 | -50.923698 | 2026-10-04 00:09:00 | METOP-B | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 54fde4ad-6d0e-3169-b4ec-764579d163fd | -8.0303 | -47.058201 | 2026-10-04 00:09:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2d143e4-141a-3d6d-aefb-bc9e42eed4bb | -3.3552 | -43.3717 | 2026-10-04 00:09:00 | METOP-B | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed7b719c-48c4-3781-adaf-a4adaa5e9c4d | -4.2926 | -50.251801 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8270e5cf-e869-3a3b-b846-8f69a8781308 | -2.2236 | -53.695599 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e12df52d-a925-30d2-96c9-325ae3931a40 | -3.5164 | -54.6068 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 160deea2-dfbf-39fb-9178-b2ab20043306 | -3.1108 | -53.7076 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2155e95-3e11-3497-83bc-e5a6fa85e363 | -5.5515 | -49.755798 | 2026-10-04 00:09:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fb98826-0e55-3c21-b14f-a92b0729d8a8 | -4.2698 | -50.744598 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe3b0b0-088b-3717-9f38-156e760712b4 | -3.8757 | -49.684502 | 2026-10-04 00:09:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40f52e3d-8189-3e2b-85dc-b9844623d7d8 | -3.9401 | -55.828701 | 2026-10-04 00:09:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2538fdaa-ccd3-378b-83f1-998e8357ba06 | -3.1982 | -50.745701 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58c8009c-9f61-30f5-9f7b-5c99f01853a9 | -2.9708 | -54.093498 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbf567f2-6141-30cc-8fda-f9caaf0da633 | -1.4939 | -49.4562 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81de9e26-0245-395b-85f1-518f88de2ea7 | -4.2563 | -50.776402 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b63489bc-0bc5-3fcb-b737-866f439ffe25 | -2.8043 | -54.084599 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab7e782-1154-3802-8d0e-b65ff616a69f | -2.7866 | -54.097599 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 913df688-f5dc-3f77-a180-23688454e2e0 | -3.4074 | -50.348701 | 2026-10-04 00:09:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 182a1aaf-1661-359c-bf1d-eae3ce38e30e | -2.8865 | -54.084702 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffa97d5c-f550-365f-aaa9-33bedf2db8b0 | -3.1862 | -54.091801 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a887ba8-81e1-3344-a7c3-a8a5235d0bbf | -2.8613 | -49.6213 | 2026-10-04 00:09:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d720a378-6048-32e9-8e91-d19c72a5a4dc | -3.1775 | -57.894798 | 2026-10-04 00:09:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12796ef1-e583-334f-8604-0a5411df01fa | -5.5498 | -44.216702 | 2026-10-04 00:09:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3070ea59-82c6-3adb-a1eb-b4b7bdec331e | -4.4764 | -45.522999 | 2026-10-04 00:09:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01380bdf-bb42-32f4-8476-986e6ab3d205 | -0.3612 | -52.058498 | 2026-10-04 00:09:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b200dc1d-a2b0-3a3d-8356-2383b73ed9ba | -3.2934 | -53.834599 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e58688-04d4-3654-9b1e-5316da8d977c | -2.9235 | -54.158401 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be6d23bc-97c1-3fb9-9e9d-6fd968176ade | -2.6846 | -54.423401 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27bfebd3-d3d6-3a99-8559-c6d4ab77ebab | -2.8469 | -51.2906 | 2026-10-04 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a575ca63-b05a-3524-baae-7241a4fc39d8 | -2.2157 | -53.706001 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb4eb3df-800b-3a12-a143-79fbbc76fcf6 | -2.2138 | -53.6978 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 143ddf7a-070d-3fea-9dbf-9e2c1ff99f0c | -2.9767 | -54.074001 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee2d955f-a5d5-3f8f-b810-baa8658fa05a | -3.0661 | -49.524601 | 2026-10-04 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9aeb7f-b72c-3a79-992c-5af76afcfb37 | -8.5243 | -48.906601 | 2026-10-04 00:09:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d9034255-e642-31fd-8733-19bbc944766c | -3.017 | -53.886101 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d925794-89ae-3d26-a612-f2ecc9344a39 | -3.0489 | -54.2136 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 046be073-6acb-354f-af31-17e9025d76c9 | -3.5074 | -52.9491 | 2026-10-04 00:09:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebe6287-b06f-30f9-99af-17f066884c4e | -3.7776 | -51.397202 | 2026-10-04 00:09:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1901ed2c-b6eb-34b2-bf6f-6d4fa39bfbb3 | -4.2957 | -50.265499 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 933d7332-591a-32c4-8225-8243bc6a8ae1 | -5.5402 | -49.751099 | 2026-10-04 00:09:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8ec16a7-a107-3a2e-bc8b-0acea214d1f6 | -3.5185 | -54.616199 | 2026-10-04 00:09:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1df7a2f7-a74a-3042-b12a-52c7046dd749 | -2.7617 | -56.9842 | 2026-10-04 00:09:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae8fbe1-337a-3483-b361-f4bd2547428b | -2.8962 | -54.127899 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7b7bde-75c0-3d26-addd-848c2c81251b | -4.2942 | -50.258598 | 2026-10-04 00:09:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d3b0186-7ba4-3e04-9e52-252dda7e63a8 | -1.1625 | -49.267899 | 2026-10-04 00:09:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07e62ab6-1d8d-3704-a679-6beac8e30521 | -4.5506 | -47.4907 | 2026-10-04 00:09:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a332cc9-e5dc-3a2d-9fc4-7d4beaf8e0af | 0.4163 | -51.126598 | 2026-10-04 00:09:00 | METOP-B | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7580bd4f-b20a-334f-9c83-f3653595a432 | -2.9433 | -54.108601 | 2026-10-04 00:09:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28ec7b80-b15c-3383-bc0f-0d9661a23b28 | -4.8146 | -49.278599 | 2026-10-04 00:09:00 | METOP-B | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c4d908e-b536-3ca9-9e32-ed157d33273c | -2.8122 | -54.073898 | 2026-10-04 00:09:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa5ed5b1-fe63-3cc5-81fe-cf305f2de46b | -4.1478 | -47.5327 | 2026-10-04 00:09:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edb05230-f653-34d8-902b-efcbb65da9aa | -1.8579 | -47.974998 | 2026-10-04 00:09:00 | METOP-B | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e1e2b4f-eb94-3122-95a0-109288bf3c51 | 1.7609 | -55.644402 | 2026-10-04 00:09:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 946521fa-dd20-386b-bfd6-8be181de40ec | -4.5091 | -45.884399 | 2026-10-04 00:09:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79cb19fc-7906-3f8f-8181-10255d979513 | -3.1201 | -53.749199 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff3f514c-9e26-3663-a8b5-ec70b18f9ee1 | -2.959 | -54.087002 | 2026-10-04 00:09:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a68f54d5-c547-32fb-86d2-e4265e697a88 | -9.1006 | -49.7771 | 2026-10-04 00:09:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
