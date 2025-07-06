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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46724930-05a5-3ea7-a459-4ad5f00b94d3 | -4.81844 | -44.35413 | 2025-07-06 04:00:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e37534b-fd0f-32b3-9fc4-05a74af66b2a | -6.00725 | -46.41159 | 2025-07-06 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73545697-7f23-3b46-b1a8-29b0dac01a69 | -3.50026 | -43.24406 | 2025-07-06 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1a01827b-1b6a-3136-9847-b9a09c7c7c17 | -8.02734 | -45.83561 | 2025-07-06 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba45186-8025-3565-b4ec-a6cfbaec4c38 | -6.68645 | -43.14751 | 2025-07-06 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 811df875-3cb4-3f06-a4de-21bb7362b431 | -7.1887 | -43.13188 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6553963b-907a-3861-a6bd-aec552d64c2d | -7.30469 | -45.36379 | 2025-07-06 04:00:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e93c8ed7-59d9-3685-afe2-2ab0dac4735a | -3.50701 | -43.24978 | 2025-07-06 04:00:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3de1f951-33a6-37f8-96f7-de97b1bbb3fc | -7.20428 | -43.12606 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 357cc471-b87b-36cf-b24c-a6dbbe71ff70 | -3.48679 | -48.44606 | 2025-07-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c1775dd-91e1-3b31-acf4-6a1ce86065cc | -8.24259 | -46.94464 | 2025-07-06 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41673a69-f0c9-378c-ab6a-ec5e77ed566d | -7.19226 | -43.13245 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 130d1418-c411-3386-a380-39aeed196700 | -7.96683 | -47.2331 | 2025-07-06 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d42ca9f7-51ce-3c33-bf43-c4ffdca803de | -6.12311 | -42.53457 | 2025-07-06 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b63fd22b-109e-38a5-bc3c-352d794eec16 | -7.01294 | -44.34445 | 2025-07-06 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e365902-24bb-3525-97cd-d99af2cea874 | -7.1965 | -43.12894 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 467ca702-90b8-3e1c-9abd-7f5cd8eb8e10 | -5.60851 | -45.17323 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e1b5c02-b713-3c50-9287-c66b1851bf5c | -7.11553 | -44.14666 | 2025-07-06 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42769d57-da73-31a3-8f12-f010d91c0671 | -7.19938 | -43.13361 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ca8d28dd-26dc-38f3-a17b-2526a957eae0 | -7.69921 | -47.28277 | 2025-07-06 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bae11a9-032f-368e-bceb-a82c27eb3e97 | -7.09969 | -44.17274 | 2025-07-06 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 958abc18-d6a2-3d48-b0c3-42d8adb3ec7b | -3.50016 | -42.33224 | 2025-07-06 04:00:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4193d4e7-ce92-3c3d-8463-9a99112a448b | -3.48291 | -48.44511 | 2025-07-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a42de0f6-f29f-3b0c-b7ff-90d97d7806b2 | -7.55827 | -49.91121 | 2025-07-06 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e5f19a7-041f-3cd3-bcbe-1be5a51a4458 | -7.0915 | -43.21754 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 091fd987-53a1-32d1-a306-e967a8039345 | -8.03011 | -45.83449 | 2025-07-06 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7eadc726-1cd8-36a4-9f6b-1d092d394933 | -4.53374 | -38.36046 | 2025-07-06 04:00:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d32c2a4b-ccd5-31bf-bf1a-582063f3570e | -3.81259 | -42.54485 | 2025-07-06 04:00:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da31619a-8456-3d4f-871b-5470eaadee9b | -8.22555 | -44.93592 | 2025-07-06 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 112fec53-09bd-3eac-8249-dd32c94de122 | -6.41711 | -41.73365 | 2025-07-06 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a15d1db0-dbf5-3b67-89ea-19f43ea3dba4 | -5.68813 | -41.40197 | 2025-07-06 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f1b820b1-b60f-3857-95af-80d914f769ef | -6.83372 | -43.30483 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4c142f6-a5b4-3d06-877f-e269d21790bb | -7.20495 | -43.12201 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 643672bb-e6f4-34ec-a560-e81d878a04e0 | -5.56897 | -45.20819 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bb48f124-f463-3ca8-9c27-919ae669e4db | -7.20361 | -43.13012 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 378eab4d-1b53-34a8-ac03-a32b69d97d40 | -6.92887 | -45.76464 | 2025-07-06 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de592489-0463-37ec-bad4-a155d74e84df | -6.33985 | -43.74921 | 2025-07-06 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 506bb587-d1bd-3dee-8271-f67118114114 | -6.03431 | -44.14292 | 2025-07-06 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b818ef9-aa14-3eba-a05f-7aa880996823 | -7.19294 | -43.12838 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 23c86386-5503-37c1-ab37-340f8d727fe9 | -5.59849 | -45.18286 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 954d1622-43b1-3bb0-8e81-e19f37948164 | -5.60442 | -45.17252 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8b00e84-849a-3dca-bc4d-9d8df7921811 | -7.08372 | -44.39007 | 2025-07-06 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| dd7af451-95b8-364a-9268-24341d183cff | -5.22923 | -46.01917 | 2025-07-06 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cb6722f-10de-3852-bc07-df7c7121d31d | -5.60137 | -45.19091 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aee90a92-8198-3da2-bf89-362c79d24bb9 | -7.25475 | -44.22168 | 2025-07-06 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aefa15fa-6c30-3262-bbb7-2579d4f64bdc | -4.4435 | -48.17531 | 2025-07-06 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7cb4f14b-0c56-3ce5-94bf-e53edecbbfb0 | -7.56372 | -49.91224 | 2025-07-06 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7717c10c-4d1e-305e-9ce2-e14af1154a7d | -5.5991 | -45.17917 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 497888b8-ac24-3ea0-8ca1-363e3bf02cb1 | -5.56711 | -45.21925 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 162f531c-d327-32a4-b196-5bead746cd30 | -7.96846 | -47.2237 | 2025-07-06 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3acd81b3-e382-3e73-b8db-7da493b0a131 | -5.60547 | -45.1916 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6aaab574-c9c3-3ad2-bdcc-cc3c03117aea | -5.60608 | -45.18793 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd02696a-d43c-331b-a4d8-c84191c3dfce | -8.23812 | -46.94415 | 2025-07-06 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7127e4e-77cd-3b7f-90fe-f2575d54626e | -5.6032 | -45.17986 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dbaafc0-2772-33b8-9d3c-1bb71d36286b | -6.85167 | -42.80087 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ee313354-1ca4-3c59-8987-0f7279c4768f | -5.60381 | -45.17619 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 160ab0e3-cc13-33f8-a098-d9605e9a5f3f | -6.93808 | -42.80557 | 2025-07-06 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0a8309bb-8af8-3dd5-8489-3a815ff01f1d | -5.59501 | -45.17849 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb0fa785-25fd-32c0-a6bc-4fef58bb042c | -6.94842 | -42.69863 | 2025-07-06 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7bfb3824-eace-383d-b000-2a6fefd2954b | -6.75792 | -44.61687 | 2025-07-06 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebd7e0c0-678a-31de-8e9f-9f05df89790a | -5.5502 | -37.31897 | 2025-07-06 04:00:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 50fd4bea-9e31-36bf-b6bb-276c46e61710 | -6.92641 | -43.05444 | 2025-07-06 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e39e57e-c464-3149-86a3-f805447ed630 | -3.48098 | -48.44818 | 2025-07-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2adca285-3ed8-38a5-a808-a2f068811bd2 | -5.60198 | -45.18723 | 2025-07-06 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c6a5c34-f723-3eea-802d-5e3891a1c87e | -4.43838 | -48.17443 | 2025-07-06 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da73513e-709b-32d8-a54a-571caed57c2d | -2.91803 | -41.39709 | 2025-07-06 04:00:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7305c538-4d19-3dca-804c-8095d16debd4 | -6.93458 | -42.80492 | 2025-07-06 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| cf2d6c15-5850-3079-955b-798a6022915e | -4.8139 | -47.31793 | 2025-07-06 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7c6643f-a512-38f2-b4c4-84ae658e77c0 | -5.19109 | -37.69624 | 2025-07-06 04:00:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd7c4d9a-03dc-3ed9-ae98-1fdffc090b28 | -3.48154 | -48.44489 | 2025-07-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02771e8c-873e-3d66-aa7b-cef9b15a3fcf | -11.97381 | -55.52346 | 2025-07-06 04:02:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d0a879b-80f5-3110-af5e-bb45ec163562 | -10.86928 | -47.18425 | 2025-07-06 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30afa30d-779e-3566-a9c2-c188f41d6b77 | -10.58208 | -49.13188 | 2025-07-06 04:02:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c70ee1a4-36b7-3678-9257-55026911a5b9 | -15.71668 | -43.49341 | 2025-07-06 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9899a955-62b3-345e-be1a-6f9fdaebc9c7 | -11.32694 | -51.45665 | 2025-07-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01fe20c7-5e27-3256-8477-13385d965ecf | -11.88702 | -44.89067 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| daa321bc-a2a9-3032-91cf-91b8f5fdf82e | -11.45102 | -45.10926 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84904590-3d50-38ed-b5ff-39d5827b2840 | -16.4273 | -42.18021 | 2025-07-06 04:02:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b97e85f1-752f-35b7-b1e8-db6c91521f38 | -11.44355 | -45.10794 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41585443-cb44-371d-87d9-f3dc7ef874c7 | -8.80916 | -45.97268 | 2025-07-06 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89547ab6-df5e-3634-ac61-28cf79425ab1 | -11.43981 | -45.10728 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24528479-a732-3564-99dd-ae73c2736a0c | -10.25273 | -48.16727 | 2025-07-06 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d05af010-114b-3e9a-be05-6f0a09990712 | -11.45632 | -45.10079 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 116d30e9-b94f-3a8f-a795-a2b67720f5e5 | -10.8786 | -47.1817 | 2025-07-06 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 592d225d-39c3-3e71-9697-3dfc1c74fb08 | -11.88569 | -44.89291 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3f956c6-9c00-3dc7-8e6b-042a6fecd115 | -9.20387 | -45.33924 | 2025-07-06 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb819683-bc1b-38e5-9529-eb85c1a049ce | -10.64862 | -44.48982 | 2025-07-06 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8645f86f-6b7e-342d-bdad-e7a485db0f4c | -11.33333 | -51.45391 | 2025-07-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45272e6f-872d-333d-9b34-a907bfcf922d | -14.24249 | -41.79658 | 2025-07-06 04:02:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 92212117-449c-3102-8ff8-92a28a7a1979 | -11.44433 | -45.10337 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c6bbc08-686b-3e5d-8747-92973881a6b8 | -10.64682 | -46.48212 | 2025-07-06 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 803596f5-b5fd-3b0e-a2f9-a2538c46f718 | -11.45554 | -45.10535 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84be34b1-61a5-3a6c-889f-945d972be357 | -11.32844 | -51.44886 | 2025-07-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feabd852-2165-3cd4-82ad-2e7c8e88b23e | -11.44276 | -45.11251 | 2025-07-06 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e3a1b3f-a4ee-334c-a90c-6a93264b1804 | -12.01315 | -47.77184 | 2025-07-06 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4fc9cf90-41a5-3d5f-9987-de486892452a | -12.05917 | -43.50635 | 2025-07-06 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2996c52-3684-372c-97a3-52d8d353e890 | -12.06325 | -43.50307 | 2025-07-06 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9478a9d7-cbc0-37c8-9d97-cbbbbea9f2d7 | -9.09076 | -47.96772 | 2025-07-06 04:02:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a8fb87b9-9cbb-3c2c-832d-969165c3c3a5 | -12.15546 | -46.58696 | 2025-07-06 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b7eb6b1-0291-3b7f-8562-17012852fbed | -12.01392 | -47.76754 | 2025-07-06 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README5.md)
