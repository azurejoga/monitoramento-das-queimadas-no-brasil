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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ea05040-0195-30df-8d87-e3999bc0e044 | -11.90192 | -57.13118 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1f5cc42-d43d-3b5e-a9da-a6925aa58971 | -11.89797 | -57.13434 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d90c14c-d04c-3b79-9fcd-a7246b4d8a79 | -11.88725 | -57.13642 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb0304c4-0258-38f3-b797-a1e068197e6e | -10.12928 | -52.40656 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8e15c43-48b6-34da-a70b-fba8be8a85ef | -11.22318 | -54.31143 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 74509c4c-36bc-3bee-a3c5-00a38dc1654b | -13.27543 | -49.76739 | 2026-06-30 05:16:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 936bf6f1-2cd0-3d16-a4fe-10d7123d829f | -10.13982 | -52.40113 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3e33a1e-b8a1-3de5-8e99-f0ff70f91f3f | -9.19217 | -46.63631 | 2026-06-30 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b0e7030-ffaa-3284-8e69-ff50f8727e00 | -9.59846 | -56.92496 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be654c27-24a6-3f58-bf7d-c1569a7fdd64 | -10.55239 | -56.33831 | 2026-06-30 05:16:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a492a6d-e5e6-37b0-b568-1a0bd67fb7fe | -13.71031 | -47.87023 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99c4fa1b-6bf1-3208-9907-77580712beaa | -11.8974 | -57.13802 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c3551f3-15e0-3f3b-afce-e93bdf086c4e | -10.72338 | -56.22709 | 2026-06-30 05:16:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98d9acd4-0fc8-3390-b2e1-1cc2840df0b8 | -13.27738 | -49.76764 | 2026-06-30 05:16:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 668aee92-5f09-3364-98fb-d0a4d66e00c1 | -9.32674 | -58.01442 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b700549-832d-33a8-a475-914d9e8e097c | -14.95684 | -52.85884 | 2026-06-30 05:16:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2091211-1ea0-3c06-8da2-02cf68c56206 | -10.0454 | -59.1134 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7f7bce-1368-31d6-bf0f-2b8ea619d91f | -11.93924 | -57.70533 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9759a41f-ec89-3123-a26b-ccc8055d2fe1 | -11.22632 | -54.31677 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3c16be6-c9a4-3524-ac84-794d0367a3f4 | -12.45118 | -58.49276 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51f1a6e0-729f-32f4-bfcb-9e9d8e33597c | -13.71599 | -47.87449 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68312d87-4235-371e-8a1c-274406bddbbd | -9.08603 | -59.38808 | 2026-06-30 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c76f94ef-17e4-39db-a64c-36ba70967476 | -9.15304 | -58.29678 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 692b7f79-4aaa-3d13-9a48-1051d6e32c84 | -9.32729 | -58.01093 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ca65774-6a12-3a4d-b2d2-3a6986fb474a | -9.12732 | -58.2644 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f4eb78f-fd11-384b-ac34-9cfbbe64dec9 | -11.93869 | -57.70892 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edc68782-4105-30a1-847a-fedccd600cfb | -9.08267 | -59.38752 | 2026-06-30 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 87725130-ffdf-336c-be70-43fa9d178273 | -12.61288 | -57.88882 | 2026-06-30 05:16:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad0af824-040d-323f-a966-6cef30600d88 | -10.24626 | -59.302 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49d52578-b759-3913-8d4d-f8a4eb8c50d7 | -12.22305 | -56.56273 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d118d485-2419-3955-a0cb-8c3379e80915 | -12.19934 | -52.86724 | 2026-06-30 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 421d71b9-5cd9-3bd7-93c5-fa1128aed515 | -14.63307 | -54.46299 | 2026-06-30 05:16:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ee4dc0e-1081-391f-af24-c6aae0e47712 | -11.91946 | -57.38818 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee7b482d-70a1-36d9-ae3f-db930d403c1b | -11.90551 | -57.41196 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f321fc5e-4a55-322f-8588-c19bad8de769 | -9.45279 | -50.84532 | 2026-06-30 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 202d249e-cb30-3d2d-b46b-c4fce9421d39 | -11.63568 | -59.00855 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 634c3fe1-a57c-3d3b-813b-59a07fc22e19 | -9.594 | -56.93161 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6a82c35-0a82-362c-8340-56f0aee4be33 | -12.45007 | -58.49981 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff155ea1-279c-3cd2-85de-21f3a164d8c3 | -13.26134 | -56.79905 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4dff3fdf-7e2c-3ff1-b134-a26bb510a3e9 | -11.31645 | -54.46873 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d55fb69-7bf4-36be-b69e-829a67da667f | -9.60237 | -56.92189 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62916322-571b-3a21-8fd2-bf6db1ee36fd | -11.63512 | -59.01206 | 2026-06-30 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 087a195f-ea30-3b81-83db-4116115eedad | -10.80325 | -48.5714 | 2026-06-30 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c9f825d-4ed3-3d0a-a0de-58d4d6618594 | -13.25384 | -56.80187 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0c1d9b6-0ed4-365f-be52-1b47326b68a2 | -9.13118 | -58.26144 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df9c9995-dae1-371d-b5be-a03df9f5e8c4 | -12.28511 | -57.5532 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c306222-46d9-31f6-8828-b45f2b9f6993 | -11.88556 | -57.12482 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22346f39-d0b9-39af-a0f4-296961274123 | -9.75152 | -49.02973 | 2026-06-30 05:16:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f735f7c5-4fc3-3eb2-ab19-05fb4f9f86e6 | -13.94399 | -53.95031 | 2026-06-30 05:16:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e04663df-ee5c-30bf-b7b7-fbb9c745b5e4 | -9.1569 | -58.29383 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d114ef9d-cf9e-3b39-bf5d-c83a6b57a577 | -9.12401 | -58.26386 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 709e6ce8-e2b6-3724-a306-0d4d1a7f0c9a | -12.45504 | -58.48978 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eda73004-d725-34c7-ab37-d94397b25c0d | -11.87369 | -57.08895 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 568e57f0-3665-3151-8c88-f62319ddd5e8 | -10.13498 | -52.40453 | 2026-06-30 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 975877ae-1cea-3955-b4fc-fef54bd9f803 | -13.26364 | -56.80732 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1c81e6b2-14f8-3cf2-a23a-281eaec9c042 | -9.31793 | -58.02729 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4c34805-e4e4-3fac-9da6-b5cfaa6a378b | -11.7965 | -56.99774 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a116d311-e4c8-31a6-8f50-003c700dd0d1 | -10.76961 | -54.10334 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 586a8650-89d8-3eae-9e84-8df5d5f6b851 | -9.3295 | -58.01843 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6580a131-090a-3f7c-aca6-125038f4d51e | -9.14974 | -58.29625 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f1fb969-0320-332c-8b7e-5523c727c744 | -9.18736 | -45.32644 | 2026-06-30 05:16:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2db006be-e174-3454-839b-4d860cd6db13 | -9.756 | -49.03717 | 2026-06-30 05:16:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24760bbb-c48a-3345-ad2d-a72b221378b4 | -10.38313 | -49.59368 | 2026-06-30 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40513353-f139-3565-8e2f-3426ff8bfd4f | -13.26768 | -56.80397 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d628dbaf-2ba6-34d9-a8ca-442bc35fc62e | -10.78573 | -54.10072 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe0c9c13-ac66-3465-a3c0-dd49e4c6b27d | -11.58171 | -47.92126 | 2026-06-30 05:16:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6455f71f-4820-3a66-9257-e0dd9a834e0b | -13.71703 | -47.85606 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c04a155-2089-3c49-930f-9c7ad37c0521 | -13.7092 | -47.87032 | 2026-06-30 05:16:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9e462a4-9ed4-360d-87f3-c6009717a7d4 | -12.44511 | -58.48817 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ebfc33ba-444f-37f7-ba6f-e44a8c5114d7 | -11.93813 | -57.71249 | 2026-06-30 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a347b47-175e-39c8-9cf9-2b0822304ec0 | -10.06674 | -60.49285 | 2026-06-30 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 829d91a3-72ba-3a71-aacc-21983344a4be | -12.28567 | -57.54958 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20b0464c-aa23-34bb-a3cc-6a37c8057859 | -13.26193 | -56.79517 | 2026-06-30 05:16:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0cd90b21-917c-3e02-8553-b9a529826e69 | -9.75196 | -49.02637 | 2026-06-30 05:16:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0b0c072-79d3-3c22-a96b-3b892c6319aa | -9.19108 | -46.63548 | 2026-06-30 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9947aa6d-d2d7-3401-98fe-277a738943f0 | -11.89008 | -57.14062 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d640668-43d1-3cc7-a12c-7a88692560b1 | -9.32564 | -58.02138 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3d65a05-5fe8-3469-a495-f5a95ceff164 | -11.21591 | -54.33475 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 028c82bb-ea9a-394c-bbaa-9c9bd83041cc | -11.89176 | -57.12959 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7de4dd7e-0de6-3217-8b04-8c9cee40e168 | -12.50612 | -48.26883 | 2026-06-30 05:16:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fcd576e-b9d7-3ec8-b788-4b4fe93115e5 | -9.59735 | -56.93213 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc925667-6e59-3bca-b286-5bcceddc793e | -9.32895 | -58.02191 | 2026-06-30 05:16:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b23f4c36-1988-36f2-81c0-28aac1180e55 | -12.45228 | -58.48572 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d4d70c0a-add6-3a69-88bd-4b7ea61b46cd | -12.45449 | -58.4933 | 2026-06-30 05:16:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9de0f24-8520-3934-884c-130ed9f27aa5 | -10.71923 | -51.66032 | 2026-06-30 05:16:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d341cb14-d4bd-3ad5-bf7c-449faef194ce | -11.89458 | -57.13381 | 2026-06-30 05:16:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddaad20c-a93a-3769-a9e2-170c6e76fd40 | -11.92283 | -57.38871 | 2026-06-30 05:16:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a454031-703d-30de-80b0-c179e781d610 | -9.14275 | -58.25261 | 2026-06-30 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 469281a2-df78-33b6-8d2e-31e4f0066b31 | -10.77278 | -54.1088 | 2026-06-30 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3894f024-92e6-3840-b54f-226e1c1190f4 | -12.22077 | -56.55443 | 2026-06-30 05:16:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d210767f-ba69-3c3a-a06e-0f4daa9b91a5 | -9.60572 | -56.92241 | 2026-06-30 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0057d3b2-fb58-3958-a25e-c795c5bf7daa | -17.71579 | -46.78277 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d319f5ac-c095-3293-91df-79dfe5106578 | -16.17617 | -59.33878 | 2026-06-30 05:18:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7391311e-9d36-3e8d-8a52-e956aa6dd931 | -16.17561 | -59.34237 | 2026-06-30 05:18:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98c493d2-203f-3dfa-be1a-23a7abd8ec1c | -17.7118 | -46.77742 | 2026-06-30 05:18:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8699c568-615b-331f-9ecd-a4aa54145ca6 | -15.08466 | -59.9044 | 2026-06-30 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| adf35852-110a-323b-971f-f648a99a4b47 | -16.19942 | -59.32056 | 2026-06-30 05:18:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e2ab4136-997b-3c4b-8f50-b6c49af27084 | -17.4357 | -47.16684 | 2026-06-30 05:18:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c109b43-8589-3a77-beca-5faa02bde129 | -15.08134 | -59.90384 | 2026-06-30 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f732108-f98f-3af6-abdb-38a29fda19e4 | -21.31637 | -48.5388 | 2026-06-30 05:18:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README18.md)
