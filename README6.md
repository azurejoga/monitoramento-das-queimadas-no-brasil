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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb69235d-f818-340c-b7cb-4e9bf66e1217 | -7.79207 | -46.0155 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 890fa8c2-a7d0-3e5a-aee7-fd8267a3f406 | -5.3648 | -46.29604 | 2025-10-10 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 57f9ca99-6fe9-3848-80ec-780898339d7a | -8.51175 | -45.96193 | 2025-10-10 00:35:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 887dad51-3a28-357b-a810-6cb9a8832437 | -3.33426 | -44.42273 | 2025-10-10 00:35:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 44b15f2d-7c79-3e3e-bcac-2158e3f6a464 | -8.84149 | -46.05206 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ca06fd81-6f9c-38e2-a29f-326edf77f4dd | -8.85285 | -46.06179 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 47745d20-6e40-36f0-97f4-85e43e32c645 | -8.89842 | -46.01444 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 431e13f8-1d2d-36d8-bd34-6b35d9b9b4f8 | -5.28738 | -44.88694 | 2025-10-10 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 82309451-8eee-3ea8-a37a-86bf3b161593 | -6.58283 | -44.62156 | 2025-10-10 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 50924ed4-825b-3357-aaf6-2877b9baa957 | -8.00558 | -46.57933 | 2025-10-10 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e90cdc7b-dde9-3387-8bd7-b45f093ac926 | -3.83535 | -50.97475 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be153585-74ef-3076-ae97-79370e95e266 | -3.29707 | -52.61831 | 2025-10-10 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a2683cb0-2159-3dc1-9d86-c9064f40d1a6 | -3.78909 | -49.4393 | 2025-10-10 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7c8dad0f-6996-3cfa-abb9-dd5aec31b207 | -8.16618 | -43.32922 | 2025-10-10 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| c6efa4f8-b3e2-3df2-8002-6f83fbd6849c | -3.74628 | -44.39029 | 2025-10-10 00:35:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| fba032fe-4c71-38b6-becd-f589690593c0 | -1.41149 | -46.71162 | 2025-10-10 00:35:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b383baf8-abc9-32b6-9e0e-611c94244a7c | -6.74914 | -42.85419 | 2025-10-10 00:35:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 6be6aa3f-fac4-31da-b791-164aca2a3e8e | -7.39937 | -39.78654 | 2025-10-10 00:35:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 4445b54e-009a-3d9d-a807-040dc0fcd9f7 | -7.25958 | -44.91117 | 2025-10-10 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 49259152-1f2b-35bb-8cc5-8880e9d638f1 | -2.90001 | -49.40224 | 2025-10-10 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 23770032-1a2e-3c51-95e4-f4aa6f9fc7c9 | -2.92161 | -48.31329 | 2025-10-10 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e1f5219-7909-327e-ae79-772f371662fd | -2.82257 | -47.72269 | 2025-10-10 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a10a3ef-98b9-3f52-9b51-f95c7b7fa7c4 | -7.33347 | -47.8204 | 2025-10-10 00:35:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e89c56b3-e8ab-369c-8535-ed7bd011b0b5 | 0.71923 | -51.37321 | 2025-10-10 00:35:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1dc49246-d5bc-39e4-b98c-207a2028868d | -8.19031 | -43.32515 | 2025-10-10 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| e5ea0bc3-0774-35fb-b7a8-a4b7d9cf590d | -7.40856 | -39.79021 | 2025-10-10 00:35:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 27ba8c07-e690-3be5-9529-3a8d448a8010 | -5.463 | -44.06247 | 2025-10-10 00:35:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4605fed8-117c-3efa-bc76-95d66b5c9b38 | -3.00144 | -48.74571 | 2025-10-10 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9afd4fa9-4e13-312a-92d3-4f9f611743aa | -4.84693 | -45.4128 | 2025-10-10 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 33d24701-5dfd-3086-9801-5eaadf3bbc1b | -6.46232 | -44.585 | 2025-10-10 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 037442fe-5063-3b5d-9523-e761f837a4e4 | -2.67821 | -48.41558 | 2025-10-10 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 08c1c9c1-e2ac-3f93-8f91-72cde388d95d | -2.89606 | -48.06746 | 2025-10-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1a9029fe-ca86-3f8d-8929-3c55af1024d2 | -7.92146 | -45.50135 | 2025-10-10 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f5ba070a-9fe6-390a-ae0f-55d269b9f858 | -5.286 | -44.8776 | 2025-10-10 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| db2a6fdf-6c14-3dd6-8a3a-aba163c240c1 | -7.20454 | -45.49472 | 2025-10-10 00:35:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| b02f36c9-fc64-3f86-8f81-ff6ff79633e9 | -3.59797 | -48.98894 | 2025-10-10 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| e3f3d8ab-859d-3ac1-9027-e90e178b563f | -7.05235 | -45.05218 | 2025-10-10 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ba5fb185-79d5-3fff-9610-e8a5a79d8683 | -7.00302 | -46.99594 | 2025-10-10 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a2048ce2-e351-340c-93db-f67676a0e9c6 | -3.77564 | -49.1353 | 2025-10-10 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22cf7f32-97d6-3b45-9f5b-076d3bd974f1 | -5.6584 | -43.6162 | 2025-10-10 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b15a6ffb-c4d7-3697-9c88-aad4a62c70d0 | -5.48008 | -43.05478 | 2025-10-10 00:35:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 618f270d-9ac5-3710-8d03-55369ab9e83f | -8.84307 | -46.06293 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 15379ee5-6ec9-38bc-9af5-69ff53ed3812 | -5.49626 | -43.07352 | 2025-10-10 00:35:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 03c86944-f3c6-37aa-bd4c-0c2bcfcb5253 | -7.62442 | -46.8299 | 2025-10-10 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9cf46ed8-ca58-3f3e-a68e-d2a94a34b9f5 | -3.33173 | -44.4053 | 2025-10-10 00:35:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4fa524e7-86aa-3f13-b320-32b2bcfeed80 | -8.21062 | -43.37597 | 2025-10-10 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| c02ebc96-cba5-3b40-af23-7de75368f548 | -3.80426 | -50.2138 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a97fc9ce-ef16-39bd-8c21-3413657c9375 | -2.54707 | -47.80116 | 2025-10-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9153cc37-b318-3ded-b275-331345e7d815 | -8.52017 | -46.15346 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 0bc443a9-f5e1-399a-89fa-5e3645b791e5 | -2.99883 | -48.72715 | 2025-10-10 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 379f903e-66b7-3650-a8de-631f48c17cd9 | -7.77259 | -44.03983 | 2025-10-10 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 39503821-086a-369d-b482-9fbc624e3a14 | -1.40353 | -46.70633 | 2025-10-10 00:35:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 76ba68be-15e1-3219-955a-eefd46ab2a98 | -8.68693 | -46.72366 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9cf758ec-7835-38a4-8a19-eaafbc7b1ed8 | -3.53146 | -48.91203 | 2025-10-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a61c61b9-46a7-361f-9d58-c8e5785648a4 | -7.91967 | -45.48922 | 2025-10-10 00:35:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e8f866fc-1dcf-36c0-b001-78949395dee8 | -2.18409 | -54.48083 | 2025-10-10 00:35:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bc4ba575-1eb4-3953-adf7-44bfad240912 | -6.59623 | -44.63466 | 2025-10-10 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7cfbc2ab-b17c-386d-b754-7ca6556b9d15 | -6.82048 | -42.80145 | 2025-10-10 00:35:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| bc23017c-fa79-31a0-80a8-c1f2af768309 | -8.51854 | -46.14252 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2b5bcbfa-3cd5-3219-ae61-7cf3b96e5b39 | -8.19308 | -43.3428 | 2025-10-10 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| bfa5d98b-57ff-3937-bf2b-86d637fa6d91 | -5.70665 | -44.21889 | 2025-10-10 00:35:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9b8dad4f-ebb5-357d-aca9-fbe081e52ae9 | -3.54169 | -48.91985 | 2025-10-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e8ccb51e-1439-3e28-9b70-f34f6b170a45 | -7.78905 | -46.55938 | 2025-10-10 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe945039-18ca-37b2-98a3-57bafe0b71fe | -2.49411 | -47.56274 | 2025-10-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cada7589-023c-3b94-870f-dc73071b2463 | -8.85126 | -46.05081 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 44127b5b-7c67-367c-9c55-6067daac746d | -7.40944 | -45.92122 | 2025-10-10 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| dc23dd47-020f-384f-9ed3-e96c6b169533 | -4.18781 | -46.23565 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d7948f35-0e21-3b23-96aa-6de4a5eb9cae | -4.17921 | -46.23017 | 2025-10-10 00:35:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4aa8631e-1720-3461-b78f-229c662b611c | -3.88286 | -50.98011 | 2025-10-10 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e845d25f-7b4e-3cfa-b9e2-60e87947ed93 | -2.67685 | -48.40596 | 2025-10-10 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 098041f9-fd04-3573-92b6-91fcf44877ed | -7.78646 | -44.05376 | 2025-10-10 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 7aa967d9-ebb3-3069-9d83-c832ab2fd3d3 | -3.54295 | -48.92894 | 2025-10-10 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab076ec1-a288-31fc-a3c1-38e7c9da638a | 1.94333 | -50.91282 | 2025-10-10 00:37:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5aa02361-8eac-37a3-a143-74b7536f7101 | 1.12789 | -51.41005 | 2025-10-10 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0cfbe4d8-2bf0-3645-8177-d2965d24a425 | -4.6505 | -43.1805 | 2025-10-10 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 9fb63cef-a729-300d-bc76-67f89885bda2 | -8.5221 | -46.1301 | 2025-10-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 224.9 |
| 901baa91-8e3c-39d9-bca3-5415e4d58cc0 | -17.9382 | -44.9909 | 2025-10-10 00:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 73c974c5-d4e3-3b80-b248-6cec9a1066dd | -8.5407 | -46.1507 | 2025-10-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b5f2bd73-e9cd-37c3-b276-4d4c75fe0b17 | -15.8991 | -43.3065 | 2025-10-10 00:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 088b6590-b613-3444-a7b8-51533e11d98c | -5.6373 | -45.9705 | 2025-10-10 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 9a891e33-075a-3ca5-b154-d59dd5f25672 | -8.5218 | -46.1526 | 2025-10-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 9948a010-c38e-3739-b02d-d0a8f39cf105 | -8.5032 | -46.1321 | 2025-10-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5b80fe01-df29-38f9-98d9-febd563127d1 | -7.3966 | -45.9227 | 2025-10-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| c7f7ea5d-7350-3b06-909b-720f045870dc | -8.8435 | -46.0519 | 2025-10-10 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 3eab3fc4-88d2-34d6-baf0-2850a4db3a50 | -8.5029 | -46.1545 | 2025-10-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 98f11fc7-0837-3b21-a755-a1d9700f887d | -15.9195 | -43.2779 | 2025-10-10 00:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 382.2 |
| b983b3e2-271d-378e-8a7b-e23d51824665 | -6.5849 | -44.6327 | 2025-10-10 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 84e1f236-775f-3518-8eee-4b697ab69f13 | -17.9369 | -45.0388 | 2025-10-10 00:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 35801d14-d94c-33cb-81a3-16eb366a20b1 | -7.7755 | -44.0396 | 2025-10-10 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 3cbcaf08-1f18-3866-b3a2-8dc4866f789e | -4.6504 | -43.2038 | 2025-10-10 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 563d2427-e6aa-3d39-8281-c3b9bf6e7ef5 | -17.9376 | -45.0148 | 2025-10-10 00:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 363.7 |
| fa89f42b-7e54-3ff6-82ef-b32012313744 | -8.5409 | -46.1282 | 2025-10-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7a28fbd1-82bc-3a72-b608-0a2e3675a22b | -17.9577 | -45.0103 | 2025-10-10 00:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 114.5 |
| c158952e-0c9c-3fdb-8e0b-cbf1e7cfc140 | -15.8997 | -43.2822 | 2025-10-10 00:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 6157c2b0-b7f4-37be-a783-8fb2947f0094 | -15.9189 | -43.3022 | 2025-10-10 00:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 277.3 |
| f37228ed-212b-317a-ab08-2d0e20aae192 | -17.9175 | -45.0194 | 2025-10-10 00:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 7817a188-0cd9-335f-b3e8-1b8fc14f0b47 | -17.9168 | -45.0434 | 2025-10-10 00:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1bd3b4d8-9c6b-37f2-9716-fd13dad388b3 | -8.5184 | -66.9954 | 2025-10-10 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ceba4950-54c3-38a3-a8d4-da4e27e487f9 | -7.4154 | -45.9211 | 2025-10-10 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 09fdb3ea-33e8-36b2-a3c5-4a9bb21bb1f8 | -5.656 | -45.9692 | 2025-10-10 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |


[Clique aqui para ver as próximas entradas](README7.md)
