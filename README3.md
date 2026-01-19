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
| 3eff0ae3-26bc-32e0-b390-c80cd37ac8fb | 4.44481 | -60.63879 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1035b703-82d1-3203-972d-ae0e8970b22b | 4.84449 | -60.24585 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b2dc6e2-1d9f-304e-a7ea-d81d8db87a0b | 4.38376 | -60.7316 | 2026-01-19 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcda79fa-5b61-3294-b5bb-967e24d9eb90 | 2.54914 | -60.57059 | 2026-01-19 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c2a8b67-81ae-310c-94a1-0987c840421e | 4.45469 | -60.6332 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35911fa6-c708-382a-ab54-e9e6811f65e7 | 4.42851 | -60.64922 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4b966c5-68ec-3afc-a752-27c39dddcf74 | 1.13441 | -60.51619 | 2026-01-19 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cb98ab7-a499-3257-87c5-48691085cb30 | 4.45182 | -60.63779 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5023e510-4a2d-3398-bd3b-aef931e2e939 | 4.43718 | -60.63577 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 751ea876-62cc-3541-a2d4-5fe37ac2ea8c | 4.44955 | -60.64619 | 2026-01-19 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4431e274-627d-331d-b285-be6a5531f63f | 2.9567 | -61.31138 | 2026-01-19 05:25:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 862dbd60-8538-337e-b3c8-e1a7a43c8e50 | 4.44543 | -60.64278 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a817aa49-701d-34d8-a7ff-d97f91763c48 | 2.54571 | -60.57113 | 2026-01-19 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa866741-d7e7-3bb7-a9d6-d93eaeffddec | 2.95946 | -61.31126 | 2026-01-19 05:25:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48ab80a-7e2d-3688-be00-0e86ecc0649f | 1.13554 | -60.52343 | 2026-01-19 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 161c1aaf-8067-3753-84c2-917778663320 | 1.03318 | -59.93781 | 2026-01-19 05:25:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ee94cdf-5ac9-3e52-b21e-c3ef65c99807 | 1.1378 | -60.51566 | 2026-01-19 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a54ef83e-e206-3711-963f-ba2d4bc8fe0a | 4.44605 | -60.64673 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c6db019-2a1e-3fa8-a8da-d2b259439a80 | 3.53619 | -60.65711 | 2026-01-19 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7602b5c5-4a2c-3ef1-9ff1-13bbbf054e1c | 3.54256 | -60.65224 | 2026-01-19 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e12a5ae-1309-3d7e-b7d1-e3f941e7f50c | -1.95761 | -54.0948 | 2026-01-19 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a326ed57-6be3-3209-91d0-2746d8e167cd | -1.95358 | -54.09465 | 2026-01-19 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 445fa604-b842-39be-ba18-425726590747 | -2.14574 | -53.64904 | 2026-01-19 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0fbd1cbd-cb04-3b37-9a85-ac09f02d6ad2 | -2.14449 | -53.65039 | 2026-01-19 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1f23af30-6cf3-3739-87e4-bc3d0645cdf1 | -1.95781 | -54.09519 | 2026-01-19 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 740cceda-1b37-3ac2-801c-08518fdbc186 | -10.55104 | -56.34309 | 2026-01-19 05:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84eb1eaf-0219-31fa-a820-f950334beebc | -10.55157 | -56.33939 | 2026-01-19 05:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36355299-3f7b-3294-9729-1da211e9a92e | -10.55373 | -56.34297 | 2026-01-19 05:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b99e9066-6105-36a5-b527-010effe30ffa | 4.05196 | -61.47075 | 2026-01-19 05:46:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05d51e1a-4d45-36a9-82fd-605986a444fe | 4.1568 | -60.03 | 2026-01-19 05:46:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea31d9d3-25f6-3e56-bc69-0621760fc2ef | 4.04868 | -60.18124 | 2026-01-19 05:46:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1efeeb7-2917-3da3-8f92-6573ea45399d | 4.44623 | -60.64425 | 2026-01-19 05:46:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1c583174-6d54-33b5-875f-fefc139588b8 | 4.45609 | -60.63369 | 2026-01-19 05:46:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05a0e178-4027-3204-9c88-95bcdd59eafe | 4.31808 | -60.57287 | 2026-01-19 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6b4b74b-c34c-3868-9a0c-d9916fe5fed5 | 3.3216 | -61.12424 | 2026-01-19 05:46:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a3b7df9-263f-3fb9-a3b7-2520a21532d0 | 2.95891 | -61.31001 | 2026-01-19 05:46:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2440dee6-c2d0-3fe4-b364-f5808c2e4ff7 | 4.38261 | -60.7324 | 2026-01-19 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffa1e30e-93b2-38d8-894d-26d4bb7826df | 4.16075 | -60.02955 | 2026-01-19 05:46:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 298bacd0-9e35-3014-a198-b52a37d1c7a5 | 4.44697 | -60.64875 | 2026-01-19 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2521c81c-e6ab-36c8-a634-cab17ef4700c | 4.21978 | -60.82299 | 2026-01-19 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57bece94-1702-35b8-9546-f2fafc7b041c | 4.43732 | -60.63694 | 2026-01-19 05:46:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e74d37b1-04a4-3a6b-a7b0-1709c057c272 | 4.14893 | -60.03104 | 2026-01-19 05:46:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fdfa932-db8a-308c-b16a-e6998b42f529 | 4.45303 | -60.63858 | 2026-01-19 05:46:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83552f42-c1d9-3bd7-8357-feb9a490bb37 | 3.53649 | -60.65715 | 2026-01-19 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ab086cd-0286-3533-9e6d-dc650d38f2b5 | 4.45233 | -60.63431 | 2026-01-19 05:46:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0684828-ce51-3a23-90cc-1305be13f66a | 1.13511 | -60.52758 | 2026-01-19 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23fae0ef-5c57-31bc-8f3c-83333ab289c1 | 2.54899 | -60.57256 | 2026-01-19 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06149807-99f9-31cd-bcbf-021c05ec1c15 | 2.59725 | -61.29833 | 2026-01-19 05:48:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5a426aa6-ebe8-32c7-ac0f-c56d35060376 | 1.1373 | -60.51591 | 2026-01-19 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15adef15-8d2f-367f-b199-ab769d1c00bf | 1.1299 | -60.52056 | 2026-01-19 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d08cc0a-79d3-322f-bf77-c79324e14aad | 1.13785 | -60.51931 | 2026-01-19 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9dd02fc-3fc8-33df-bedc-a5d835f44dea | 1.13442 | -60.52333 | 2026-01-19 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6da9dc6a-ca73-36dd-8700-bdf61025d249 | 1.13387 | -60.51994 | 2026-01-19 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3b8bd79-0963-3bdc-81f7-c5ab9460f9ca | 2.20414 | -60.7066 | 2026-01-19 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92e2bbfd-2f31-31ca-ba57-5a7e612d8c62 | 1.13045 | -60.52394 | 2026-01-19 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d1fa562-b0f2-37e5-8f8d-ca084e2f3196 | -1.95448 | -54.09308 | 2026-01-19 05:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ef32395-16a5-3e96-aafd-a3a76e5660ae | -1.95369 | -54.09834 | 2026-01-19 05:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4da3e02-5d5c-33b5-bc32-8f912411ec4d | 1.13792 | -60.51385 | 2026-01-19 06:56:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c0910504-aaad-3840-95ed-3bff154b483c | -7.49222 | -42.7319 | 2026-01-19 11:53:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 9317169f-5e64-34e0-8a31-3eb89fdaf36b | -7.49352 | -42.72272 | 2026-01-19 11:53:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 831713cb-7829-3459-987a-a4cb8d518815 | -13.41086 | -43.00881 | 2026-01-19 11:57:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |


