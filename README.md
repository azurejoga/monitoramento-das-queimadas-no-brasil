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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddb98e05-b25a-34ee-95ae-7829606060e0 | -10.5776 | -49.1316 | 2025-07-07 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 6a7b8ffb-0136-3ce4-ac6e-0421019b20c1 | -18.3578 | -49.6803 | 2025-07-07 00:00:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 43.2 |
| 1c20542f-939c-316b-bdb9-86b5b5fdf7d5 | -18.3779 | -49.6765 | 2025-07-07 00:00:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 46.3 |
| 62b94ff6-44c7-36d6-8823-304ec2f18e3c | -7.7126 | -44.5762 | 2025-07-07 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 21e663ee-2996-33a9-969d-fb2c54de37fe | -10.5776 | -49.1316 | 2025-07-07 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 38bb0122-d985-3ce0-bcfb-2ee83dc0a16e | -7.6938 | -44.578 | 2025-07-07 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.6 |
| cf7d0633-5de9-38c3-939b-f6a30cc2c368 | -6.1606 | -48.0507 | 2025-07-07 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f6452837-99b8-3dc3-8d81-a8233dadfb6e | -7.7126 | -44.5762 | 2025-07-07 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| a3983e7b-7cdd-3b2c-b6a2-31d3bc5a1776 | -7.694 | -44.555 | 2025-07-07 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 5cdf424f-3934-342a-ba8f-cbaec97f0496 | -6.1792 | -48.0494 | 2025-07-07 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e0f04d4d-f6f7-3795-a9e9-a9ddeb462806 | -6.1606 | -48.0507 | 2025-07-07 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 27bcd853-7215-3451-ba16-a3c9eab5f55b | -7.7126 | -44.5762 | 2025-07-07 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| bb2e7879-8521-3e80-8bd6-178ada04fd3c | -6.1791 | -48.0712 | 2025-07-07 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 6e29ea17-1a58-33ce-8430-4491c5f370c1 | -6.1792 | -48.0494 | 2025-07-07 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 68922d58-e219-3db0-95ac-9a200e1d2e08 | -7.6938 | -44.578 | 2025-07-07 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.8 |
| f77a1e5b-4537-350b-9cd5-5ba6ea1cd452 | -6.1604 | -48.0724 | 2025-07-07 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 53372b56-52d8-31f6-80a6-839c9a3653c8 | -12.75456 | -44.41898 | 2025-07-07 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 0f2b7112-4be8-3906-80df-72ca0973a37f | -14.12272 | -51.29504 | 2025-07-07 00:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4c8dc13d-8ccb-3571-a5ca-d4149413e19f | -13.43077 | -47.87781 | 2025-07-07 00:22:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f13ff89c-183a-3a8b-986a-7766d9d587fa | -13.01939 | -46.77738 | 2025-07-07 00:22:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 18c41ac8-c202-3dca-bec1-2f311f4ceb3a | -15.59365 | -41.81211 | 2025-07-07 00:22:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 38a093b4-0e93-36b4-b3a0-06000307e590 | -12.75331 | -44.40992 | 2025-07-07 00:22:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| d5a4c042-5094-3474-b901-fe7756539d98 | -14.62956 | -48.14168 | 2025-07-07 00:22:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3f89a5ff-2174-35b9-ad2f-8c5ba60cff6e | -16.32736 | -43.62049 | 2025-07-07 00:22:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 223e2e4a-faf3-368f-bbc0-e5883f3162f2 | -13.42015 | -47.87925 | 2025-07-07 00:22:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4a9521e5-6f41-39be-ad99-4d28d8ceed7d | -13.01791 | -46.76565 | 2025-07-07 00:22:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9556cb90-af1d-3449-aaf8-6d6f152aa299 | -8.72982 | -46.49659 | 2025-07-07 00:24:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9cbba8a5-fb45-36cc-a889-3eb55aa69eea | -7.69336 | -44.58376 | 2025-07-07 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 590da256-182a-3ccc-9549-eec0e182f906 | -7.70097 | -44.5736 | 2025-07-07 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 9705c756-fea4-32b8-8299-f0c2e54a2590 | -6.71356 | -47.80568 | 2025-07-07 00:24:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 9c8311fe-5708-3e1c-8f00-6877cec3f4ad | -11.8795 | -44.88472 | 2025-07-07 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0c13dc88-d832-37e8-a4ad-673458b2bf7f | -9.19774 | -45.33919 | 2025-07-07 00:24:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8fad88a3-def4-32f6-8618-0bb285da670a | -6.77147 | -45.56813 | 2025-07-07 00:24:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4a93195-b43a-32c9-98f8-19ac3f83813c | -8.05887 | -43.1242 | 2025-07-07 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| b80e2434-49d9-3e98-82d3-9d52a00a88f3 | -11.33441 | -51.44393 | 2025-07-07 00:24:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| f7e04ccf-8a09-341a-8dd1-360466113733 | -12.07407 | -43.49747 | 2025-07-07 00:24:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fd91e6aa-6333-3e95-ac4f-73cf9389bb69 | -9.45264 | -43.20471 | 2025-07-07 00:24:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3d470c0a-cbb8-3058-8fed-2cc0dca38552 | -9.59958 | -40.34552 | 2025-07-07 00:24:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 26440847-866a-345c-b83c-6ddaa6fbd742 | -8.0575 | -43.11453 | 2025-07-07 00:24:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| e6505add-2840-3a1d-815f-6de5684f64bb | -6.68964 | -43.14722 | 2025-07-07 00:24:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 95d22e6c-cb12-3479-836d-8f8e6e52b172 | -9.04556 | -44.36953 | 2025-07-07 00:24:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d132455a-140e-32d0-878a-e1ec9b4573a7 | -7.70221 | -44.58249 | 2025-07-07 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 1fdabc96-4d66-364f-a225-0fd5e701ee7d | -10.57464 | -49.13578 | 2025-07-07 00:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 28ab4a93-4b09-378b-ac4a-8d1a04429413 | -9.6051 | -40.35273 | 2025-07-07 00:24:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 690b7843-dd4d-3435-9c4f-a5274b0f39fc | -12.0652 | -43.49875 | 2025-07-07 00:24:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0b4b17db-ee37-3f77-9c7d-281f49a77172 | -7.69212 | -44.57487 | 2025-07-07 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d6d536c9-42e1-38ab-8498-deb7442d8efd | -7.70982 | -44.57233 | 2025-07-07 00:24:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2953acf1-881b-3dbf-90f3-2407079e89b2 | -10.58396 | -49.11932 | 2025-07-07 00:24:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d9487423-baba-33c1-be98-2289a0e538c1 | -9.60159 | -40.35896 | 2025-07-07 00:24:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 1ec0bcaf-c2e4-3542-adc4-793d395b9726 | -8.61378 | -41.92449 | 2025-07-07 00:24:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2a2ccdab-e97f-3e4f-9180-e4ffffe1fd7d | -11.88075 | -44.89388 | 2025-07-07 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 07e0e942-db1a-3f8b-a103-f2b6f0703ce5 | -7.83111 | -44.1867 | 2025-07-07 00:24:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 476f9bb9-2102-3eb0-be97-139fde91fd0a | -9.45131 | -43.19533 | 2025-07-07 00:24:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1ea36496-9763-36d9-87b8-e93220218d61 | -7.62657 | -45.36538 | 2025-07-07 00:24:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 624b4969-2e5b-3de2-b656-07d9b1047750 | -5.60028 | -45.17402 | 2025-07-07 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc5a45d5-a7dc-3756-a484-4ade0d44f40d | -4.25079 | -48.20679 | 2025-07-07 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 34c16496-7ae9-312c-93d3-765239240644 | -4.28161 | -48.18624 | 2025-07-07 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 2cae6d3d-783b-34d9-935d-f50888bd9b2e | -6.17187 | -48.05332 | 2025-07-07 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 46e586bd-de0f-323b-9893-3f98c45a29cb | -5.57108 | -45.2232 | 2025-07-07 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1f76f2bb-e3aa-339b-88d4-cb366d0755d6 | -6.16217 | -48.0546 | 2025-07-07 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 12d73795-2aca-3e37-aba4-1e0d05ca799a | -4.83152 | -45.20586 | 2025-07-07 00:24:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6857ae52-688a-3111-a926-cf2464928e4a | -4.283 | -48.19661 | 2025-07-07 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 023e66fd-0ae7-362b-a834-a5eae71048e2 | -6.16364 | -48.06544 | 2025-07-07 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 43623417-d41c-3392-94f1-49967be6d415 | -4.82145 | -45.19828 | 2025-07-07 00:24:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 136bb951-e656-3e11-baef-50231e8a8b26 | -2.91013 | -48.24833 | 2025-07-07 00:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cd49f50b-0b86-3992-8779-6ab4a853716f | -4.82268 | -45.2071 | 2025-07-07 00:24:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8aa05334-3bde-3055-a6dc-a3db44422a08 | -3.92994 | -43.17116 | 2025-07-07 00:24:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2c2f6ada-59ed-33d7-b4c9-3208a5ea27c1 | -6.17331 | -48.06393 | 2025-07-07 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 2f86f154-a219-3d40-bfad-62a8e8b20ced | -4.83029 | -45.19702 | 2025-07-07 00:24:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b9efdfde-534c-3797-a715-8df26df824e2 | -3.92847 | -43.16065 | 2025-07-07 00:24:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6b21c18a-539d-3e84-a838-a52d63acdf81 | -5.59267 | -45.1841 | 2025-07-07 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| de547dc7-7e46-3123-bfa9-17e63aafc493 | -6.1791 | -48.0712 | 2025-07-07 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 82ec7a8f-00ef-312e-ba85-7eed5537db28 | -7.7126 | -44.5762 | 2025-07-07 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2206d691-4f47-3728-9219-adfbec69c7a2 | -6.1608 | -48.0289 | 2025-07-07 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 28155379-dca1-33b3-9630-352b265b5986 | -7.6938 | -44.578 | 2025-07-07 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 44e71cc5-d6c0-3260-8ad1-cdda191db319 | -6.1604 | -48.0724 | 2025-07-07 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b4a0105d-891b-3bca-84d9-a299688c62cf | -6.1606 | -48.0507 | 2025-07-07 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 215.2 |
| e13a2c71-9025-33f1-874f-d58181f6adc2 | -6.1794 | -48.0277 | 2025-07-07 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| e93a9c78-08a4-32a2-b903-5bbfaa858d42 | -6.1792 | -48.0494 | 2025-07-07 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 328.0 |
| 72798af2-cf15-34df-bdd1-cfa24be9ce22 | -6.1794 | -48.0277 | 2025-07-07 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| de6bda6d-bb8c-3582-a1d4-4a7d10a03e46 | -6.1792 | -48.0494 | 2025-07-07 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 195.7 |
| a721164a-c39a-3989-b7d8-c48fb95b3d60 | -6.1608 | -48.0289 | 2025-07-07 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 9f2941a7-57e7-3c10-a5b2-90565dc5165a | -6.1791 | -48.0712 | 2025-07-07 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| fd0096a8-c4f9-39a5-957d-2421abeba610 | -6.1606 | -48.0507 | 2025-07-07 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 9d5adebd-7900-332c-9314-acfdd24d4075 | -6.1604 | -48.0724 | 2025-07-07 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f3654420-a59e-3964-b193-8431116f6609 | -9.5152 | -40.331 | 2025-07-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 18583c32-3377-35d2-a4c5-0d99cc1a6678 | -6.1604 | -48.0724 | 2025-07-07 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 534585af-d61e-3649-b6fc-84d57ed888d5 | -7.6938 | -44.578 | 2025-07-07 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 379bdb14-6ac2-3f5c-85e4-93be2f2cbfc6 | -6.1791 | -48.0712 | 2025-07-07 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 179.3 |
| faa82810-c167-3336-aecd-34c3002d80fc | -9.4769 | -40.3365 | 2025-07-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| a6bb5b68-10b7-3717-a234-c306453b244e | -9.496 | -40.3337 | 2025-07-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 475.1 |
| c296eb71-e737-35da-9664-28f60b7e54b9 | -6.1794 | -48.0277 | 2025-07-07 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 966373e6-c9b2-3cfa-8670-b777c640ddea | -6.1606 | -48.0507 | 2025-07-07 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 284.1 |
| caf19767-6a2e-30ef-8b4b-8a73ddfda611 | -9.4956 | -40.3586 | 2025-07-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 71ab1623-caa9-31b7-af63-e5a0207882ba | -6.1608 | -48.0289 | 2025-07-07 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 6a71d9dd-df44-36a6-9ef7-76ba024d48e2 | -6.1792 | -48.0494 | 2025-07-07 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 320.1 |
| 8a8a0e0b-fe2c-3b07-80b1-d1f9c3ab62a4 | -6.1791 | -48.0712 | 2025-07-07 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 10f4dab1-31cf-3488-9d69-65967ec8d433 | -6.1604 | -48.0724 | 2025-07-07 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 66b2eea6-c429-30c4-93d4-7dd793287b09 | -9.4769 | -40.3365 | 2025-07-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.7 |
| e6e7ec37-27fe-3176-bcef-ec6e9279f278 | -6.1606 | -48.0507 | 2025-07-07 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |


[Clique aqui para ver as próximas entradas](README2.md)
