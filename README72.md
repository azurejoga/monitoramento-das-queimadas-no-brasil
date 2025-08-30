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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b58029b4-d647-3a19-8a97-d196ea23af8f | -15.219 | -53.80206 | 2025-08-30 05:12:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d115cfa1-f538-3e2d-a465-9b1cf94dee0f | -14.5927 | -54.49203 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15b90215-450f-358a-9a09-57c9f49e2a89 | -14.78562 | -59.73603 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 750cbf13-d702-386a-99f0-a177dadfbb3d | -15.21796 | -53.80981 | 2025-08-30 05:12:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b734b93-aaad-3bb7-9366-b9feca696abb | -14.79129 | -59.70024 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4a5ecac-e9a1-3920-8b2c-ff28aad01890 | -14.62843 | -48.07852 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c09f08e0-f7e6-3351-8dc8-05f5346101c8 | -12.422 | -63.91165 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bad0a9a-2014-34e3-8b5f-757b96ef9fee | -14.79242 | -59.69309 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5da78be-86a9-3701-a142-5b70677c2007 | -14.59694 | -54.55088 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 496d0349-f93c-3cc9-9ff0-109a3587d15f | -14.75236 | -55.4191 | 2025-08-30 05:12:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8532ae04-a8eb-3980-80a4-2a2b9b360898 | -14.49605 | -52.05217 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80e44b50-ee9a-328d-9355-5a4756764488 | -14.62447 | -48.07577 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0733ad5d-3485-3128-8412-def4b5b072e6 | -12.43681 | -63.92181 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 75c175ac-1e17-3257-bf54-7c605b47a0a6 | -16.53074 | -55.0447 | 2025-08-30 05:12:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cf256020-2689-3294-acbf-b341c4aed521 | -14.11081 | -51.77952 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64faf9bb-1972-3016-9624-e67d1bfd0435 | -14.45977 | -52.0153 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed97edc4-6f67-3731-a0c6-ec9d4366cf50 | -14.3183 | -51.87201 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f75f214-4784-36d4-964e-021b9d953cbb | -14.32638 | -51.95975 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ada41756-6b0e-3807-b34c-8f632da71795 | -15.76783 | -47.76744 | 2025-08-30 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26bb6972-675c-3b68-a1dc-6a839578dc74 | -14.62256 | -48.07629 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a85ca6c0-53bf-3797-8942-8d7c3e8f6ee7 | -14.59792 | -54.54929 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6767b8c2-9b45-3138-afac-95dda7cc6b4b | -14.78619 | -59.73244 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8467395b-a10a-3e88-88fb-8a356e8d8e43 | -12.22433 | -64.22316 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc9ab3a6-f2cc-38ab-9c02-5f8bcebbc3a9 | -15.58726 | -56.02294 | 2025-08-30 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd8dcadd-b27f-398f-bb13-ab4969925ec0 | -14.77785 | -59.74205 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1943d05-631e-34b6-9771-37eae1ad8a71 | -15.18725 | -53.78544 | 2025-08-30 05:12:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78ba2e62-e0c7-39e0-bf6f-237b7e6012f6 | -14.61608 | -48.07956 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e25460f1-16c4-3a5b-8c6d-5206e55b2a96 | -12.42878 | -63.9203 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0647b944-685f-3133-b363-8532c0411e20 | -14.62919 | -48.07174 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7476209c-ee12-3aa6-b42b-7b122b17206a | -14.61551 | -48.0846 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6adae06a-1b62-355f-9a48-784303bb2bd7 | -12.43003 | -63.91315 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0adb72f-6107-3196-9266-ec7c1b0f3b63 | -14.49919 | -52.99221 | 2025-08-30 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8310818-f824-30c6-8afb-2b93a7bf4f87 | -14.49866 | -52.99633 | 2025-08-30 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 291cb223-632a-3ec3-8a25-50b731bb4087 | -14.59437 | -54.53999 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75b099a1-0d6d-3980-bc32-7d717893df98 | -12.43279 | -63.92105 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f8b567f-55a1-3cd6-b123-99e9570917df | -15.21848 | -53.80594 | 2025-08-30 05:12:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a299d906-c939-32cd-9f8b-6639f460c41b | -15.18776 | -53.78157 | 2025-08-30 05:12:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1094dedf-4801-3409-87b3-61fc8b52c825 | -14.77066 | -59.74448 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b39a83c-601b-3815-ad39-698ac62bdbd7 | -14.79186 | -59.69667 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d741c211-1a19-3400-85cb-cfd1d55c74e2 | -14.10611 | -51.77888 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b36f55e-a506-3be4-b9f5-bad202fc1523 | -14.3488 | -53.3241 | 2025-08-30 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42fc5896-dd3d-394e-a478-530ebcb34282 | -14.50936 | -52.05901 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 586ae5d9-13b8-3b2a-a283-d4c023e81937 | -15.20576 | -56.05973 | 2025-08-30 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f595ab0-7d69-33fe-b22e-82418a0723fd | -13.39801 | -57.07108 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69568746-9edd-3eaf-a241-a1b5f8fe1e35 | -15.76156 | -47.767 | 2025-08-30 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baae2199-731a-353d-a696-5cf8888fe13b | -12.42602 | -63.9124 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4083e1ba-c760-381e-97bf-5d40dbafeff9 | -16.58355 | -54.65115 | 2025-08-30 05:12:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c2f6d85-de17-3ab7-bc6f-30834b5e2cff | -15.01867 | -59.91428 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8287750c-f585-3ca4-a5cb-7962a14b4258 | -14.78174 | -59.73905 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 356115c2-d6d9-308d-abda-5efbb0119f5f | -15.20942 | -56.06023 | 2025-08-30 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5bfaebca-4301-3c20-b186-67c645d26f28 | -14.31945 | -53.09464 | 2025-08-30 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1e98f8d-4325-39c7-8fa5-e83874f5ae64 | -14.50788 | -52.9935 | 2025-08-30 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f7a8569-9b03-30d0-9948-4e9fabb9bfaf | -14.62881 | -48.07514 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19e2cd81-acf4-33b3-b331-6dcd90cdc10a | -12.42539 | -63.91597 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df55de47-de46-3dcd-9a67-4efbb57e4929 | -15.20512 | -56.06421 | 2025-08-30 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 697b3591-e388-3616-91a3-1a3b51adef8a | -14.31362 | -51.8713 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80a1d12c-09ff-3fa7-a847-1fc91d648b1c | -12.22367 | -64.22687 | 2025-08-30 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9975e938-1849-35ed-bcb5-8243f10a67b4 | -14.45851 | -52.02518 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7798ac7a-00cf-3950-aafc-d166f03e090d | -14.5947 | -54.54358 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 099a8fcd-db2f-37b7-8807-acff44ff197c | -15.10472 | -48.16744 | 2025-08-30 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9efa78c-7bb0-3eb7-9bd9-13fb4e363d6a | -14.59335 | -54.49573 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eed906e4-af54-3503-ae65-9d726234518b | -14.79508 | -59.71923 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 047f96df-1ae4-37ec-8b42-fd570c045048 | -14.79953 | -59.71265 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96cbba1d-0d8a-3d3f-a7fd-61643bc66e6a | -16.57953 | -54.65052 | 2025-08-30 05:12:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98313095-eca2-3538-a07a-21c3c27c162b | -14.34508 | -53.3194 | 2025-08-30 05:12:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e12504a0-d534-3720-aec4-289681228817 | -13.43739 | -57.18193 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30db590c-37eb-315f-9e8a-ac5476481b19 | -15.10427 | -48.17165 | 2025-08-30 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fc8a224-5a19-384c-9612-fe499ee21caf | -14.33919 | -51.8954 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd5d5032-7e42-3d69-8b8b-3f111dbcb122 | -14.59663 | -54.49272 | 2025-08-30 05:12:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed18fadd-0cdc-3b41-a9e6-563a49c5de3e | -15.84425 | -56.1841 | 2025-08-30 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| d6692fed-2d70-34f1-bfe2-3ecee687a49b | -14.63076 | -48.07414 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 773b871c-42f9-3bb9-b351-64de6c76c009 | -16.58307 | -54.65479 | 2025-08-30 05:12:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d52b7f7-2f9e-3db1-9036-5cd6561375f1 | -14.78231 | -59.73545 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33a4b037-22aa-3102-ad0f-73a7d496db91 | -15.03441 | -57.18869 | 2025-08-30 05:12:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e5950dc-3167-3e95-824e-f4d6a35f4094 | -14.50238 | -52.05116 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd7d549e-64c7-3706-adaa-dc5cf50a33a0 | -14.62214 | -48.08002 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 04a94c0a-bb46-3b3b-bda5-79e67a790ec9 | -14.7895 | -59.73301 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea5e36c5-f082-396f-beae-91ff9439fb5e | -16.40593 | -45.65664 | 2025-08-30 05:12:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 301d1d66-f96f-3e79-bbe4-cb1dc513d5b2 | -14.49141 | -52.05155 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b67427fb-7628-3afe-806a-fd3d244fb40b | -14.4931 | -52.0499 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 58c89c27-b803-3383-b808-fc47425a2078 | -14.8001 | -59.70908 | 2025-08-30 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d52df5b4-f6f7-320d-a375-9d51a97ac492 | -15.21953 | -53.79817 | 2025-08-30 05:12:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eb1ac5d-be59-37d4-8121-c3539321c946 | -14.62483 | -48.07231 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe4b9a8a-68df-3dfe-a1b1-21741fc913f1 | -14.62295 | -48.07278 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b09b6e8-9609-32c3-ac1e-4094ed8dadf7 | -15.60904 | -56.31615 | 2025-08-30 05:12:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ba58d01-6faf-31ef-86d3-aba2a38eff76 | -13.37032 | -46.99928 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bf7418f5-2181-3afb-822e-356cc2204fd1 | -13.47366 | -46.95951 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 344c4caf-0073-34d2-9510-727a160035d7 | -13.36841 | -46.97669 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b239187-ca48-3b32-ac30-cef00997b6fa | -12.9459 | -48.12649 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b521446-4c43-35df-a8b5-599f05a11eba | -11.29921 | -63.25916 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 289490a3-f61d-3f3c-8909-95d75254edc1 | -9.7762 | -64.2569 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5afeb99-abd6-333f-9391-034b60b04ccb | -13.62695 | -48.18806 | 2025-08-30 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c3b4f3b-4baa-3bd6-8d6d-f0d4947718ba | -11.74195 | -51.75248 | 2025-08-30 05:12:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d687664e-cad3-3f0e-982f-7329fc1e7e44 | -13.36467 | -47.01191 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6aa7af9c-0c5d-3dd1-9531-2adb1d5ddca2 | -12.6349 | -57.00636 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40878048-2ebd-3c74-b0d8-060761706fb3 | -9.67673 | -65.02155 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0bbece32-258c-33b4-a07e-2fad71d769f3 | -12.63434 | -57.01013 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48ede63c-4f49-3b65-a3ec-1c4e62d5df0d | -13.46721 | -46.95931 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1febaf0-93de-30e7-9362-b622b7bf890d | -12.82594 | -48.09386 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0e2a9c3-b312-37bc-a465-18ee52648ae9 | -13.37906 | -46.97911 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README73.md)
