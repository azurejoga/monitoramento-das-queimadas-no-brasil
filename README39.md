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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 318b12d1-3094-365d-aac5-eb7b6ea5be01 | -3.70499 | -60.61647 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21136e54-8aed-3028-8299-de01461f83d6 | -5.89447 | -52.06296 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70e222fc-97c9-388b-8ce6-5ed821791922 | -3.00376 | -57.92612 | 2026-09-16 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c985d63-4954-3d28-9432-febbab0a86a0 | -2.89578 | -50.43228 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cdf6a73-20ca-31d6-b958-d759ae815994 | -2.98457 | -54.16049 | 2026-09-16 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 419fbff7-d62e-3581-a5d3-dc3381ebb53a | -3.14457 | -51.10757 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7115b5d1-d2d0-3e55-8bf9-4d20c45eb2ca | -6.72956 | -48.10939 | 2026-09-16 04:57:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ff47184-c147-3c13-9c03-c65f4bf10f4a | -3.37874 | -50.45352 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b0d9a2f-598e-3272-9ebb-952fcfb5f906 | -5.3727 | -56.04586 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a42f8ae6-25a2-3ceb-bc3f-89f604167957 | -2.70504 | -57.53066 | 2026-09-16 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad012921-bb46-3c61-bdeb-7e8ee59ed278 | -5.85269 | -52.06468 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 595565de-9a17-3ced-83a7-84c8531fd83e | -6.71938 | -58.80384 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b213cb52-3b39-37ac-8857-d79a961bea67 | -7.51766 | -47.56631 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cce5783-a5d2-3fa3-a967-b9b92bd666ee | -4.52818 | -55.0774 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55ff29d2-729b-32ce-8502-70ac2ee609c7 | -4.54027 | -54.93508 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c706fe3e-27fb-3a18-8a2f-cd50d667ca22 | -5.7807 | -45.09452 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 77f5b47c-3d4c-33e1-8594-f4643bef78e3 | -4.51698 | -54.97462 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b64104e-dcf3-320d-a0ed-ab833579d489 | -8.33641 | -51.30972 | 2026-09-16 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 857556cf-a654-3f7f-8eac-f5e4a6a56f68 | -5.12641 | -55.93938 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a64421fa-6f27-3758-92b9-e0e5b3a51e70 | -9.09896 | -45.73018 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68b365d6-78d1-3d7b-98b4-81e1f7a923dd | -8.0184 | -54.83936 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39195f4e-2099-3d4e-a8d9-51319984d359 | -2.32588 | -47.2025 | 2026-09-16 04:57:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58fa0ef1-10d5-3bbf-ac52-383240c56940 | -1.28697 | -55.71525 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d697d371-224c-3458-afb0-e712c5331951 | -2.1035 | -52.03998 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdf0dd3e-76b1-31e6-b141-bf288873c0b9 | -3.32681 | -57.86843 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11e4825b-4b0b-3acd-ba2e-4afbfcc561b9 | -6.19249 | -53.28128 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0236bb38-4ebd-3010-b11e-c3201913595c | -3.33418 | -58.13173 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4935f898-32a3-3485-b522-7be190392831 | -8.57383 | -48.51393 | 2026-09-16 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47d8a5c8-306d-3c79-ab9b-9f66df9f1717 | -3.7629 | -59.39313 | 2026-09-16 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4096dd7b-5215-3853-878c-eeeb1630c715 | -6.09636 | -57.68515 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ae9fdf0-57b4-3a11-8964-860d487bffe2 | -6.66624 | -50.91955 | 2026-09-16 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff9678d0-155c-3eca-bc80-a742705bf3a0 | -8.05054 | -43.74473 | 2026-09-16 04:57:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 41c893fe-c980-3caf-97f9-3a4c66f62414 | -5.1304 | -55.93623 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9887bd35-d57a-3812-876b-4296993dd4a9 | -5.3687 | -56.04901 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ccb648d-51de-3969-b39a-299ce000fc4a | -6.32945 | -59.9938 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50d8593d-6ab3-380a-ba17-1a492277fd6b | -2.87245 | -49.14186 | 2026-09-16 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a7415a6-9f7e-3f23-97ad-1069795fd63b | -3.11258 | -57.67697 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d09acf66-39d3-3a10-8499-4a13a10ef062 | -5.63395 | -51.69845 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 95af4bc9-3adb-39af-aae0-47499909585e | -5.38455 | -55.90416 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4259131e-ab3a-32a6-aeca-f6ce12ddc711 | -6.66322 | -50.91459 | 2026-09-16 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c16d758-95fd-355e-8bd3-8b3523abd95f | -2.91822 | -50.406 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c3226b0-7939-3533-928e-6d3e1e591163 | -3.48785 | -50.37794 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2add8bc8-3f31-3a74-a4f6-cca0258906dc | -6.10468 | -57.63475 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81fc8394-5448-3fd3-a824-32fe5db07c34 | -6.26992 | -43.28132 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a210bdc0-d6da-3e54-a137-e1523ebc9e1a | -3.1083 | -51.18134 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 392016a6-38b0-3508-83a2-15c86aa5a031 | -5.15486 | -55.93616 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 7103802b-3c94-30fb-b35a-7226e7505c38 | -2.82122 | -51.34277 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5588980c-26dd-38f9-9807-37d22f8c614f | -6.33573 | -62.6823 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 33b59027-e0d9-3fa8-b115-5c7cf3a61d9e | -4.30376 | -49.12426 | 2026-09-16 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3686b0e8-507f-3495-9938-5d16bbb9eafd | -2.9157 | -50.4226 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfb4833f-ab3d-3570-9ee1-4683e48c5154 | -8.78272 | -45.89961 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0438d5e-cc13-394d-9cc2-305d4fd20070 | -7.01146 | -46.52224 | 2026-09-16 04:57:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 410f1571-4e0d-330d-bc44-78dce0640cbb | -6.95152 | -42.57737 | 2026-09-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 90ca5b84-89ac-305b-b901-0da823a82831 | -2.57913 | -55.99204 | 2026-09-16 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06813cfc-da79-311a-8555-9fc5f28e9ea6 | -4.49106 | -55.49965 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb434ff4-7d4e-33b8-b299-6c87c7adfcc6 | -6.00215 | -44.31538 | 2026-09-16 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 750a077c-6067-3ee2-bf0e-e2f44b7dfe6d | -4.46359 | -55.05293 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5d4de65-a07c-3f1e-a200-afe17321aba5 | -3.02072 | -51.34466 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 80926fc1-c4f7-36be-94ed-d8f673eb52d1 | -7.15646 | -52.71233 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51a3b0bb-b9cb-3b7e-92a0-f4f9ea5490a8 | -2.90723 | -50.4298 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06202128-6ac3-353f-a657-3ffe4e304ac3 | -2.91289 | -50.3924 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc34b996-cd54-35fa-a2c1-88ddf83867c0 | -7.08717 | -42.09997 | 2026-09-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0b897692-03ae-31e1-8bf9-b7494f13a018 | -3.57594 | -55.59652 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e8dd5ac-a821-319b-bb7f-80a5421f5133 | -2.77454 | -51.3704 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 63628ed6-3225-3f99-935a-354ec279d3ea | -7.51763 | -47.33583 | 2026-09-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d62095dd-c17e-3bb5-a048-fbbe318daf98 | -2.8928 | -50.42758 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8404d40-b789-3c77-814d-7817a8205a6f | -5.84001 | -52.032 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4d40fe2-92d9-374d-a488-4d96df3d16b9 | -5.84117 | -52.04761 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 894c95a5-bd31-30ea-959c-ea9f2db27895 | -6.76946 | -58.81195 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2322ee74-fccd-32b4-84d6-7e2cfa636c01 | -6.40503 | -55.25566 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db74649a-7708-3d74-8cbe-b6597efee42c | -2.78548 | -51.36819 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1263a1c-a1d2-3cf9-bda7-64259dffc54b | -6.29026 | -59.92061 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee1a4059-1d98-38d7-9721-6bd8c71a8bdb | -2.88982 | -50.42287 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4819c75-b2a8-38fa-9034-b08c9fdc55b6 | -4.38732 | -55.04105 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d46957e-96f4-3243-8ff8-bc970551371f | -4.81488 | -42.88526 | 2026-09-16 04:57:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61f06e0c-42a6-31bb-b402-8b2f2d3ba6ad | -6.27264 | -55.29593 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2eef877-5a41-3441-a7f5-d7f50c7ffdb3 | -2.90064 | -50.42454 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 440ffd97-5413-3027-a52a-88c90ed6f658 | -5.86124 | -52.12398 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 514e4953-f07c-3b67-9e33-110df8ede843 | -5.45879 | -60.22192 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39486577-0c60-301e-b461-0832576b7ebd | -2.82239 | -51.33521 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7dc0c7c-26ba-3a82-bcfd-4ff7e1c2b061 | -2.82181 | -51.33899 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b9e2d58-362b-3978-a703-f956d11a12a0 | -3.04636 | -51.27063 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76608de5-db80-3bdd-92e2-749e70e7a70b | -6.71633 | -58.79838 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30e70371-f0cf-367c-8c45-5007c0a8fefd | -3.45648 | -60.52028 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb03b9d6-1d6b-3dcc-89a2-189116f7bcc8 | -7.83009 | -50.24241 | 2026-09-16 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1411c405-ea88-3faf-99db-da49d5ec52d7 | -3.7739 | -51.35 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73f9f69f-f275-33ed-a476-77aca3d35cb1 | -1.28348 | -55.71471 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6204fdbc-f80a-30f6-b80a-7b454299045b | -7.86026 | -55.45584 | 2026-09-16 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 94493f69-9825-3729-b295-ad28decd5889 | -3.70878 | -60.62184 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e310aac-f5ba-30eb-88ce-86af20c1149b | -6.10836 | -55.66591 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a52cc027-9ee8-3270-af46-23d2e90085da | -6.34802 | -62.69798 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b90195bc-0966-30c6-ab87-38b9adf6ccfa | -2.5779 | -55.99975 | 2026-09-16 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbf2fcc8-ec12-3e02-9aac-0800c128b316 | -5.0743 | -56.24475 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71e37845-8cce-3ec1-9bfd-d4fbcbf2a9e0 | -5.60634 | -44.84986 | 2026-09-16 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8331229-85d6-305b-8ab3-0d10c2433803 | -2.6089 | -51.21787 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7978357-6ce1-39af-ad95-aa8a95a845de | -4.28606 | -48.0403 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69ca6800-5745-300b-b6a2-db992f2cc3de | -4.37617 | -55.02494 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3a38b0c8-250e-365f-b716-5b655a98d54a | -5.84003 | -52.05513 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fc94080-d82a-3305-8dcb-04da8ae66028 | -4.36072 | -47.77729 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fba57592-d740-3e1f-9601-53b8afea2590 | -7.61269 | -57.60921 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
