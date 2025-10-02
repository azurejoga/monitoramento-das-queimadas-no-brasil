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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0050cdcb-6b7e-34a6-a6cc-1160105276d0 | -9.5608 | -50.77898 | 2025-10-02 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a6d96e4-811f-3764-8d5a-05b700d1cbaf | -7.77774 | -42.5431 | 2025-10-02 04:29:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| da5b8618-43bb-3bf0-87c9-95d7c3e3de96 | -6.95963 | -45.31772 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 10ea3db9-cf82-39db-9892-faa61dfc247c | -11.4652 | -45.06158 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d71a9ce8-ae06-3253-b916-67d9492afd3f | -11.16962 | -47.27761 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3d788d74-29f6-3500-b8c8-865d8fa91f7b | -11.27804 | -47.83004 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c447bcd4-0748-33fe-b0c0-3a9c271040ad | -6.35392 | -43.297 | 2025-10-02 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39144f33-ea59-356a-8491-5d4dc8b00886 | -6.18458 | -44.06189 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a9bb923-aca8-3dd5-9fdf-c269a5c064c8 | -10.83014 | -46.63747 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1f9035b3-6f8e-30bc-8584-be35a18eb3e8 | -12.26607 | -44.13157 | 2025-10-02 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9ca10edf-f831-3e6c-bde4-6ba9b8b1793c | -11.81544 | -44.909 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef3a793e-4914-3391-8931-02e9d7616a75 | -9.44843 | -50.89731 | 2025-10-02 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 198548e7-1c0c-36e6-9ab7-294b279ce0ee | -10.23695 | -50.30893 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 68b7c610-4642-346a-a72a-3aa79d31ae5e | -11.27748 | -47.83358 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a3a496a-dcf2-3856-8cd0-db1ad57c09b5 | -11.80102 | -47.58523 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 184a749f-f41c-3b2a-aa9a-58f5512f341e | -8.51616 | -47.79715 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9214c925-5f9d-3af9-9c3a-2bdfa8dac6ea | -9.94456 | -43.66696 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edbdd5ac-949b-3041-b56a-a52d7b6ef000 | -10.32578 | -48.18449 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1aea626-5c71-3eeb-96e8-3fc355949256 | -12.11613 | -43.41829 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce57db68-613f-3013-b0f6-424738c877fb | -8.70424 | -47.86734 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2be7a3c-c507-3611-b2fb-b10dfc415c18 | -6.35689 | -43.30172 | 2025-10-02 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3dad331-7cf5-307f-9d51-9d5740342077 | -11.11874 | -49.81394 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd0b62e7-9683-3df6-908e-8b4f3d350b41 | -8.51466 | -44.66909 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6bc3ae1-684a-383e-986c-51fc946c9993 | -6.72668 | -44.14085 | 2025-10-02 04:29:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0fbd9d5-ce03-30c1-9216-0276edf71af0 | -10.21008 | -50.26723 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 58979045-79b2-32c1-a73c-18bec14f51bb | -9.92008 | -43.65435 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2778d4b4-9ae9-3079-978e-81a773b5e8d8 | -12.27409 | -44.12833 | 2025-10-02 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f728e01b-99a3-341a-a012-56768d0d13f4 | -9.94587 | -43.65821 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f745987-137f-3e23-b69f-a574dbb541b0 | -10.48891 | -49.36858 | 2025-10-02 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d759378-a39f-337a-a26a-2c17c3cf9167 | -9.40975 | -47.58498 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8605e1c3-5070-397e-9ea2-1b322647e1b6 | -7.88493 | -47.30752 | 2025-10-02 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3bf1fb2-4b8c-3756-bf5b-fa76518b3725 | -7.72809 | -46.22325 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e81f40a2-2be0-3b5b-93e4-03271d14bbe6 | -10.24289 | -50.36185 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c7b0b28d-07a2-30c7-9f24-b29226d0c733 | -11.818 | -45.01173 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c060a55-aad3-37aa-aadd-40c99d8695d2 | -9.94694 | -43.67624 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fe3e962-386c-39a2-9204-91c79c59e511 | -11.54391 | -45.0638 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91a511bc-3157-3c48-b62a-c0b2064c5b6c | -9.90199 | -43.70051 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d89b0c4-aa1e-3b34-ac9a-da1f95477466 | -8.51223 | -47.80018 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 175cad31-d500-32dc-b46b-9887ff65fb7b | -11.20011 | -47.19229 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de77bbfc-24ee-363c-be28-39f32e50febc | -8.81124 | -46.6887 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6afe35d-ff0b-3986-9a3f-2c30b94e1e0b | -11.47422 | -44.97801 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| efbe037c-9ec2-3b30-a939-094f968eaff1 | -10.83569 | -46.62382 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a3689f1e-b05c-38dd-adbb-f0e07ab53321 | -8.89766 | -46.60909 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2737f62a-1264-33bf-b1a5-bd64a4423111 | -7.29139 | -42.8165 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b8ec388-09de-319b-be6b-c729ce09b5d2 | -9.62737 | -46.6355 | 2025-10-02 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd4abee7-8a87-342e-8f7e-4767c27cda05 | -10.83455 | -46.60909 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 11b1ddcb-6922-3b8a-922a-09b820b00ae7 | -11.00933 | -46.57837 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c0c3c9e-4895-3df8-a485-9fd73a4ba401 | -6.77166 | -45.58924 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e481c0ad-ee01-338b-bf43-338a1fb4c9ac | -6.98467 | -44.38856 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 067bd10d-d56c-3b38-b459-9a99f0a1a46d | -8.90923 | -46.06354 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6934d042-afb4-31a6-99b4-deb26a6ae30b | -10.81913 | -47.9693 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60876822-2b1b-3536-aca6-95cff7e2a121 | -11.19012 | -47.19069 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21571b8b-19f6-3037-a058-dea0e292ad59 | -11.81156 | -47.58333 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bdab1d9-54f1-3389-a980-8c90f06f4fe1 | -8.5128 | -47.79661 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b906cca-f1fe-32a0-b584-1ddb513531a9 | -9.93707 | -43.7673 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 50de1e21-aa1a-31a1-a821-0431fc6099c7 | -6.26548 | -43.88532 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ea6d0fb-3035-3611-95d4-26dcfd65a9a6 | -10.70601 | -47.98709 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9ff7cea-47a1-3429-a750-413839f4c8a7 | -7.60132 | -45.4088 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d0c8cbf-8db5-3adb-b36a-c86185ff0fbf | -10.70868 | -48.00537 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3a35451-8e06-3263-aa03-38e7545eecd8 | -7.72864 | -46.21976 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1899e58f-cd93-3a2f-9dac-8b2138f73d93 | -7.24762 | -49.5154 | 2025-10-02 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3e5f31c-8584-39d3-91cf-57f9ae9985b9 | -9.92929 | -43.74415 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 88bfddcd-6da5-3065-849a-f1c379676d86 | -9.9435 | -43.72434 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b055cf50-46a1-368f-80d3-de88ee5692e1 | -11.09081 | -47.83914 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75dd2763-9b34-3073-ac33-ffd91ae484da | -9.85754 | -44.60247 | 2025-10-02 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c139e127-5e91-3914-9ea2-0aba840670c7 | -11.67895 | -45.31869 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f9a40d4-71e7-3e92-a63a-f5270184e7a9 | -10.68842 | -48.5579 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 281e6760-b678-3ff2-9f1a-1b6f7e763686 | -10.79462 | -45.34902 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9466a84e-d18c-3330-b332-76a36b6a526b | -10.86236 | -46.5844 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7f83003-44e1-3dc5-b77b-4268b15755db | -10.33076 | -45.25679 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc7913eb-c308-3f32-905a-ce6214a54afb | -9.4877 | -45.54994 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1650476e-fb2c-311a-9e36-bbc14881e6c6 | -8.57983 | -49.60492 | 2025-10-02 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf56de4c-4a2d-37cb-b602-45c67be41fa0 | -11.67142 | -45.32153 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93dc753e-240b-3cf4-879b-2881c3c3fc15 | -11.60653 | -45.05646 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 464bf43e-c561-3eef-b9f7-e6b39f3e419f | -9.33363 | -45.91824 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 176fa893-b2c6-3ac2-8979-10a9a05281ac | -11.73559 | -44.42621 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dc73a6a-932d-34a7-948a-ef14d66c4b30 | -11.00902 | -49.58384 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37077c8e-917d-3e21-9b16-be8992634ed4 | -5.62542 | -51.93847 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 708db18f-542b-3c27-99e0-c30e7b6e83d2 | -10.68832 | -48.57991 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b03f54c3-9d67-36cb-994d-f87bd2e6254e | -8.57373 | -44.66278 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c76319e-655f-3333-80a2-f6cc466da150 | -11.09306 | -47.82501 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2b0d098-4513-3d19-9b1f-739598415394 | -11.58655 | -47.65921 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d1ae928-b29a-308c-9807-d50cd4146e96 | -7.79264 | -42.52132 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d364cf01-8295-3af8-8137-d05bf355a67a | -10.84606 | -45.39514 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6c5e01e7-7ab4-3fec-9e86-bcb45a57aa95 | -10.29182 | -51.077 | 2025-10-02 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c398fd9c-850a-3560-9fdd-31aa69e0ff58 | -11.16239 | -47.19345 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23dbba68-d1e3-38bf-9bfc-625db9177373 | -10.82247 | -47.96984 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f745f1f-b1ef-3578-844e-b3c3316fb86e | -10.24488 | -50.30597 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aee7f6ca-715a-3c30-be2c-d6b8f7f1124e | -11.81481 | -44.91321 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35c818b8-c5c5-3197-ba82-d6d21d47bf53 | -11.26499 | -47.81307 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76ec48a5-4fa5-3170-abd0-c6190bf8c74a | -6.96526 | -45.32585 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c99b4ac-d67c-3b30-ae10-97e048565521 | -11.07809 | -47.8117 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8af9c1ab-2a02-3741-837e-7e8f654faa37 | -9.84871 | -49.30892 | 2025-10-02 04:29:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f7ee1086-0b3a-3ec5-9422-4e63f15d3267 | -11.71799 | -44.47073 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eaf7610-be09-37be-aa72-976523653a76 | -10.30924 | -48.24466 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc8f0bd5-3075-3be3-927c-dd8004eed211 | -11.27585 | -47.82241 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6727c19a-9126-3466-8200-ca491c7a4d88 | -12.75499 | -39.74041 | 2025-10-02 04:29:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1df2acdb-c4a9-39e3-8e9b-a5ca56e22388 | -6.28707 | -44.07271 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbac61a9-17ac-3fa1-b5d1-cb4dbb9dcac1 | -11.62168 | -45.05116 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46b40f1e-cb31-3ee8-8c53-e850063747e6 | -11.80161 | -45.00097 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README63.md)
