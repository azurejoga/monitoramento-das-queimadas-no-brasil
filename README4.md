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
| fa1d415f-3cd6-3b5a-9fef-17b78f4ba8c6 | -19.497499 | -44.168201 | 2024-10-10 00:16:56 | METOP-C | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 17eb3d38-8b32-3394-8752-35f42ca06595 | -19.499701 | -44.180099 | 2024-10-10 00:16:56 | METOP-C | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 020e858b-d73f-3d37-ab85-a30daabb91b0 | -18.7486 | -43.812099 | 2024-10-10 00:17:07 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 83d7d21c-d640-37e8-b950-f7809e10ffdb | -16.982 | -45.282101 | 2024-10-10 00:17:41 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1ed1553e-494b-38b7-b92b-6215f3a884f9 | -16.9844 | -45.294899 | 2024-10-10 00:17:41 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3cd2ca98-8ad7-318b-9e61-9beaf735c412 | -4.95151 | -42.99438 | 2024-10-10 00:18:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 67c9fe4e-8ef7-3b53-9758-46b033b76c0a | -4.94972 | -42.98069 | 2024-10-10 00:18:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 916d6f19-4b14-324e-ad3d-5301ab5118bf | -4.94904 | -43.00042 | 2024-10-10 00:18:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| e4388242-024f-36d5-a638-fd1074dffaeb | -4.94714 | -42.98671 | 2024-10-10 00:18:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 779a7db0-d82e-3bec-9295-21d3939b59e6 | -4.44374 | -42.90734 | 2024-10-10 00:18:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 4b764b86-893c-321a-8a2c-38da53a2af1a | -4.43305 | -42.90884 | 2024-10-10 00:18:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ad30ac55-5e6f-337b-ab12-5783925ec75f | -4.24881 | -41.93164 | 2024-10-10 00:18:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 5f731307-8a08-3add-9ed0-9c2104bccd6d | -4.24881 | -41.92585 | 2024-10-10 00:18:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 52c9e084-5d05-3308-af3c-03cc2ceabfd8 | -4.2473 | -41.91452 | 2024-10-10 00:18:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f18274aa-5606-3e24-b759-8f1ddfbdf5bb | -4.24723 | -41.92031 | 2024-10-10 00:18:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| c9302b21-3a88-3f6e-9276-8f935fe8ceec | -4.14885 | -43.00611 | 2024-10-10 00:18:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 0a86358c-7fbe-34f2-af7c-80e341eee044 | -4.14704 | -42.99259 | 2024-10-10 00:18:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 57e67027-45c8-3524-9e74-2200a3676717 | -3.61745 | -42.75841 | 2024-10-10 00:18:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5348c993-0fa8-3e60-856d-68f008d72df2 | -6.25521 | -42.51971 | 2024-10-10 00:18:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5f687e1d-48d1-33b9-ac06-84ebc4bcc85f | -5.87871 | -41.96733 | 2024-10-10 00:18:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 91f317c8-7e72-385f-a4f4-bb68912f78b0 | -5.87708 | -41.95534 | 2024-10-10 00:18:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 976602f4-4874-3746-b295-7366f564850d | -5.8685 | -41.96869 | 2024-10-10 00:18:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 774635fd-9725-32d6-a7a5-e7dcc0b76247 | -5.86688 | -41.95663 | 2024-10-10 00:18:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 96a176c3-e7ef-378b-90ea-7ecc31d8f127 | -5.72217 | -42.32664 | 2024-10-10 00:18:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| eaadbfae-9953-3dd1-9502-0887e938deb8 | -5.58234 | -43.26204 | 2024-10-10 00:18:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0c392817-818c-34a7-9a40-811e8e6bc5bb | -5.58041 | -43.24757 | 2024-10-10 00:18:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e12f6f23-f8f8-35b8-93bd-0b1b5f747ba2 | -5.49868 | -42.8004 | 2024-10-10 00:18:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c4b78b67-207d-3f02-ad71-f43598214eae | -5.48611 | -42.78833 | 2024-10-10 00:18:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| ce160a01-4eec-34cc-a3ab-2415faa7e2f5 | -5.48432 | -42.77471 | 2024-10-10 00:18:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| cb3cd30b-f4eb-3afc-9456-a76b547384cc | -7.83015 | -42.47101 | 2024-10-10 00:18:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 147fc174-0a17-36a5-b3f2-736576173e8a | -7.8284 | -42.45738 | 2024-10-10 00:18:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7392dbca-c1fd-3098-92dc-39ab9cf53a36 | -7.79684 | -43.09969 | 2024-10-10 00:18:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 4f0f6d27-8796-3341-ac88-8d0c6207331b | -7.79447 | -43.09346 | 2024-10-10 00:18:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 3c03895c-7957-3c3f-96da-65225ae52e3d | -7.69161 | -43.00421 | 2024-10-10 00:18:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 3a99473d-1417-36f8-a011-126d6b2e90c4 | -7.69119 | -42.99402 | 2024-10-10 00:18:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 1d06392c-4f61-381e-91cd-dcd4887f9924 | -7.68965 | -42.98849 | 2024-10-10 00:18:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 44.9 |
| 2991a341-2fcb-3cca-8836-d739ffeb10f8 | -7.61725 | -42.41352 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c60dbd88-9f0e-3117-96cb-e49947a18995 | -7.23163 | -42.3026 | 2024-10-10 00:18:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 698307e9-b283-31ea-9603-17f8d7f1491b | -7.22096 | -42.30406 | 2024-10-10 00:18:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| a8819a6a-49f7-349d-abda-4559bbeaaf31 | -7.09491 | -42.63152 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e7675045-8e77-3840-b877-bcc967ddb186 | -7.09109 | -42.62355 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 89e402be-4fae-3233-b680-404eba8385b6 | -6.72162 | -43.55608 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2b811137-f3b4-303a-b46b-9d106f87470a | -9.30825 | -43.35338 | 2024-10-10 00:18:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 41.5 |
| b4e8008e-bb6f-3825-93fb-7667ca7ee420 | -9.30161 | -43.34749 | 2024-10-10 00:18:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| f7deb433-6ab1-3406-b569-ddbd79163666 | -8.15755 | -42.9755 | 2024-10-10 00:18:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 4ef6f60b-e2f1-30bb-80cc-ba8b9aa9a8fe | -8.15564 | -42.96021 | 2024-10-10 00:18:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 9a2b3add-1ee9-3ef9-ab7f-f32047653706 | -8.14625 | -42.96756 | 2024-10-10 00:18:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 63789ca9-dda5-3c8e-85ab-bba570ac4fdd | -8.14611 | -42.97692 | 2024-10-10 00:18:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| c9d91167-5df1-3514-9b90-b437d0e33177 | -8.14422 | -42.9617 | 2024-10-10 00:18:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 3078a5a4-e881-350b-abae-b8c153009176 | -3.4617 | -44.28136 | 2024-10-10 00:18:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| b42df26e-067d-33ba-9238-2aab9649bd94 | -3.45917 | -44.29272 | 2024-10-10 00:18:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 91ab23df-a452-32bf-b23f-adbc3f48aaa7 | -3.45704 | -44.2764 | 2024-10-10 00:18:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| f8bba8b1-ebba-33bc-b798-f3ccb2edfc78 | -3.29918 | -43.51754 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a0e1876e-1dad-327c-9f1c-563d11973cdf | -4.32098 | -44.61421 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| edaa74ce-16ea-3f98-b90b-31ac49fd60ae | -4.29732 | -44.39714 | 2024-10-10 00:18:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b5bf2e5e-3159-37d0-91c3-2587f73e66fd | -4.29509 | -44.37994 | 2024-10-10 00:18:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| cbadc7a1-14d0-3717-b617-0a6b268e0f1c | -4.28998 | -44.38709 | 2024-10-10 00:18:00 | TERRA_M-M | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 4c359680-d293-3346-9d11-8251dae93524 | -4.0411 | -44.26132 | 2024-10-10 00:18:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e249c356-d9d7-3a80-9037-e64e98bce0d0 | -4.28162 | -43.14732 | 2024-10-10 00:18:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a245e7c1-8ae9-3b01-8682-a724127e36d4 | -6.00291 | -43.48965 | 2024-10-10 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c1e40eb7-9168-3922-bb8e-be35b8115cbe | -5.99141 | -43.49112 | 2024-10-10 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| aa8afd0c-c372-3798-9ee4-fb67ea14063f | -5.98932 | -43.47544 | 2024-10-10 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a939c73f-74eb-39fe-a746-af2cccf979e5 | -6.35436 | -43.82735 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e04b0a1e-7cda-35fc-88be-18a3e2e76656 | -6.3523 | -43.81128 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 69364bcd-dff2-357b-8f94-f70257320fb4 | -6.34603 | -43.81749 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 95ff7b44-f799-32fe-96e8-b633f1f9b034 | -6.1686 | -43.71363 | 2024-10-10 00:18:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| cf364b81-c425-37c5-a45c-d7397b516fea | -5.85402 | -43.74744 | 2024-10-10 00:18:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e452589c-3638-3791-ba8c-f8e2c51fc296 | -6.189 | -44.38538 | 2024-10-10 00:18:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3de64155-ea9d-358a-8a33-111033390c77 | -5.94818 | -44.74334 | 2024-10-10 00:18:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 2a59ddbe-3e05-3995-a696-05f7e4a38b3c | -5.70624 | -44.79288 | 2024-10-10 00:18:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 77f653a5-2be2-3ba2-b313-61abf02a24b8 | -5.49307 | -44.28794 | 2024-10-10 00:18:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a39fc6d7-e75d-3a6a-82fa-7222fdbda224 | -5.49015 | -44.54485 | 2024-10-10 00:18:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ee59e749-ae2a-3f31-aa0d-a91f4667e87b | -5.48769 | -44.52639 | 2024-10-10 00:18:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4fc0a31c-cd1d-30fe-8e23-dd7e0f3d53dc | -5.48739 | -44.30111 | 2024-10-10 00:18:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 45cf8ca0-4685-3c22-bda0-26a4f91c8f3c | -5.48512 | -44.28337 | 2024-10-10 00:18:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8034b313-b247-3ac1-8662-2c72b718ede8 | -5.48089 | -44.28948 | 2024-10-10 00:18:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 514514ac-7b22-3323-ba82-cfc726282c67 | -5.23515 | -44.78876 | 2024-10-10 00:18:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ead4a2d3-93ef-37b9-84c8-f392ab5b7f91 | -7.63246 | -45.27618 | 2024-10-10 00:18:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ef27b8dd-44c7-351c-af9a-52d9a20000cc | -7.31211 | -44.98022 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 79d76eeb-253b-3e8f-914d-bdea22a99bbc | -7.31075 | -44.99575 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a4eebc0a-00d8-3f19-a092-1ed82092c519 | -7.30811 | -44.97421 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 6abaec83-fb25-3138-a85e-4b847760e6f0 | -7.29882 | -44.98183 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b4ff9972-2a78-3cd1-85ee-646ea923f351 | -7.29482 | -44.97582 | 2024-10-10 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a8feb9ac-8d35-3639-aabc-f132b7cc32ea | -6.51331 | -44.35699 | 2024-10-10 00:18:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8d8b497e-b2d3-3624-9f35-d432ebfae4f0 | -6.51095 | -44.33837 | 2024-10-10 00:18:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b1f8c0a9-5c34-364d-8d62-eb521ede6c85 | -6.50888 | -44.34513 | 2024-10-10 00:18:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| ac82f381-5c89-3976-886e-750fcb6c40b8 | -8.13435 | -44.47724 | 2024-10-10 00:18:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0cd9535f-30d8-3849-92c1-3e3b7714eb55 | -8.13183 | -44.45744 | 2024-10-10 00:18:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 4fc97aae-d3f2-3d3f-9ffb-b585634fa482 | -8.00411 | -44.37596 | 2024-10-10 00:18:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 3deb8948-438c-3e83-82a9-a68fb48b8a3a | -4.46799 | -45.90156 | 2024-10-10 00:18:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.6 |
| e48cae6f-f407-3014-8258-485e077dd66a | -4.28188 | -45.47503 | 2024-10-10 00:18:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ec1170a1-2b50-3d69-999d-cbd443a4cb3f | -4.28159 | -45.48966 | 2024-10-10 00:18:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 35.6 |
| e51d5292-a500-38df-93d3-9ae33b0c84a0 | -4.27887 | -45.4688 | 2024-10-10 00:18:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| ea97a7a1-912d-30fc-b0be-a805cb46881a | -3.81487 | -45.51923 | 2024-10-10 00:18:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 517f6902-db46-3264-9749-3a1c82169aae | -3.81469 | -45.50352 | 2024-10-10 00:18:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 182.3 |
| 4c192534-1ac2-3e65-8c0e-bd21ce3a85c1 | -3.81217 | -45.49845 | 2024-10-10 00:18:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 319.9 |
| 799fa511-625d-3abb-81ca-2834986ffaa1 | -3.81185 | -45.48291 | 2024-10-10 00:18:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 1c803f6b-ea5c-3ce1-9664-1ed8cce01c8e | -3.80162 | -45.50526 | 2024-10-10 00:18:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 4f0f23d9-465e-3335-aed3-7a287c4d4125 | -3.79909 | -45.5002 | 2024-10-10 00:18:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 32ff78bd-3b65-376a-95eb-c89e0e8d7f5a | -3.7988 | -45.48466 | 2024-10-10 00:18:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |


[Clique aqui para ver as próximas entradas](README5.md)
