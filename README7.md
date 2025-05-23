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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04557644-750f-3f3e-ae98-0b391e45dec9 | -7.21048 | -43.13118 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4dfefd87-23f4-320a-8be0-d3b4e86a4e32 | -6.22608 | -43.37416 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 94d3d52d-bf5c-3efc-838e-3e3ee919d71d | -6.94413 | -42.79574 | 2025-05-23 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4c0a89c6-21fd-33cd-a725-0403ae13b171 | -5.78563 | -43.61579 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a631b4a-1d23-3804-bc8c-c8949e641c47 | -5.7596 | -43.48912 | 2025-05-23 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3a3adc7-548e-3fbc-81d1-7f3cbbebf57b | -7.0672 | -44.93346 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aa345388-795a-3011-bfb0-414f609999d4 | -6.22959 | -43.35265 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8501d00f-5313-3e05-8590-1eaedd941d12 | -7.21116 | -43.12707 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ff21f91-b4a1-336a-9c63-b73f8d107744 | -6.03687 | -44.05017 | 2025-05-23 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2792f372-f1a1-329e-a02c-de06041fb862 | -5.76033 | -43.48468 | 2025-05-23 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c5ca76b-01ce-3910-8316-11c91b762526 | -7.22777 | -44.70986 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a605b07-b012-39ca-8a83-ad940ad5c506 | -6.22976 | -43.37478 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5875d740-28e7-3d55-ae31-a1dde9e3fe1a | -7.07272 | -44.93609 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e78ae1b-97c0-3d65-a269-d864aefbf3bf | -7.71118 | -45.66061 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 071791da-592e-3e84-8016-3c49dc3997da | -6.95121 | -42.79696 | 2025-05-23 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a6a49f6-71a3-3586-9f54-1ba292f8a8e2 | -7.22884 | -44.70834 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9911c68a-7906-3bc1-9fc4-dcf3352bdf5d | -7.39423 | -45.92739 | 2025-05-23 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b03567be-de26-33e7-aeab-44d6dbdbcbb4 | -6.94832 | -42.79237 | 2025-05-23 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4bc5712-7c8e-3e11-9e06-b87116962b5c | -6.94478 | -42.79177 | 2025-05-23 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f08709d6-63b6-34c6-a4f9-7452e1275400 | -6.22749 | -43.36552 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6e8ef2b4-4edb-3154-8534-064cfc745255 | -7.71221 | -45.66382 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0051f72a-6346-31b2-903e-440ed55b67fc | -6.22819 | -43.36121 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4c032330-d357-3def-b7d7-c3dfa4f3a4d2 | -7.06408 | -44.92759 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| be76e902-c483-3f9c-a351-5da6d6cc65f9 | -6.38705 | -43.66693 | 2025-05-23 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7d006a1-261e-387e-8b25-a5bb25fdc1de | -7.20938 | -43.09315 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 67b73935-81ac-3ecd-b5dc-8e37b2af7a04 | -5.9742 | -43.75814 | 2025-05-23 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b4e0eae1-704e-3384-afd7-ef7a5cd92b0d | -6.60651 | -44.78429 | 2025-05-23 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 230d41f1-6764-3126-a34c-cc29921f17d9 | -6.22889 | -43.35692 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2f9297eb-d722-3c3b-b93b-cc31b5138e07 | -7.7135 | -45.6564 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 308348de-790d-3d60-9f81-4ac1f9be9931 | -5.57261 | -45.20058 | 2025-05-23 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c07c5f89-5408-3146-9c82-b6ba97e9bef5 | -5.9755 | -43.75142 | 2025-05-23 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7147b8ca-5e37-3410-81be-c66dd731448c | -5.58215 | -45.19449 | 2025-05-23 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb882707-6d9a-3a1e-8667-b1ebb27e551e | -6.22433 | -43.3387 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b38a2868-ada0-311c-872e-bb9812918caf | -9.32946 | -40.67239 | 2025-05-23 04:02:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 46d040d0-03aa-31e9-ab23-ac46b0f2e668 | -7.65328 | -45.23433 | 2025-05-23 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc0e6589-7b03-3760-a660-3da4520c12f7 | -7.71056 | -45.66433 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad25e4b1-e1e9-3ebb-b000-2f32fcb94d81 | -6.23117 | -43.36615 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b20f477-5739-3378-80b5-96516d7f6822 | -7.06807 | -44.92818 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4cf869f6-855e-3680-9d05-054152bfac00 | -6.22591 | -43.35207 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2fb60bf-5bb7-3939-89a2-faf503fd34b7 | -6.03225 | -44.05425 | 2025-05-23 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcd1ffea-0975-356b-b631-ed97d941f73d | -7.71531 | -45.66132 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 05e58587-4ffa-3a8b-9aad-442b7830145d | -7.21475 | -43.12766 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 17cac205-a025-3fdb-a88a-d5255d405f84 | -5.97477 | -43.75595 | 2025-05-23 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cc194046-8a48-3e92-a555-8d5fd3fd9e04 | -7.22803 | -44.71324 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bad7f0b-c3cb-30cd-b092-50605f467dc3 | -6.94059 | -42.79513 | 2025-05-23 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44bf2fcf-3fb9-32af-9d8a-49ab53c3077b | -5.97496 | -43.75363 | 2025-05-23 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6dad3bc5-8b6c-31e6-a406-00813ece9390 | -5.76333 | -43.48969 | 2025-05-23 04:02:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18ad594f-4a67-37ed-b3c8-10e7abe559d7 | -5.78488 | -43.62027 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbea6730-6e34-3072-8f3d-c2959053cc5e | -7.07434 | -44.93981 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4a2d78d0-701b-3be2-9e75-3ca784e23df5 | -7.20647 | -43.08847 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07089cd6-f06d-32bb-ad81-b67d024a6556 | -6.94767 | -42.79634 | 2025-05-23 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2becf1cf-2b38-34c6-b11b-bb91a16e09c9 | -6.38333 | -43.66625 | 2025-05-23 04:02:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1007f5bc-08e5-3c8e-aab6-7e776d88264e | -7.36017 | -43.42265 | 2025-05-23 04:02:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed54dcdc-d3c0-3a93-986e-0c02aebc6a11 | -7.68349 | -45.64832 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5028ffd6-538c-3858-b09b-6d8d229af116 | -7.68762 | -45.64901 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e140bce6-a5de-3111-8e4e-a0298e7cc0f5 | -7.07121 | -44.93398 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b5dd12fa-d69a-300e-ab14-cad20681420c | -6.54458 | -44.02493 | 2025-05-23 04:02:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b93c93e2-6619-3e71-aca5-991438c8c90d | -5.58153 | -45.19822 | 2025-05-23 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 905f73ed-1d3e-3c3a-ab2a-3a0cec971a1e | -6.23047 | -43.37045 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a05d1f2a-bc4f-302b-8628-b02ba96b2290 | -7.20153 | -43.09607 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| de428ca0-1578-3fb0-80af-18dee89664f0 | -7.20579 | -43.09256 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1149bae6-5b86-374d-a008-9dc854270c7c | -7.71763 | -45.65711 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c15d96f-3d05-3a80-b680-99fc3f43daa4 | -7.07034 | -44.93924 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6bad7aa0-4575-3912-bcdb-d72cb96763eb | -6.22679 | -43.36983 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 0b300fd2-2e0a-3cf8-a9b1-8bc4beec8de7 | -5.58091 | -45.20196 | 2025-05-23 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0d3d1b3d-240b-396d-9a11-151df1754cc1 | -6.03482 | -44.05267 | 2025-05-23 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 000058b9-4e36-3062-b1a0-ca8c12f305ee | -5.78486 | -43.61702 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6f9a456a-18e7-38c2-b3ff-c201f75c3475 | -6.23187 | -43.36185 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0edab4e0-ac9c-32d8-baff-3256ee0748e8 | -7.23169 | -44.71051 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bee85abd-689d-3da8-9faa-69b78c4274ff | -7.39355 | -45.93136 | 2025-05-23 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 898718e1-5d4d-344c-81fb-61d77d6fab1c | -5.57613 | -45.20501 | 2025-05-23 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d177b34-49f8-3dd9-8006-34eb36bd9202 | -6.92039 | -45.81731 | 2025-05-23 04:02:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10540f81-3e2f-3d3d-a715-d231006ccf6b | -5.97927 | -43.75205 | 2025-05-23 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 381a4684-f83e-363f-baaf-b4801f77c706 | -7.71285 | -45.66011 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bad8ab72-a599-3396-abaf-e3c9c9139e3b | -8.50137 | -41.00958 | 2025-05-23 04:02:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 772e98b5-41db-3fb4-ae72-2a01228b2979 | -7.07582 | -44.9419 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4a37b76-4fb7-3f73-b334-15d4a126b999 | -5.78263 | -43.6107 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 552073cf-4f87-3e0c-9859-0d28d1a28801 | -7.23964 | -43.11071 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5db5f38a-1628-318d-b502-db6aaba19257 | -7.20689 | -43.13059 | 2025-05-23 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f1379813-6d2e-365c-af70-a5051225be39 | -6.20322 | -42.64849 | 2025-05-23 04:02:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 325212eb-f132-36c7-8806-74c5618bb24c | -7.06632 | -44.93879 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 836a9b57-86a3-3adf-a8f4-9098e7ab7ef7 | -7.71593 | -45.6576 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9395c4f2-5723-3574-b20c-ab2f40e0210f | -7.24261 | -44.7174 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e16493b2-d33e-3501-9d3b-21eb6b803aa0 | -5.57676 | -45.20126 | 2025-05-23 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ffa891eb-4493-328c-9b47-c8fbe6994a7b | -7.71699 | -45.66082 | 2025-05-23 04:02:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 40f6dd34-c861-309f-8b60-caaaa9436e6c | -6.60255 | -44.78354 | 2025-05-23 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13a0c42e-c34e-3350-991b-d944bf61c325 | -5.78184 | -43.6119 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53f93517-bc91-3389-8c6c-bbc2b99f0c13 | -5.78189 | -43.61516 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6836f787-9d65-3593-8462-742cae82a047 | -5.57738 | -45.19753 | 2025-05-23 04:02:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7dbaa707-f5ee-3c07-aeb0-c7fa99780a23 | -7.23869 | -44.71675 | 2025-05-23 04:02:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 267cf07a-2a18-3231-9c5d-176e86d0f0a0 | -6.03865 | -44.0533 | 2025-05-23 04:02:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83c87d70-0f09-350f-8ad6-bba0d6c344ed | -6.23554 | -43.3625 | 2025-05-23 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7472be89-d481-3125-8451-d099d9ad3944 | -4.17506 | -42.03139 | 2025-05-23 04:02:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c2d4401-fcb8-3f4d-bed0-296f79b7fd1c | -13.78227 | -54.30641 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0620b09e-9e52-3dfa-b7d3-517cc78afd31 | -14.03541 | -53.37299 | 2025-05-23 04:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f18d60cb-894b-3e2e-acb9-4667eebec7be | -12.06771 | -47.33722 | 2025-05-23 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b2db392-217b-325e-b668-baa73be171ce | -10.7111 | -48.82219 | 2025-05-23 04:04:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 033b6b4b-6560-34c1-8ee6-2eb14a079d91 | -11.30645 | -54.02344 | 2025-05-23 04:04:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09679b3b-1fe9-3503-9004-de9137f9879b | -11.56186 | -47.46089 | 2025-05-23 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70a89905-142f-3983-be8a-a30fbeb3fe53 | -14.86962 | -45.12223 | 2025-05-23 04:04:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
