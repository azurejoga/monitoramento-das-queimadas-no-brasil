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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfa75add-c932-3a15-804d-04822ad56603 | -5.90489 | -44.76541 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24972289-8c9b-3527-ba3a-3804aa2ea01d | -6.33177 | -44.30968 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fecb2589-de62-3b65-a64f-b1f3fac63c71 | -5.63218 | -50.0288 | 2025-10-18 04:00:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12eb0b09-3e13-38a1-b9a3-2b953ac2cec9 | -5.16982 | -46.19347 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0fbca75-ae48-34d1-9f4c-ff7fd8677de4 | -2.57223 | -49.11366 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aee3847-09c5-3c75-b1d9-cc69f8213fcb | -4.96773 | -44.61415 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e934b75-ebe9-3b12-bf71-817c9473968d | -3.83326 | -47.4017 | 2025-10-18 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cbb03351-b731-30c4-a8f0-0779545b982f | -3.57534 | -49.43993 | 2025-10-18 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a603bca6-1dc8-3204-8a69-e939dfa92a15 | -4.96086 | -45.09125 | 2025-10-18 04:00:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9a7a308-7ecd-32ad-80ba-f05dfaa2e61d | -5.38508 | -40.89878 | 2025-10-18 04:00:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 561f694e-a1ab-3453-a11b-2ddffb27537c | -4.91831 | -45.4064 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2b7323ea-4f12-32df-9478-ce73d88a5731 | -6.13137 | -44.30153 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2ede6a2-f1dd-317c-b263-213524b288e3 | -6.54471 | -43.91528 | 2025-10-18 04:00:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 69cce468-31ed-3761-9f05-d5940a5e612e | -1.6175 | -46.66751 | 2025-10-18 04:00:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d84e39d1-4144-32cd-b8b3-ca9483f0acaf | -3.47388 | -50.02142 | 2025-10-18 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0cbb0b05-9e47-3d70-90fd-363f38042b7f | -5.54119 | -44.04167 | 2025-10-18 04:00:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8be9c985-2270-3bcf-8a6d-9a917b404547 | -3.79016 | -51.76328 | 2025-10-18 04:00:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c801beab-b90f-3ea3-be3c-5472c504514b | -5.01255 | -46.02568 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 049c2955-8e11-364f-a03c-f13532713eac | -4.66953 | -44.80078 | 2025-10-18 04:00:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ca9f2f-01b5-307e-b5b6-4ab6e115beb5 | -6.19859 | -41.72823 | 2025-10-18 04:00:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6867802c-4fa6-30fd-917b-49841b00aa13 | -2.56936 | -49.11417 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e257dc1c-e953-3e1f-b62d-89740fdb1902 | -5.83693 | -40.81831 | 2025-10-18 04:00:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b7d9e1e-f16e-365b-962e-795f316f0bf5 | -6.37014 | -45.76801 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85cb66c1-f3cc-3b9a-b1ab-7e995d572d97 | -6.94422 | -39.60027 | 2025-10-18 04:00:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7132af77-632e-3190-b497-ab946e316453 | -5.58372 | -44.17983 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3ae5f67-943c-3a36-be1f-805ea6daa3a8 | -5.34317 | -44.99678 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c79ec70e-cd13-3932-b9a2-c553ab6961c6 | -4.94678 | -45.6301 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c1cd194-5b4f-3c77-bc17-0b4d99bfe38e | -2.57504 | -49.11506 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dde36f7f-8056-3a9a-8fb0-d3f15e213a33 | -6.00561 | -40.22534 | 2025-10-18 04:00:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fc9953a0-42cc-30e8-b5b2-61bae8802295 | -3.85099 | -41.57751 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 05c4808f-5862-33aa-ad78-33043beab84f | -4.45314 | -43.22924 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d12ea771-e395-306a-bf87-5dbfbed8c0a7 | -6.9442 | -41.56519 | 2025-10-18 04:00:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 660caee5-b953-3764-82f7-4f93826c9e64 | -6.98189 | -39.68407 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 14353ede-6cf0-3bf7-b0ae-d6340b95fc08 | -4.44197 | -43.22749 | 2025-10-18 04:00:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72bd69cc-6404-38a5-8b63-2164eb03b2c2 | -4.87685 | -46.70613 | 2025-10-18 04:00:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb222b76-5ed3-3bd1-8309-6217dd40c26b | -7.01441 | -41.83048 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3841f967-85c1-35d3-99a1-59c65cb4c824 | -5.92408 | -45.44711 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4b64175-5cc3-3f09-aefa-107f21f33940 | -6.17374 | -44.72823 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8370f2f6-d58c-3fd5-aca6-21ba1147386d | -4.93818 | -41.54561 | 2025-10-18 04:00:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6af6e25f-d9ae-3de1-bb04-481a53b752ff | -5.38676 | -40.88817 | 2025-10-18 04:00:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 843b1665-5174-3021-87eb-f62acc947bd4 | -5.71313 | -49.09948 | 2025-10-18 04:00:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d881e6eb-f046-3451-b3f4-45a17ec61e87 | -4.53131 | -44.80145 | 2025-10-18 04:00:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59ef0464-2f0d-34fe-abc2-0e5497ab2d07 | -4.42406 | -40.17268 | 2025-10-18 04:00:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6624a1ad-6ad0-365c-88c5-c97045bca0f4 | -6.23348 | -44.15158 | 2025-10-18 04:00:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d7797905-4af7-3c77-9270-2c964eb8baf1 | -5.57984 | -44.17922 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a3dfd532-60ef-3b7b-a08f-4115e5f9f9ea | -3.85281 | -41.5661 | 2025-10-18 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9ab1668e-eda8-3075-8828-45ee142f338c | -6.98824 | -38.43486 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 55ae9d87-6846-3ce5-8397-1df632393a27 | -3.89864 | -43.03498 | 2025-10-18 04:00:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8739925f-fd0a-3c10-b8a5-755c75475ec0 | -6.5306 | -44.902 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f084d979-7a2f-38e9-8958-10cc0596cac0 | -6.24224 | -44.97065 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7848aa5-0e42-3899-bf34-3dc0e456802e | -3.49829 | -42.7282 | 2025-10-18 04:00:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 538845d5-a379-3d7b-8dd1-80c8be804b44 | -2.72226 | -48.8347 | 2025-10-18 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e8d18ff-158d-3156-ad10-d592513e716d | -4.76809 | -40.863 | 2025-10-18 04:00:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 26c30360-5d71-3197-9227-5f8f26d824fe | -2.15592 | -51.96157 | 2025-10-18 04:00:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db6f454f-48e0-3e4e-b618-8becf1a60afe | -7.03858 | -41.83833 | 2025-10-18 04:00:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 862387b7-6e34-394c-97dd-a7efb7e186a0 | -5.20701 | -46.18997 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8827159-1310-3074-8970-4dae4afcffba | -4.91416 | -45.4067 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 23f45c4a-7c31-3f55-a54d-f27cf43e0686 | -6.35867 | -45.7582 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef40d804-848b-36fb-8446-8f8ccd1e98b6 | -5.21508 | -45.24185 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18b2cdf5-9e0f-3dd3-ac1b-7e576a7de2f6 | -3.49822 | -42.72761 | 2025-10-18 04:00:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3772227c-1c21-35fc-8564-c98acaad9161 | -3.74873 | -39.27295 | 2025-10-18 04:00:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 45e10523-72dc-390d-9b71-6879f9eb7f2a | -6.05429 | -44.52376 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0604d8ae-1478-3f12-9995-ecb3b35224ea | -2.57061 | -49.10642 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12c6e4ff-2e22-3b97-b26e-fc914a0a5fa0 | -6.97084 | -39.66819 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5175d220-b743-3e89-b7be-7b2a8d38db17 | -4.00547 | -49.02231 | 2025-10-18 04:00:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 76bb9450-bf47-358d-8812-061d2851d480 | -5.29402 | -47.93523 | 2025-10-18 04:00:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ec8811d5-89a0-364e-a19f-1705aa8d02a8 | -4.83687 | -48.07876 | 2025-10-18 04:00:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 378482ab-31d4-3815-a6aa-9c3f78f54583 | -5.30563 | -44.84544 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bb773109-3281-32c0-aa74-1ff456165cf3 | -5.89257 | -43.9115 | 2025-10-18 04:00:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc9dcad4-f561-3e5d-ab16-fe398123032f | -2.56656 | -49.11274 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52d1d326-7d5b-3062-a3b7-6673d0a94a3c | -4.93595 | -41.53762 | 2025-10-18 04:00:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c219552e-f44e-3c90-a45d-fb9b8c01a99b | -5.92206 | -44.76111 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c840aded-f420-31ed-be50-0251c477babe | -3.14726 | -50.25896 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 438693a5-e781-3218-86c8-49bbcb510eb6 | -5.37797 | -46.00314 | 2025-10-18 04:00:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 39a5af17-8fa7-3b26-a4ab-4e662c68096a | -3.68481 | -45.63596 | 2025-10-18 04:00:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abb67409-3da8-37ba-870d-db3a7ef7a338 | -3.25119 | -45.9663 | 2025-10-18 04:00:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc959e94-5394-3f58-9241-d9fab5b42b19 | -3.14278 | -50.24888 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3aaa1c64-8307-388b-b508-28e7941fa486 | -5.12913 | -45.12993 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 941d0b6d-3e15-3931-948a-37f779a8dd3e | -5.56029 | -44.14404 | 2025-10-18 04:00:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2a77af7-5437-333b-84b8-de1d72bf69eb | -3.47307 | -50.02604 | 2025-10-18 04:00:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31309039-a738-34fa-a900-6171207fc021 | -5.8917 | -44.70887 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d53e2a7-1ddf-3fce-b20e-93800f2fba9f | -6.56475 | -44.43319 | 2025-10-18 04:00:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f61ad1d9-d057-3d68-9582-61ab006fd11b | -5.30173 | -45.47889 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1789594-e223-364f-baf5-69f4d8f4ce10 | -2.57629 | -49.10731 | 2025-10-18 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c96429e9-5a0d-34c5-a24c-2deff6005369 | -5.17056 | -46.18899 | 2025-10-18 04:00:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a36d2016-1c0e-3173-aca5-883fc5dfc087 | -5.98693 | -39.52002 | 2025-10-18 04:00:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d1f4365-91bd-3b58-86b2-8ab6744c09f1 | -6.4717 | -39.72385 | 2025-10-18 04:00:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b64ed41a-1b31-3fe3-8f0c-817a9b43fa6a | -6.24282 | -44.96716 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b91bc5e3-6ead-3938-9ddd-862cb4e3660b | -5.63588 | -50.03265 | 2025-10-18 04:00:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4250ece-62d2-36ec-b273-1c143c50eb96 | -6.1652 | -44.33812 | 2025-10-18 04:00:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb3d55be-99a1-3da4-922d-46c3e8741222 | -4.93682 | -49.76324 | 2025-10-18 04:00:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21af752d-72b2-35b5-9d11-c84acbf3a353 | -6.36654 | -45.76336 | 2025-10-18 04:00:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29de0f34-18fc-3f20-81a3-81e7de237fd6 | -2.87807 | -50.72762 | 2025-10-18 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73b12b1f-c5ac-3133-ad45-436faff71f56 | -4.94107 | -49.76036 | 2025-10-18 04:00:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4111af88-443d-3dcc-9f02-a9f0fcd1268c | -6.96754 | -39.66771 | 2025-10-18 04:00:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0644477-f826-3565-8e4c-a2962e010d01 | -3.24667 | -45.96551 | 2025-10-18 04:00:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6820aa13-72b3-3d28-a561-443203f636ce | -6.52773 | -41.48789 | 2025-10-18 04:00:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b1eb673c-7dbd-3d21-a546-703dc8576d4b | -3.57309 | -49.44078 | 2025-10-18 04:00:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| da19e514-0a9b-3a47-9a80-d3648bbf7301 | -5.16606 | -45.21776 | 2025-10-18 04:00:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa3d32e4-b3c1-3e51-8955-202ccfc7236b | -5.88029 | -44.83778 | 2025-10-18 04:00:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README15.md)
