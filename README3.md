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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 433cd995-5d7f-341c-aa51-b023db1d7aea | -5.03896 | -45.31275 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 32cf5a18-bb56-3fe5-a81d-14e7c2669adf | -7.01751 | -44.96373 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 3cbc5619-6bc5-30f1-a165-183973e2cbc5 | -10.60492 | -44.33126 | 2025-09-07 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4f4442f6-a575-30e3-bd2f-0dc378d9d25d | -11.61037 | -47.16926 | 2025-09-07 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| b13ff451-31a9-322c-b0e3-7375946d9e41 | -5.70718 | -43.94112 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8ff3d397-e079-3d3d-b442-03f72fd2c378 | -6.22941 | -43.31267 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ebeea1a7-4370-335d-b0be-2e0ebaa572c7 | -5.75784 | -45.52914 | 2025-09-07 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c50f576-752a-329d-82ca-ec3706f7b860 | -6.19122 | -43.37785 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3f1c5392-4eb0-3b26-90fb-08f2a0bb1c4f | -4.17702 | -42.02577 | 2025-09-07 00:11:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 88e51909-a2ac-310e-9116-58c669504e93 | -7.23404 | -43.84922 | 2025-09-07 00:11:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a4a78279-8b9e-3f5f-9355-ea142bfcd2f5 | -6.88049 | -45.59789 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3de6c180-4a94-3558-84b0-51df9a8ac831 | -6.21641 | -46.76274 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8ef3a3b5-0d9a-33d2-b247-ad805e009652 | -5.83303 | -43.97434 | 2025-09-07 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b550c2ac-2a07-34e0-95a8-a13ecffca7fb | -6.86622 | -44.26108 | 2025-09-07 00:11:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5b51d33a-3be4-39d0-aeb2-5dafbe394af1 | -6.20286 | -43.59164 | 2025-09-07 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a9b48559-7208-33d4-a8be-56edc2738a95 | -6.30474 | -51.42636 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 589a2c9b-1531-3084-be6f-7e06869b22f4 | -6.59938 | -43.98997 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 6265b86c-a3fa-367c-8b5e-96d3491e4f4d | -5.83377 | -44.12534 | 2025-09-07 00:11:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 78b83f08-c2d6-3e4b-914f-37abce688611 | -6.26383 | -43.49635 | 2025-09-07 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 273bd0ff-90af-3d7b-b72a-f2200e0335aa | -6.21237 | -44.39545 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8ce85d57-96f7-3d3d-bf45-9c4735ca4820 | -10.77598 | -46.03054 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 087110b8-dad4-343b-ad59-8d29db0869bc | -11.27358 | -46.41164 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f67314e3-357f-311c-8452-da2fb467ad65 | -6.23577 | -43.29379 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a85af0e5-1752-35d6-8394-f5b64afaa2a4 | -6.21251 | -42.466 | 2025-09-07 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| e6eee74c-ef57-396c-a9f3-4a4084670bc7 | -7.29042 | -42.52122 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a17ca261-2e74-3705-bdec-759bac75dd05 | -9.73982 | -48.9716 | 2025-09-07 00:11:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 20dfa0ce-80cd-3436-96af-48323465d59b | -6.20855 | -42.63162 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6fcfa0e5-5cc7-3b06-baf8-89644922345b | -10.34155 | -44.90372 | 2025-09-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 13805f56-43bd-3b32-95ec-bfa10433ae31 | -8.70953 | -47.86666 | 2025-09-07 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9cc84973-8148-303c-ba9e-bb62d2c1d2af | -8.9187 | -45.80961 | 2025-09-07 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 543a77f8-fbe1-39f9-abc3-22c62ac3d520 | -11.27527 | -46.42482 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8ae19f70-0a61-31b3-b0c5-254a44f1bc5c | -10.38517 | -44.97607 | 2025-09-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 6608e63c-b6c4-331b-8599-341c3f7e1d17 | -6.58806 | -43.97326 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cca72e82-60fd-32f1-86e1-badcc1d9c8de | -7.62902 | -46.55386 | 2025-09-07 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 709ea963-fc5f-3316-931e-6873227b8c86 | -6.32245 | -42.1967 | 2025-09-07 00:11:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 5b3e3dff-c292-34d7-a83d-781b4b92c56f | -6.24336 | -43.28373 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 49bbb4d2-811a-39bd-9f3e-b8c89a21839e | -8.93327 | -48.66548 | 2025-09-07 00:11:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a5e71aa9-8370-3801-a4fc-28979f1be07b | -6.52699 | -42.93077 | 2025-09-07 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 85dde73d-07b9-324e-a35e-c331e65a4b3f | -8.68086 | -47.45769 | 2025-09-07 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 42f4f557-48f7-39f7-8bce-5e4fad254ab0 | -10.73797 | -44.35673 | 2025-09-07 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3fe62de9-6d19-3bf4-8462-d5834318d9ab | -6.38935 | -43.00778 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a882f338-a544-39d1-a5e3-e0a8281f1851 | -11.26071 | -46.48016 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 120d4a82-911f-3cd5-97a2-ceb729c7bd1b | -9.97414 | -46.80363 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 5f998193-ffad-3d07-8297-21b3cfd843dc | -11.85469 | -50.55315 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e5b0f56c-68bd-32a3-886e-895f7d83a79c | -3.78816 | -44.51908 | 2025-09-07 00:11:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a1f0b367-f65a-3373-a5b9-8f7ff837efee | -6.00258 | -44.14403 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 668e1c4d-5acc-3ef2-bfc4-2dd545355d15 | -6.23455 | -43.28498 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ff49bafe-3e15-38a2-a952-8723f2bb950d | -6.1481 | -44.25736 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a7cfa929-18ed-3623-9d98-62f85e847bf1 | -7.67834 | -47.33219 | 2025-09-07 00:11:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 7ee97eec-a448-32e6-ace8-a3ab34cbcd15 | -7.43898 | -44.953 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d21e37c-6a4d-31d6-9b47-c9cdd8f95a30 | -7.63901 | -46.55837 | 2025-09-07 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 41cfd4b7-7760-3a34-9fff-ee514db63e4a | -8.93103 | -48.64712 | 2025-09-07 00:11:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 49.3 |
| cd0701bc-2862-3660-90cd-4c3b430585ed | -11.25905 | -46.46699 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 047db163-d03a-3a65-a1d1-159e2b565c7c | -6.17841 | -45.42664 | 2025-09-07 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e55dc81d-aa36-3749-87dd-9257ad32dc9c | -10.78215 | -46.01171 | 2025-09-07 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8e136ad7-227a-33e0-920c-cb7b51e9a77e | -6.34056 | -43.79133 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f0e0dc38-8ca9-37c9-af1b-c01b981c9d59 | -6.07831 | -43.55275 | 2025-09-07 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90d22d34-760e-3a7c-9aeb-e561ca7b61e9 | -6.22696 | -43.29504 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 313e4925-dde2-32d2-aecc-f83e7d148f27 | -7.76378 | -48.82259 | 2025-09-07 00:11:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1320b24e-b3ee-3825-a26e-f3718ab13e21 | -5.79373 | -45.65572 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f98c0495-30d6-3f4e-8900-3aa7b0a2b22d | -6.23779 | -42.5817 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 54fac07c-c27d-31ac-9b27-3505ed9fcc43 | -6.19406 | -43.5929 | 2025-09-07 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a3eecdb8-2ab6-3cbc-865b-3537d203bc04 | -5.40644 | -44.83198 | 2025-09-07 00:11:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ac998321-dc89-3dec-97b5-5ecb7cb94f9d | -6.22954 | -43.57304 | 2025-09-07 00:11:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 41c860ac-7910-38ec-8c16-6d78294929f1 | -6.18878 | -53.26061 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 5a982ab6-1383-319e-a59c-aa949db545c1 | -9.71064 | -49.47876 | 2025-09-07 00:11:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| fb1e833b-3d43-34ae-8b5e-0aae01c6c51e | -4.25858 | -48.55154 | 2025-09-07 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5d78c0e3-9ca6-3e48-a318-8f5a2ab65f96 | -5.8661 | -46.05183 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 96608c2f-9840-3700-bac3-8ad06fbc6c4c | -6.19968 | -42.63289 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| b3db7c46-1565-3d0d-823f-40ba15f0c0b6 | -7.75382 | -48.84174 | 2025-09-07 00:11:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 63b84f12-075a-3da5-b8e7-d6b71edf63f6 | -7.74495 | -48.81338 | 2025-09-07 00:11:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d77a69ea-1b19-3f73-a1e8-3ad0034fbabe | -5.83254 | -44.11643 | 2025-09-07 00:11:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ddd85f50-f0b2-3dc7-a532-ce8d87d108d6 | -7.4377 | -44.94338 | 2025-09-07 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d1cc9294-6617-3326-b753-c1b9d4770a2d | -4.48682 | -48.1127 | 2025-09-07 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a8d04057-7c43-35c8-a3c3-1eebb16cd6ec | -2.89664 | -40.25425 | 2025-09-07 00:11:00 | TERRA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0ac10de7-b689-3a1f-abd9-8838fe2476f4 | -7.92721 | -49.30143 | 2025-09-07 00:11:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 86a25108-25bb-31f1-80d5-8fd419af0951 | -10.61544 | -44.3398 | 2025-09-07 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9551a3e9-cd07-35f4-9cef-a8c271989d16 | -6.27264 | -43.4951 | 2025-09-07 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a2f96ed2-9082-3e86-b948-c387ec346194 | -5.48948 | -45.91718 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6719fe6c-e509-397f-bbf2-fd2bf4ce9f85 | -6.20981 | -42.64059 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| adecf1da-22b4-3177-bbee-5d4f2ad0fb6a | -9.71324 | -49.50014 | 2025-09-07 00:11:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| d818cab7-d031-3fa2-bb5c-a60b84c83179 | -4.8647 | -45.66282 | 2025-09-07 00:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2fcb4bcf-1bfb-375e-abaa-4529c8b68dbf | -6.10388 | -43.2016 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3a21e60d-74e3-3667-9351-4ecd0365aff8 | -5.97721 | -44.1567 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 145121f7-1739-30db-bd3d-b1791716214f | -6.18769 | -45.42533 | 2025-09-07 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| e25d8686-3f9f-3a59-ae97-6d2c3bb566aa | -4.1692 | -42.03664 | 2025-09-07 00:11:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9695ed57-d833-3510-b7aa-17c499d1a330 | -6.19842 | -42.62397 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 59313c7e-225f-3547-abde-2f001f8f5d4d | -4.27658 | -48.18699 | 2025-09-07 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| da60222b-dbf0-31eb-8c1b-0ae73f04da41 | -8.04487 | -44.04775 | 2025-09-07 00:11:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08e421a1-073d-3ce7-b6a6-5978a5646b5f | -8.71153 | -47.88213 | 2025-09-07 00:11:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a49ac358-23fe-3eec-96f9-a983c1df329b | -6.61711 | -43.98754 | 2025-09-07 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 04c4bc12-19be-3f6e-abf8-c25c5eb6525a | -6.60152 | -48.05276 | 2025-09-07 00:11:00 | TERRA_M-M | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0500b1dc-a5d5-32de-a5ec-715afdc58f7f | -6.41685 | -44.40993 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 475d2d37-a9b1-32de-8cf0-182889ce8570 | -7.33852 | -48.51022 | 2025-09-07 00:11:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 724deb25-c175-321d-bbc2-5032944c6130 | -6.13798 | -44.24951 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9d4955c6-e05f-3c4a-b95f-26f66acf76f2 | -6.16465 | -44.24584 | 2025-09-07 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 29fb9656-0495-34f3-a45e-acde4f4e580c | -6.88313 | -45.54541 | 2025-09-07 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f4972f3d-88ae-3570-9c96-1a7d95865913 | -5.6029 | -45.79172 | 2025-09-07 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ccb04088-f1b7-3ea7-b1be-00e6113b9e14 | -5.99863 | -44.181 | 2025-09-07 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 227cbd9e-63dc-3363-9bd4-9d38398510ad | -6.21994 | -42.64827 | 2025-09-07 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |


[Clique aqui para ver as próximas entradas](README4.md)
