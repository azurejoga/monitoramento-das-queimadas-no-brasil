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
| 695fa2e3-ee15-3911-9ee9-e1f047a7f647 | -2.88688 | -44.37888 | 2025-11-25 04:38:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a7bada9-c2f5-334d-b248-dcece743d4b3 | 1.33066 | -50.86446 | 2025-11-25 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6ff3ac4-1475-38fd-80d8-056a8c0fcad0 | -5.90643 | -44.01022 | 2025-11-25 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b409945-a365-365e-b490-f26386819d68 | -3.10543 | -51.50376 | 2025-11-25 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e476f01c-64e5-347c-b59f-4dbeb45a79f5 | -5.63637 | -43.93032 | 2025-11-25 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d9be809-4d17-33b2-9b8b-e89c02474ec3 | -1.30065 | -53.14899 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2d91562-d438-315a-9c06-7b4778b2d39f | -3.76829 | -44.04556 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d74158f-ebf9-31f4-b28d-7af414fbe370 | -3.99019 | -43.43233 | 2025-11-25 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bef6167b-a663-3090-9838-3c91e8af4253 | -3.82165 | -40.69049 | 2025-11-25 04:38:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a6e5f06-aedc-3e5d-b76e-0b28d83f503f | 1.54753 | -55.63827 | 2025-11-25 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d66818d0-515f-31d8-ad50-0cf2acfe6c49 | -1.34274 | -53.1571 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6285f41-23d1-388a-a260-b3edb01e0b17 | -2.92839 | -48.23341 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef103737-0d64-3995-ac06-cb7e03bfd3af | -4.74572 | -44.45089 | 2025-11-25 04:38:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c0d0cbc-c48c-3ae9-bc54-375f0b9c157a | -4.66294 | -44.15162 | 2025-11-25 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 57648402-5f75-3245-9f5c-e572d6057ce4 | -4.05127 | -42.52158 | 2025-11-25 04:38:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5114bfdb-d658-30b7-8486-ed686494f9b7 | -5.78064 | -44.05316 | 2025-11-25 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b78594aa-ae50-3c43-a6af-42e5e4566c7b | -3.77627 | -44.04676 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e4c44310-da96-33fc-b10e-939d9eba3ea3 | -4.81598 | -43.83071 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 43157bc1-2fb5-34ea-8d2c-324d9ac94dce | -3.58506 | -50.28987 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62e01901-8b5a-3ef1-85fe-363049706805 | -3.38723 | -47.19033 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f129ba36-0d6d-33b1-bc59-cc8c68dcdd83 | -6.46417 | -43.55927 | 2025-11-25 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d29854d-85b0-3b61-894e-a9039673c4ad | -4.1793 | -45.52041 | 2025-11-25 04:38:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfe47ee5-8565-3bbc-8544-c2dfcd1e437c | -6.68764 | -43.95155 | 2025-11-25 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3dcb6944-34ff-3dab-a24f-2db8d92d9be5 | -4.20464 | -48.56465 | 2025-11-25 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 610f7768-825e-3fd4-b163-5beb75e49b87 | -2.48952 | -47.82803 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bddb82d1-f346-3adc-b111-f9cc096f4661 | -6.31818 | -47.12501 | 2025-11-25 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ece5e6f-1a53-34a5-92b3-35bd8610e25f | -3.82922 | -43.99469 | 2025-11-25 04:38:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6579667b-b1f3-3637-9db2-d1d1df8fc7ec | -2.87506 | -51.80921 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 714faf22-5473-3541-be02-c5aea98d0b17 | -2.43233 | -50.26504 | 2025-11-25 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d66b4ed-83fd-3cb5-8ce8-c334513a05c7 | -2.9361 | -48.22754 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 95022939-2cbf-3d48-abf1-e0d1f689a8fa | -4.33422 | -44.33034 | 2025-11-25 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30e03696-b41e-350a-bca3-c8fbaa997366 | -3.87232 | -50.16708 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9de47813-766a-32ec-88d5-fdefcbaf194b | -6.08601 | -41.6879 | 2025-11-25 04:38:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3a693153-79c7-3182-97b2-2e80571abbc7 | -2.32856 | -52.77 | 2025-11-25 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89bc405a-59e0-3a42-9d03-6651d0e82c64 | -3.71926 | -43.22155 | 2025-11-25 04:38:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b202974-a47a-321c-9756-416ca61443fd | 0.8429 | -50.10916 | 2025-11-25 04:38:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20571287-975e-300a-a9a7-d941b02b2d4e | -4.81244 | -43.82641 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19aeef74-1488-38a7-8ec7-c4af54a3be18 | -2.93224 | -48.23047 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e8ee2aad-4f33-317f-98ff-b4354668a201 | -2.93333 | -48.22357 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4e4fbd3-2b4e-3827-a9d4-44a0b65a38f8 | -3.20788 | -46.83365 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1fb46db9-093b-3382-8088-e560a9999b1a | -2.94272 | -48.22857 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 687f3aff-c917-302a-affa-e0a5fd692002 | -0.78854 | -52.41666 | 2025-11-25 04:38:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdecfabc-27e5-35fe-b2f7-670366cb3495 | -4.72654 | -44.7374 | 2025-11-25 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba081f06-c1ac-3db8-8b15-8bf432cc5196 | -2.47514 | -47.83292 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 081083e2-fbe2-3363-bbe1-a20f541c55c1 | -2.4862 | -47.82752 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b453840-862c-3001-888b-8f53d86cf5a8 | -6.72919 | -42.93922 | 2025-11-25 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d4465eb5-70bb-3485-9baf-f23894cd92f8 | -4.51311 | -50.54176 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b42ec30-1530-34cc-8cd8-e7f08cb910a3 | -2.48398 | -47.82005 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5980567-e0c5-3dcf-8041-97f089782bf4 | -3.88778 | -47.24035 | 2025-11-25 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b48285e1-8eab-3155-900e-a635bc1ab2c2 | -4.81188 | -43.83008 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9914ca0-c1c8-30e9-95ff-48ff12d4a1b0 | -4.82121 | -43.82397 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0c9b1f44-b666-3f46-ab92-41f19c1e2db6 | -2.93555 | -48.23099 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6c446a79-da28-315b-96b9-5c8825a1503d | -5.58384 | -45.16191 | 2025-11-25 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ec7e8fe-eb5a-3083-add2-511e1c699cc1 | -4.59262 | -44.04412 | 2025-11-25 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 030ce434-0609-3ae3-b47a-a582c5a8af8d | -2.93501 | -48.23444 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f21ad130-d272-3d8d-9ceb-efb4591fcc89 | -1.82889 | -45.57057 | 2025-11-25 04:38:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccefac33-f92c-3ac4-ba68-df653492894f | -4.95338 | -42.71008 | 2025-11-25 04:38:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63ec8b13-8fac-32ea-9afb-578bbe321622 | 1.55089 | -55.63896 | 2025-11-25 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2b2c4a4-ea59-3324-8742-eac7122956dd | -6.31333 | -43.8218 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12fa757d-6830-3897-8e71-83a2209b5a88 | -2.92562 | -48.22944 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e74e1c7d-132a-309b-ac99-d9c1ba9edf47 | -4.55057 | -43.29866 | 2025-11-25 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 42060823-085f-30db-83ef-c0d4a3881105 | -4.82531 | -43.82462 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 58ef65eb-d472-3e05-b2ee-0e9cdc8f8c22 | -3.80681 | -49.98306 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c53a1154-3e48-3795-9a76-9661b600377b | -5.29431 | -46.74677 | 2025-11-25 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c67dc9ec-6c36-3567-b262-f42902016916 | -2.39596 | -45.62733 | 2025-11-25 04:38:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6688428-6f07-3bf0-b6ee-ee21ddb8ecab | -5.03102 | -43.25875 | 2025-11-25 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23ddd5eb-5a9b-3883-8dd4-12ec21d16677 | -4.33766 | -44.34015 | 2025-11-25 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5f99ae5-8c89-3204-b11d-cc9b770a4cc6 | -4.17538 | -43.82967 | 2025-11-25 04:38:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3cfc70e-4889-350d-a093-7f3f47034ac9 | -3.20903 | -46.82624 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0152cf09-1263-37a0-8619-8d643bf3c108 | -3.10531 | -51.50441 | 2025-11-25 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6925dd6d-e6c1-3a47-b0f9-fc4d748ec4f5 | -2.49312 | -47.82506 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ba691c7-4416-3489-a4b4-8d2ee37338d7 | -2.75011 | -51.90969 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16455f01-1b78-3606-9cf4-324506b42b1c | -4.59189 | -44.04414 | 2025-11-25 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3231745c-9022-3436-bf4c-5624ba9da201 | -3.58786 | -50.29398 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b87bc5f-ed2a-359b-be3a-42e1cb60ebef | -4.7487 | -44.45329 | 2025-11-25 04:38:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 586fbbdc-a858-3e4f-81eb-b845b4f2571e | -3.77974 | -44.05078 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3f1a9cf-ee84-32ad-8fe5-f064eefd8b79 | -4.18352 | -43.83086 | 2025-11-25 04:38:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e56f1b4-71bf-3d94-b171-7a77d3f0e05b | -3.88834 | -47.23671 | 2025-11-25 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1eef64c-5e70-34da-91ef-245fd1f904a2 | -3.96861 | -47.66525 | 2025-11-25 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f779e04f-a1bb-3857-8af3-45187f15e6b2 | -4.81543 | -43.83439 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3af5870-db20-39fa-8729-db559547658e | -2.98731 | -52.62516 | 2025-11-25 04:38:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bfd2163-b287-3b4a-bcf9-0e9a73356503 | -3.82868 | -43.99816 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee9706fb-9dd5-36e1-9c39-8b4db2d46568 | -8.1618 | -43.19429 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 56204c8c-b335-367c-acc8-69f52db78f87 | -7.56597 | -45.86844 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e436c9d0-fad1-3ac6-9055-b3ac1180def3 | -8.05279 | -43.13861 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| fe594a1d-9079-3d21-b615-2f4c0fa61d33 | -6.83933 | -46.26976 | 2025-11-25 04:40:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cdd326a-788e-3f98-bf09-e04cf8bfef50 | -8.04892 | -43.13343 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 57e9f171-d00a-3f64-aa7e-3eda96243aa8 | -7.56828 | -45.85719 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20bf27ce-a752-3f22-8ad3-e2e2eeb417a3 | -8.06184 | -43.1398 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 18554dd0-5985-34ae-98b0-1c26edbdddaa | -7.56628 | -45.87092 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a50b028c-ef29-3f51-9319-97cd0aa7f434 | -8.04506 | -43.12822 | 2025-11-25 04:40:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c77f20af-e9f2-31aa-9581-70570b1151a0 | -7.5632 | -45.86574 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c17ab82f-fc49-3213-a3a2-815ecc2a08b5 | -12.00521 | -49.27472 | 2025-11-25 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fce7ef5d-3130-375d-b062-6707d54da15d | -12.00184 | -49.27419 | 2025-11-25 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2f8f26cc-8f5a-3eeb-aac5-d5b518cd52bb | -7.57487 | -45.86047 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85bfee0f-aadf-3580-a11a-e269a4ba875c | -6.83869 | -46.27397 | 2025-11-25 04:40:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 705883b6-bbc0-35f3-88fe-5f0c2ad799d0 | -7.28235 | -45.11951 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0da4708-bb8a-323f-b990-410f81870fb4 | -7.57137 | -45.86231 | 2025-11-25 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2503220f-aef8-3c46-bd1e-d3c859381006 | -7.46106 | -45.18357 | 2025-11-25 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd358230-0c5e-3c41-8ea2-ce3a5ccf0b21 | -7.86486 | -46.75216 | 2025-11-25 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README15.md)
