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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e935f7a0-77fd-3d79-821e-dbd5924c2338 | -3.07377 | -54.16321 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7804b636-0601-3eef-b3da-c3ee3469a93f | -6.87407 | -43.67762 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 91219b99-a94b-3bd9-9db1-55afb720be7b | -3.46056 | -54.59338 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3892cb9a-e439-3819-b95b-10a1d07305e2 | -5.83652 | -45.01055 | 2026-10-05 17:15:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6a5640eb-199c-339e-839c-1e66c3afc029 | -5.68338 | -53.4982 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| fa7e57cd-7dfc-300c-8ea8-a48e1791857f | -8.44581 | -54.9757 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90ad2372-6331-3590-ad7c-c2610845139f | -4.06389 | -54.04919 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 54ac0a1e-e38a-3177-9dc7-8330ff97aeca | -3.23418 | -53.88694 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e8fb88aa-3750-335a-bde4-5b3cfc53f159 | -5.246 | -43.1515 | 2026-10-05 17:15:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ea00096-8f88-38df-bbed-eb62459bbc2a | -6.67769 | -45.21665 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 57d8efcb-a6dc-3bae-a276-95fff8ecf50a | -6.68428 | -45.22488 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5895bc59-ad23-384f-99e3-5eccba124b8a | -6.33144 | -42.55688 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 3bd0e0bb-ec06-361f-8354-388e35bd7e50 | -5.39694 | -54.45592 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 910e515e-ff1d-3e81-9389-1429a7172263 | -6.73039 | -44.928 | 2026-10-05 17:15:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b9de7527-2753-30ee-8e2a-b552a2cd9070 | -6.69335 | -45.21708 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0fe9d1c9-6a47-3976-a50f-277098133a94 | -3.09772 | -53.72727 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 186cae95-dc56-383b-8bb6-196fe8c34b17 | -8.65512 | -54.55674 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| de9e82b7-44f9-3163-b79d-883db3e58fd8 | -4.03023 | -54.88842 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| bc12fb75-1145-3d75-82a9-8fca2671459b | -8.31992 | -45.46659 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2e6c3b56-543f-3465-8c11-0542ff1f4c67 | -7.90031 | -44.18433 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a18b3cbd-ad96-3efa-ba7a-b30cb69da41d | -8.77789 | -47.56432 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 220ca0a8-1bfd-3586-9aea-60ebd0004919 | -3.6758 | -55.51325 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1f5d6e2d-633d-3677-92dc-a5fcab592b25 | -3.0743 | -54.16666 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0cb427a9-0419-3ef1-bcb7-082389fb5483 | -3.07151 | -54.17062 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df3bbc1c-b98a-3240-846b-21d9bbc6c74d | -6.68584 | -45.23405 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c017d0b7-0a28-3a93-ba44-aa8053ec084f | -3.04662 | -54.22803 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25fbb9d5-26dc-3bbb-a70a-354e8eda99d3 | -9.88114 | -64.17255 | 2026-10-05 17:15:00 | NPP-375 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 50c46bc4-6b85-3709-b1aa-09f37fb5072e | -3.60909 | -50.97693 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf289212-52c3-3278-a24b-38f2dfb650fc | -6.51002 | -55.38866 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9fa199d6-a69c-31a6-984c-42558f433c91 | -6.88661 | -43.68342 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9350885c-1695-37e2-8777-24766a7a30c5 | -3.82156 | -41.80975 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 4f579f7a-28d4-31ab-ad39-50fdcb75d56b | -3.10052 | -53.72328 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 2fb8cdea-21b4-31dc-8d4b-a4d30c82aef0 | -3.46602 | -50.08955 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 564a2b90-2cba-37b3-bb76-7dfeffcbe80f | -6.60449 | -42.26347 | 2026-10-05 17:15:00 | NPP-375 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| f01fd34e-3f53-380f-bcc6-3f9a4ace1919 | -5.68511 | -53.48728 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| ca8da5b7-c945-3627-88f8-56180eea8326 | -9.91764 | -65.01871 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a7fc2471-ece2-32c0-8d58-83f01f8775cd | -5.44108 | -42.64745 | 2026-10-05 17:15:00 | NPP-375 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 6c317805-165f-3151-8a94-4744fb520766 | -8.53654 | -54.6011 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 519ef1af-b17b-3b3a-acf8-9add67f9812d | -8.42139 | -50.82745 | 2026-10-05 17:15:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a7ef5128-2bd3-34bd-9e72-17cd34010122 | -3.29081 | -53.85707 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0b4520ca-5fc6-36e0-8a9a-c37d5ada22c4 | -8.78082 | -62.87311 | 2026-10-05 17:15:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9ce01df7-730f-37bb-8db8-6fb269c268a7 | -2.54064 | -49.64632 | 2026-10-05 17:15:00 | NPP-375 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cc3a1bbd-0f2c-31bd-93d2-0f9ffb87ef9e | -5.03369 | -42.75885 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 808cc284-4859-3648-a259-c340c3db6dff | -7.83544 | -45.30413 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ae2acc0a-e124-3a84-a9b6-1f7315b8fb23 | -4.00455 | -55.67619 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 82daac40-8412-3c15-b75e-c5c5c9ed8c45 | -6.32395 | -43.81626 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8719a2f4-13a5-3e9f-b084-4825a6079d38 | -3.10782 | -53.70437 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| bd410052-4234-34c8-95be-d434b15cd8b8 | -3.2233 | -55.12106 | 2026-10-05 17:15:00 | NPP-375 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0a5747fd-fe59-34ed-a1b5-0aaa060d20d7 | -3.68277 | -55.94795 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 851ff00b-8cb5-3c6c-8531-ec0feab8081a | -5.68232 | -53.49125 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 928dd2ce-2e11-30a0-9ae9-5d8dbb21018b | -3.08827 | -53.72549 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c001ffe4-44de-3a35-a1e3-d288c4b4c4c0 | -3.89438 | -58.74262 | 2026-10-05 17:15:00 | NPP-375 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 180.7 |
| ad570900-0179-380a-bfbe-f9aceb625624 | -5.94902 | -41.34629 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 42.0 |
| b1957f43-2daf-3320-8e9b-4daf4a5cfbc0 | -3.06275 | -54.15782 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 8fda0721-3bf7-3ed2-a450-e32aea8441b5 | -6.74274 | -41.20426 | 2026-10-05 17:15:00 | NPP-375 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| ddb94408-8c5e-3c4c-b746-74aa40e7aa08 | -3.64788 | -54.04789 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e4392394-a298-35f6-9344-047fb5a13933 | -3.63003 | -55.28078 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 774af7f7-3349-3426-93af-53532dd57a7c | -7.22088 | -55.17924 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e2db620c-df4b-3adb-9a5f-5ed2c12f9e56 | -9.24522 | -46.68647 | 2026-10-05 17:15:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 35325cb1-a00f-31c6-899d-1e2f53216da5 | -8.99358 | -67.07207 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9d54f297-daa9-3e02-9532-4e51e9738cbf | -3.29693 | -53.8526 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 874bf85d-bbd6-3bcd-a0ec-4050fbfd6103 | -3.18528 | -54.07534 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5fd7001c-4ec3-3e74-9952-043e7e7dbbb4 | -3.63339 | -55.28029 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6e5eec0f-48ab-3f6d-9510-95318d1376a2 | -4.71423 | -47.93508 | 2026-10-05 17:15:00 | NPP-375 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fe6e17dd-ad09-36ac-ab3b-9769f8c0055d | -2.99322 | -42.04457 | 2026-10-05 17:15:00 | NPP-375 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6ef179a-2841-3ccc-8bee-aa466304c8e3 | -8.53493 | -50.43482 | 2026-10-05 17:15:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c51e0058-d39b-3294-853c-40aad0c9a378 | -4.91494 | -41.74303 | 2026-10-05 17:15:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 9d318575-e468-3b47-99f8-f90f1491db8e | -3.09652 | -53.73491 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dbb83d39-e9d4-3aee-9adc-629d7cceee73 | -6.53341 | -55.38137 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 15430254-128f-391b-8bc2-bb5901be5c47 | -9.7363 | -53.95017 | 2026-10-05 17:15:00 | NPP-375 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b66cf6d1-694b-3f68-b54e-03917e6e8400 | -4.20393 | -53.46334 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c9414cb7-82af-337d-a730-8493af08abae | -3.19283 | -54.10241 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 62ced2cd-695a-3c83-918c-7d9ed2d56156 | -2.69211 | -49.03578 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 82d00494-5c00-3169-9e2b-c84321e51ab7 | -8.28188 | -49.91682 | 2026-10-05 17:15:00 | NPP-375 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 80114007-f108-31dd-8f93-a93d24ec06e2 | -5.11387 | -42.6418 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 15af86c9-5a25-3b4c-b3e5-6d51cc6c01b2 | -3.0433 | -54.22853 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 01162908-087f-3a09-856c-feb225b8be68 | -5.24889 | -43.15227 | 2026-10-05 17:15:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 825b724d-4bf4-3a8a-8bb7-8ce2e271bce1 | -6.91179 | -43.66339 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7def315a-0d69-36ef-9628-0513756df839 | -3.05552 | -54.21962 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 847185fc-f0fa-36ab-8592-560181e313fd | -6.72873 | -44.28183 | 2026-10-05 17:15:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f48cbdd0-e326-32a2-908e-8986a424ce55 | -5.80613 | -45.24218 | 2026-10-05 17:15:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ab4dadc-793e-3623-9f84-a588466f45d7 | -3.28343 | -50.40073 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f54cdfb-218d-3c79-b802-ad360ea6db97 | -2.55526 | -49.104 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 08253972-3133-3b74-a4d7-f03a3cfbf718 | -3.97836 | -59.34092 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f3f8ae2-5455-3f44-bb8b-3fab64acf182 | -9.40861 | -47.30677 | 2026-10-05 17:15:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 78bfb10d-d7f9-3e11-8469-39c04046963a | -3.63057 | -55.28432 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 19302b9f-3531-329f-93bf-8fd30b920dca | -8.85533 | -66.79853 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 6e089fe0-f159-3994-8cf8-7dad2651e267 | -5.67674 | -53.4992 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 08908418-818c-3ee5-9e22-cc6b2f641e33 | -3.08051 | -49.54174 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3e55153a-c98e-3515-aefa-e9ce5a08d0bb | -3.23205 | -53.87308 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9f69c01b-92cc-37d5-8728-962fa5146e6a | -3.91827 | -44.14971 | 2026-10-05 17:15:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 180f4286-202c-366f-a3a2-e22e616d9e67 | -3.08531 | -54.17205 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f8d1b23c-1ccb-342a-96f1-3bf739faf812 | -3.27764 | -43.0935 | 2026-10-05 17:15:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| faee0a04-cad6-3212-b5dc-1480501e112e | -3.27137 | -50.39789 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| de791776-17f3-396c-8fc2-0d5471dd50f5 | -4.25751 | -55.04964 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 22e0ff32-49ef-3e13-8769-eda929e921e3 | -5.83705 | -45.01362 | 2026-10-05 17:15:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0d849dc3-d9f2-3d52-8dc0-c695fac18ae9 | -8.82087 | -49.31133 | 2026-10-05 17:15:00 | NPP-375 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8128e380-510e-3e63-a898-9307825d4744 | -3.91749 | -55.74799 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| be358f2f-2941-3596-89ee-7a4e70ad5035 | -6.83298 | -58.59002 | 2026-10-05 17:15:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bfab4a69-427e-37a5-89a8-a8d488f3a60e | -7.21227 | -55.19188 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README114.md)
