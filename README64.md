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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36928dcd-1f0c-3998-b0cd-a414a22d3c52 | -7.35753 | -47.63316 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db8a5664-7024-35f2-b203-9bd1cad9bfcd | -3.92548 | -47.69451 | 2025-10-29 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a2f16d4-2b76-3eed-a4ad-a0a9cf4c8e08 | -5.65622 | -47.82707 | 2025-10-29 04:44:00 | NOAA-20 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76e65449-dce8-3cfd-9644-9128c66a5d7c | -7.07507 | -44.95419 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f10b82f5-57f1-3e87-90d3-e2b2b74e1253 | -4.47488 | -43.43744 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e7cc620-1a7e-3c0b-9606-c8a71c28a8b5 | -5.09908 | -46.18159 | 2025-10-29 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 101d230a-f8dd-3a12-9be2-fd6b9f777445 | -7.80353 | -46.48164 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79c640d5-5342-3a09-a4ab-3477ebb1fc66 | -6.10857 | -42.43757 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 95130949-58fd-32db-91c2-bdfe95f610b5 | -1.21167 | -54.07482 | 2025-10-29 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 287575d5-e1dd-3fa5-8dad-4f4ff40f1b84 | -6.10262 | -42.44284 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2dbaa5b4-a70c-3829-a5e3-befdcf85780f | -3.12113 | -51.21042 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed75dcc2-d3e5-39b9-8159-69cc26a6af55 | -6.12804 | -41.84967 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 11ec1ffa-bfbe-313a-9c3f-d03ad5510277 | -3.22494 | -51.19792 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4901673-da49-3231-a5a4-6d5c82d9b7cb | -4.61491 | -46.59552 | 2025-10-29 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06b4f6b4-fe50-3242-a1ab-4da5755d27f0 | -8.18574 | -44.44748 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72a78f94-3b57-3c1e-bb97-6f9cc26b1b7b | -6.64823 | -43.61102 | 2025-10-29 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9db3db50-e5eb-3612-8c8b-22fed244a941 | -3.60363 | -48.99097 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 220957b5-6bd5-37de-aa73-bea92bb5b406 | -6.15274 | -41.57464 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 115bcfef-de52-390c-9b03-db7861f5c56d | -4.4397 | -50.15768 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82389fb8-9268-30de-8fb8-4f2f098e946c | -4.63458 | -48.69695 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 882d9064-7aba-3989-a1db-b4674a8c81f4 | -3.48031 | -52.86434 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67c4db8f-5393-3e40-b45b-2d9a46d761ed | -3.15491 | -49.2537 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0d4a73b-4714-301d-ab54-2b91d80d188c | -7.89864 | -49.17617 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f170868-d317-3102-b0bb-a9a55bf86948 | -7.06828 | -44.94027 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81259785-588f-3f88-b31f-50b4339602ec | -5.56372 | -42.16979 | 2025-10-29 04:44:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd3ee0ae-5662-3355-ba4b-7871290a19a1 | -2.57834 | -47.49369 | 2025-10-29 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fbc8e62-9416-3aa2-99f0-3724de39b35e | -6.99684 | -49.00784 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2952a87-170e-375d-afcd-a11660f93214 | -7.43205 | -41.85865 | 2025-10-29 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 61c4324e-731e-362a-8fed-1f47f682a293 | -1.20057 | -54.21685 | 2025-10-29 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e46d225-186f-3857-9902-cc2e179e9c8f | -6.99344 | -42.78883 | 2025-10-29 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3144a261-a8a0-3aa6-911a-2ac5887e0b37 | -5.59003 | -49.06919 | 2025-10-29 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fa8907b-23bd-3347-b4de-d250318344ef | -7.7909 | -46.48502 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1e8f250a-5a90-33fc-a22c-fdd4d7de8f94 | -6.97137 | -49.4012 | 2025-10-29 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1107b415-afd7-32a4-b1a9-689af6ad94ec | -4.64429 | -47.95879 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9da530e-32ad-3467-aab0-21c1b427c1c9 | -7.80728 | -46.45646 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 996f7583-2c5f-346a-ad89-6e12c6285227 | -6.1385 | -41.71082 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 659f8703-f4a8-3405-b8ce-4b1a747f54bc | -4.98896 | -44.68795 | 2025-10-29 04:44:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 391fb488-a919-375b-a162-87231621e57f | -7.78279 | -46.45778 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce764533-6a79-3290-8d27-f4fe75ef3e51 | -2.1724 | -48.23828 | 2025-10-29 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d702e8cc-16e4-38c4-8479-f7598854d97a | -8.71624 | -47.99038 | 2025-10-29 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ea49d7c-75d3-30b2-a126-6254bd3a9dbf | -9.3407 | -43.091 | 2025-10-29 04:44:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c4d3e93-faf1-3921-9eab-0ec1fc7c4922 | -7.07864 | -44.94128 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c65bbd35-2725-3287-a184-a5f5fe8ae2dd | -4.26943 | -46.92564 | 2025-10-29 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70d6c0e9-9022-3aa7-8d5e-0570057c35c3 | -7.30383 | -46.31413 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9340c71d-588a-3f7d-a800-13c360e4b3a9 | -4.01078 | -49.03514 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aad9338d-884f-379f-bdc2-da7c103dd5bf | -5.59094 | -51.13017 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99287860-e8f6-322b-ac53-382a05af81b7 | -5.41834 | -44.64364 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 59951270-2f4a-3c3e-8b33-3100eb66fb87 | -4.44024 | -50.15423 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae7b122f-25f6-329a-9f4f-f41c5bcc609a | -6.12483 | -52.38785 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5afaa6a7-97f3-38a8-9873-b2ff48c1b787 | -3.04547 | -50.27255 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1262933b-c40a-3650-b4b6-385d459ae93b | -4.37124 | -48.67945 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 112b1b36-4a32-38dc-beec-18373b23db7f | -7.64036 | -46.91633 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 006e01e6-67a0-340b-b324-4432d3a332f7 | -2.41995 | -49.30325 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7482ccb-7a1f-329b-86d4-4e462b3d78e4 | -7.9344 | -45.47839 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 160fa4af-42dd-369b-9239-f278af6d2a55 | -7.32197 | -44.7444 | 2025-10-29 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03f3e85b-a829-32ce-8a5d-01dfd46862b1 | -8.29449 | -49.3118 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18003d73-a8e6-3ac7-b7ca-fc86ae63a718 | -8.2336 | -49.77937 | 2025-10-29 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2301b655-492e-32e4-a0e5-d2c91588e1e3 | -3.72461 | -41.57298 | 2025-10-29 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd728220-6faf-3835-afa2-d1fb7d72aec1 | -4.2659 | -50.50371 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 380aee46-239a-3ba3-9439-351f87492e64 | -1.49263 | -47.81158 | 2025-10-29 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ed9195b3-14c9-38e5-9149-9966dc865f5f | -7.3171 | -47.20012 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d09e1c7-2357-3d42-8b3c-f19dece9b0a2 | -7.27781 | -46.89268 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c5698460-2202-3e56-b2ee-07493ec7f45d | -6.12365 | -41.84234 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 122b89c5-4a8f-3291-b083-62f460965301 | -4.28826 | -49.65122 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ecf829f-2c5f-3014-a5bf-a8b0a3ebe273 | -5.48159 | -46.43951 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b0e40cb8-b9df-3d28-bc34-45a9fcad064d | -7.64167 | -46.91884 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85b463ac-be8e-34fa-a03c-0ee9e18178e6 | -6.09869 | -42.4702 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 53e70a06-e833-3d42-9424-1cf5579bf53a | -8.51961 | -44.0977 | 2025-10-29 04:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 558ee993-5f32-3b8c-af99-158559ca3eee | -8.24586 | -46.90375 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1728b0f3-72c5-3570-987f-265963c43abd | -3.38471 | -50.16786 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62239301-8a93-3ccd-b3ac-52acdc4b37e1 | -4.08677 | -46.94351 | 2025-10-29 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8f5feaa-ff42-3a59-900a-2ab67de11a46 | -5.16962 | -46.16231 | 2025-10-29 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a884a632-c204-3052-adf7-d55ab7c9074a | -6.99303 | -42.79179 | 2025-10-29 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 19a9fd53-4c86-327c-b42a-87fb4faa9b45 | -8.00143 | -46.68584 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ec0fffb-648a-348e-b502-ed53e36d2172 | -3.10623 | -42.61456 | 2025-10-29 04:44:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e75a272-db71-3d1f-80fd-1d53e21ab918 | -6.10884 | -41.72748 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| acbfaf91-e4db-344c-b49f-aab88e69c892 | -7.62941 | -46.92199 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e602fb5f-ac9c-3f0e-853f-dd96ed749cf1 | -7.90537 | -45.67784 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69c70eff-8db1-3efc-9f62-f7bd58415945 | -5.42694 | -46.34575 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7abbed16-1e40-3758-8232-3135fcf28803 | -7.79691 | -46.44442 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4d6b8666-e7bb-35a9-99d4-a78e59859906 | -5.34458 | -46.86165 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9122bc3b-edeb-3042-8cd3-5a6b0a9cee45 | -4.67672 | -43.24096 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2df548ec-df04-3192-a9ad-26083875be9a | -4.20355 | -50.0814 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e006636f-7e2c-33ae-87ae-4b0a34541f2d | -5.61959 | -47.11544 | 2025-10-29 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe545107-7a22-392c-8c37-23399d684dd6 | -7.80162 | -46.43999 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| edfa41c0-3b61-3282-a2d9-af8930e4f47e | -5.19417 | -45.62911 | 2025-10-29 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bf3d2b0-56a7-3de8-98ac-02995c1f6e09 | -1.28016 | -52.92595 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6250abf1-e2ac-3662-a2be-cae33738218f | -1.4963 | -53.12685 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 439a2687-ec0c-34b8-8d21-41601889775d | -4.00687 | -49.03819 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37752406-da74-3fea-88b8-6d558c59c415 | -6.12432 | -41.84557 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| fa29da44-4d63-36c2-81da-8dd34b2478dc | -7.43707 | -45.12759 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02a37a2e-de28-3852-81e3-8970cdaa9364 | -7.75093 | -44.72206 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51a73206-b09c-3836-9d74-6fb67affa447 | -7.53687 | -47.30766 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca6daa2a-1e21-39a6-99c1-e7287f134d0a | -7.27393 | -46.89244 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ea694e49-5ed5-3582-b19e-b76436627f33 | -5.97226 | -46.31882 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d154d32-a4e2-39e5-b7e5-fd569acb726b | -1.49379 | -47.80415 | 2025-10-29 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06a6d706-0901-3216-91d1-41a112587100 | -7.7937 | -46.43871 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68b70898-2e78-3b47-a65b-56de2d450b56 | -5.60121 | -45.35885 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 965dac59-5d9c-3253-a86d-b462281d4ec7 | -3.97546 | -49.8905 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f402f08d-a423-3c4a-94ad-ed9e476a7d8d | -7.28167 | -46.89308 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README65.md)
