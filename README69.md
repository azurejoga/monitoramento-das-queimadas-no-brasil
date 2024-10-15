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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f66a9afb-bb49-3861-9a99-9471492713e6 | -10.94082 | -54.09575 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3302689e-2b05-35dd-8298-24375bd32276 | -10.94027 | -54.09926 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dd1a4f7d-a226-339d-ab9c-afc9faac83d2 | -10.93971 | -54.10278 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7d6a229-82e0-39c3-aae0-48c0a6116b08 | -10.93915 | -54.10629 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e28e4a64-879f-3e1d-a7ec-3eeb825182b2 | -10.93696 | -54.09872 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 62d67f99-933e-323d-8134-9772ff2a0e4d | -10.9364 | -54.10224 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc6c3842-65cc-3e81-b8b3-3d7f0ecd6e47 | -10.93584 | -54.10575 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b891962-41de-3fd8-82bd-206e9f175bbb | -12.42105 | -54.18878 | 2024-10-15 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6fcddf2-d82d-3c19-843c-70410bfe2283 | -14.68922 | -56.05005 | 2024-10-15 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee7b164e-8c8a-3c08-98a8-147212ffd348 | -10.80283 | -55.60921 | 2024-10-15 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24a86f37-3dff-305f-bbec-3649b54eaf71 | -10.42934 | -56.4465 | 2024-10-15 04:51:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f42ae748-ab0e-3418-a6ff-ff9ce4c3d02a | -10.1012 | -55.17661 | 2024-10-15 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d4d4eec-9010-3897-a27b-b7ed966d942f | -10.09101 | -55.17492 | 2024-10-15 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae67628e-ad1e-3b8c-bfc8-1848b4795898 | -11.44025 | -55.68169 | 2024-10-15 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bf92cce-f207-313f-9ba5-a56e19cf3be7 | -11.43684 | -55.68112 | 2024-10-15 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6c69ec8-d071-3be8-b325-8e12d25fc72e | -11.43 | -55.67998 | 2024-10-15 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fae9e3e-067a-3952-8bf3-dd8f5d9b5354 | -13.34538 | -56.66516 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e63b47ca-94ce-3761-ab57-e66f2ace4804 | -14.9614 | -57.63033 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb73b00b-a9f6-3628-a671-c3d9b30d38e3 | -14.95854 | -57.62546 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0513038c-2805-3787-b422-7b92199cebd7 | -14.88607 | -57.98745 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a716211-e348-34f9-81cc-920290db31a8 | -14.88535 | -57.99165 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1610aaa7-e4f4-3f53-bc70-bd9437609422 | -14.88244 | -57.98676 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7936fec-4b79-3c2b-8306-8ec163e77987 | -14.8817 | -57.99107 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ab23355-4e6e-3e23-ac73-59dfbdb51aac | -14.86291 | -57.96942 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4aa683ef-ec75-3a55-8048-f26fe3bd2d9d | -14.86001 | -57.9645 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| eb8bc6f1-182c-3e88-915e-a9fdd910ebf4 | -14.85927 | -57.96878 | 2024-10-15 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8bfb1a91-29eb-3c60-865a-1ab6b60b0778 | -9.39193 | -59.44036 | 2024-10-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89385dca-d295-382c-b162-86e4458bf2a5 | -15.17754 | -59.71062 | 2024-10-15 04:51:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e9adf8c-c1c8-39fa-883f-64b2071cb851 | -15.17355 | -59.70987 | 2024-10-15 04:51:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43be3379-e30e-3150-9c30-d41c234b07da | -15.96457 | -59.75751 | 2024-10-15 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9eb8fff-b51d-356c-b732-0ee8fcebdb6e | -9.26236 | -60.87883 | 2024-10-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 208421fa-f290-3593-b07b-3dd51828550b | -9.26145 | -60.88401 | 2024-10-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1289720-f6dd-330c-ba2d-8a7c6a5b0ff7 | -9.26053 | -60.88923 | 2024-10-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 224d5894-2616-3557-8bb4-9ced82fdf6da | -9.25668 | -60.8831 | 2024-10-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7903e1bc-1c3d-3b15-b656-e30341c76a66 | -9.25576 | -60.88829 | 2024-10-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 806699a8-15c0-38d1-99ee-a629e77f7a9a | -9.25192 | -60.8822 | 2024-10-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d74db41-44b3-3250-bbc7-253cb51b2016 | -9.73234 | -60.76309 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d9e19e1-e599-3603-8930-e16e4808db07 | -10.63007 | -61.43222 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0cec2ccd-268f-3304-8644-477a0097bb93 | -10.62522 | -61.4314 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ad1b8fe-cba3-3ac6-b467-8a7190940196 | -10.62415 | -61.43723 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 090fbaf8-728f-3318-aeaa-121c061517b2 | -10.44865 | -61.26632 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73e87c43-fb93-398d-a2b1-2904b823b11f | -10.44772 | -61.27138 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28d29d51-85fd-3005-b1b6-5ec9cb870bbd | -10.44383 | -61.26558 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c17ed487-7d39-3709-b4dd-c3d3b89245b7 | -10.4429 | -61.27061 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc26e447-d65c-3957-9992-5764da95ec0d | -10.44188 | -61.27618 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 441005fc-c0f1-3730-961d-21405f7eadf9 | -10.42804 | -61.02511 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21c921d1-36f8-3a6f-97d6-ce9b62b0f963 | -10.42422 | -61.01925 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c272aa2e-88e6-3ffe-8e6d-b4e1e6d5e241 | -10.42328 | -61.02449 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1908c7d6-7e66-369c-aec8-ec6368e37d64 | -10.42233 | -61.0298 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98337a37-f2ef-3cf9-b8f8-770d2aee3a11 | -10.3773 | -61.19798 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f3afef0f-a109-31a8-9ff7-135a92e754f2 | -10.37441 | -61.18667 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57b86360-6448-355a-ae26-afa84f85afcb | -10.37347 | -61.19185 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b7b1a412-866d-3ab1-8c82-85ec9935573a | -10.37253 | -61.19704 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dbc8d471-1bbd-3135-a44b-560e9c8c0c04 | -10.36964 | -61.18575 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cafa3272-c26a-3695-92d7-68db1279ca08 | -10.3687 | -61.19095 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d53a2399-77d1-3926-abbf-bab87e9349d7 | -10.36775 | -61.19615 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 55733a05-804a-3918-b4a0-5df6aad33e00 | -10.36581 | -61.17965 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d3dba8c6-1141-3e19-983d-4b97b09ab2cd | -10.36487 | -61.18483 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ce398961-4a1b-3e4d-9313-5bf87683bcc3 | -10.36392 | -61.19004 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| da9d18fc-d75f-3969-a2f2-32b8cbfc76ff | -10.36297 | -61.19528 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 26d08f54-bcaa-3e69-9a2f-d585673a52e1 | -10.35915 | -61.18916 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70b25a50-6658-33bc-b4fd-f323e16ec516 | -10.35819 | -61.19438 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 52be7867-7ddc-3ba2-92d6-018ee958382a | -13.37746 | -61.96422 | 2024-10-15 04:51:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 31f90c31-c0b1-361b-ad47-c8664f7b793b | -13.37646 | -61.96952 | 2024-10-15 04:51:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b1509d01-4d1b-3eea-b6ed-dbd096606056 | -13.3717 | -61.96856 | 2024-10-15 04:51:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abbcfe28-e89f-3603-a02c-ca0e18fcab60 | -13.36217 | -61.96661 | 2024-10-15 04:51:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9eec0d8a-c416-3d11-a867-9e9d6a584a39 | -13.35983 | -61.35011 | 2024-10-15 04:51:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 693e3f8e-937b-323e-932d-53df2a912ee3 | -13.36693 | -61.96758 | 2024-10-15 04:51:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d65a5c4e-652f-31b7-8fb3-f276efa97531 | -13.36074 | -61.34529 | 2024-10-15 04:51:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd02131d-c270-3b0b-9a36-543fbf3f0b51 | -9.11303 | -62.63893 | 2024-10-15 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0538d3c7-618c-3236-8af6-aa64c4e8a9d5 | -9.11238 | -62.64243 | 2024-10-15 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 416688cf-41a1-3658-9862-62578cee2e2e | -9.01193 | -62.57088 | 2024-10-15 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22879cb9-2eb8-3625-a621-92f5b9ee8a14 | -9.01129 | -62.57433 | 2024-10-15 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3c99d59-d5fe-371b-b4e1-007f6ebb98b3 | -9.74578 | -61.99841 | 2024-10-15 04:51:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75be5304-5345-3ce0-8e53-03f337b7a47e | -10.00605 | -62.10481 | 2024-10-15 04:51:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 068cd05b-b3ac-367d-abce-6aaa95d5ab9a | -10.00549 | -62.10785 | 2024-10-15 04:51:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84970518-214b-31a3-bdcf-30eb30c0f609 | -10.00494 | -62.11088 | 2024-10-15 04:51:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fa4cec2-57c5-34c4-b7cb-4c052250a17e | -10.34552 | -61.65363 | 2024-10-15 04:51:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22dfde8b-81d3-3e0b-815e-fe94c58c1b8d | -10.20293 | -61.39642 | 2024-10-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ef224a2-99d6-39e5-b201-083b3d7468a6 | -10.8642 | -62.33295 | 2024-10-15 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43bed6ab-9d9d-3fc6-81f0-6efdf860b6bd | -10.86363 | -62.33595 | 2024-10-15 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea8d68c7-c031-3caa-987d-9902c6061337 | -10.86201 | -62.33095 | 2024-10-15 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30a4a3b7-53b0-323d-93bd-eb53e554d85e | -10.86145 | -62.33401 | 2024-10-15 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fecac8e-2fd6-38c4-b928-6b705cf97523 | -10.86089 | -62.33709 | 2024-10-15 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d277d925-d3b6-3fb2-b445-eee3a7615476 | -10.85909 | -62.332 | 2024-10-15 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebbe0ed6-ac16-3839-822f-713c28255507 | -10.85851 | -62.33504 | 2024-10-15 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 644b4cfc-656e-3e65-87bc-1b310d3b188f | -10.85631 | -62.33324 | 2024-10-15 04:51:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8620fb83-4f77-354d-abe8-fdd225cb2e1e | -12.76207 | -62.29465 | 2024-10-15 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2c06119-da8c-3e28-8f0d-56465b1db149 | -12.96042 | -62.79586 | 2024-10-15 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec3e99fc-a228-3dc0-a5ca-9ec72d4439c2 | -12.76315 | -62.28894 | 2024-10-15 04:51:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f77bd34-09d5-3a59-bd8a-38dee9ce8869 | -12.66074 | -63.07887 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77f7b3c9-402f-394d-a7a1-f295dce2c52a | -12.65951 | -63.08535 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3fc6082-4b44-3a52-adf6-6402a9d88489 | -12.49864 | -63.02208 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce290862-6eb7-31f5-a281-36f294e56983 | -12.46222 | -62.98314 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6be72c57-d709-3444-a1cd-6f2245a45fe1 | -12.45888 | -63.02946 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18439f5d-c16f-3f32-980e-5adea13992ab | -12.4543 | -63.02515 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8752b84a-9694-3621-aaeb-06f3f614ba53 | -12.45369 | -63.02839 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4eaa145a-e20f-3e8e-91d8-0eb08f7f904e | -12.45308 | -63.03162 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b4426f5-edb6-3dae-b1e7-0321b4bcf69b | -12.44972 | -63.02085 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a533a3d-979e-3585-86f8-a229d18def5e | -12.44911 | -63.02408 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README70.md)
