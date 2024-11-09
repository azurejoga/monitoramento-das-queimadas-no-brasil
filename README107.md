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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 332c8247-640a-3c47-9400-37cecb96075a | -3.96326 | -48.18233 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b529c3c0-2f68-3d0b-8e1c-07e1f7cc1aa6 | -3.04601 | -53.27651 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d12a202-bca4-3db4-b2a8-e57f9f4fe6b0 | -2.87495 | -51.47419 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1895ecad-868b-3236-b429-a5bb405f02ec | -3.02812 | -51.23055 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a73640f-ea29-3273-9bdd-faaf9d269d57 | -4.06823 | -50.01671 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e720efe8-cf9f-3a35-b55d-cb0825056055 | -3.04837 | -51.34182 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317d0b60-eed7-3f51-805e-c44abba83e03 | -2.91895 | -49.36337 | 2024-11-09 05:20:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1653049f-af24-3adf-a9e1-7cb17bd8820b | -1.41645 | -54.77349 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43b6ac09-8478-36b0-9680-2547c2678b19 | -3.75384 | -52.09848 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42a69564-e780-38af-a831-48ff78b3b7c0 | -3.59163 | -47.35051 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0b84d7af-1cc4-3391-8d5b-2f45b65f4fc9 | -3.61896 | -54.79314 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5824728f-357f-3e99-af89-fff70d373ed8 | -3.14552 | -52.98069 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| a97b0573-e8d2-34d6-b89b-5f14ab442d16 | -1.62851 | -55.11491 | 2024-11-09 05:20:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4169b596-f3bb-3e39-bfd5-b3df0753e21c | -3.04921 | -54.46434 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b98219c2-daed-3788-90f6-7bbbec8e448d | 1.30582 | -50.73211 | 2024-11-09 05:20:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fd68cb8-2bd8-3feb-8644-6d39eba2392d | -3.64903 | -50.13618 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b81df41-b44c-34c9-ad0b-3417f96985ed | -3.51057 | -51.67555 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64b78a3a-1f3c-3598-8369-96898104f35d | -3.23149 | -50.44331 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b77c862-9471-3ceb-8039-7f3ffe3a8450 | -2.87189 | -50.32662 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2d6d461-5321-3e16-8688-608647c43c17 | -3.01495 | -53.87077 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 844924e1-06ba-37df-92d1-be7d9223fb6b | -3.5264 | -51.53126 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f3307e6-6d20-37a4-8df3-612191d07173 | -3.2357 | -50.26638 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 333ce698-dbb1-36c3-9f01-3578e445af09 | -3.37635 | -52.35753 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84f5b583-391e-3d9e-9ca4-2b4420ee64c8 | -1.57393 | -54.6379 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 760bdfe2-df4a-3fe5-bfaf-3dc89df15bf1 | -3.89993 | -50.31042 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a08cdab6-3c97-3845-a66a-fbd428adfcce | -3.23461 | -50.27367 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 167d4a7c-0df1-33eb-83bf-17dccbc4b1b8 | -3.15508 | -51.12307 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a5c3e07-e77f-31cd-9cd2-6d8e5547a829 | -3.59032 | -50.27113 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb22387d-4053-3ec7-bc84-f84c6b31fff9 | -3.20779 | -50.63636 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89d8eb57-d358-39c2-a85a-0c1ff544f100 | -2.72681 | -54.14553 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f53fb7ce-a1ab-398d-8330-860d65dd65b6 | -2.40874 | -48.53143 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a21a3cc2-02e7-3dea-8c11-df94258e8277 | -3.34876 | -50.26528 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0065f349-9466-364a-8b01-4bc61ced10c1 | -4.20362 | -50.6245 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d97067a-dc13-32b3-984f-c8eec77a4f7d | -1.82508 | -52.03007 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4df5b5c4-b01c-36a3-ba43-6e03b264a23b | -1.32192 | -54.63774 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0b45cbf6-3fc6-3827-ab95-013f20ea24fe | -3.11817 | -50.14766 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c1bb19d-15c1-31b4-aafb-7daebefd713a | -3.29315 | -46.42154 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1837487b-e1a1-3de9-81ee-3f34c1a3e7dc | -3.5884 | -47.34631 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 875fb387-1bd5-3667-b418-f415b0876608 | -3.15928 | -54.48038 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac24c320-bdc5-3497-b2d5-e40c835d98d1 | -2.61427 | -51.30107 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1675ca76-5792-337a-887b-ced2fc12a071 | -3.11318 | -51.29334 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d941f6c3-2d52-3656-bb1e-31db056676ae | -3.32071 | -49.91206 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa08bb8b-c3ab-3243-b5f3-7583a2b2bf32 | -2.8703 | -50.41214 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81a42a4d-7311-3094-adf0-d951db59ee1f | -3.2876 | -51.52569 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2c61afe-f9a3-3482-ae76-288fc482db2a | -3.21227 | -54.05151 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70d503e4-2b9d-3900-ad89-50fc924e9924 | -2.06495 | -53.28243 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68094b25-b1c9-3a31-b9b0-62125cbb5b1d | -4.6287 | -46.54094 | 2024-11-09 05:20:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64be2b91-1085-327e-82a4-8efd009fa3e4 | -3.25116 | -46.47669 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a411282e-59e6-339b-a077-73084d0b0c7e | -1.21785 | -51.7758 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de07a4b2-1607-3fd9-8458-0eb4d59820c0 | -2.7672 | -54.04922 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23dfc574-e360-34ec-9930-c62161469155 | 0.62457 | -60.08999 | 2024-11-09 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 016ba79f-2ad7-3a77-8ce1-8acfda0c4d7d | -3.24728 | -50.44922 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c72af29-3aef-31b6-ad1e-4e676c1af299 | -2.58673 | -54.01226 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6caa592c-32dd-371f-a0fa-1e77fc5ae2f9 | -3.22979 | -50.30595 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e00feaf6-543a-3083-9aac-04405198b9de | -4.82779 | -47.32735 | 2024-11-09 05:20:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9d25a03-e10d-3848-b378-e82952767726 | -3.45546 | -50.37954 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8096fb3-a691-3009-bc3e-57173a2af6fb | -3.24349 | -53.40016 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c364028-75ce-38d0-ac45-858ce0b02d57 | -3.03935 | -50.36955 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7668a2af-5d97-3e4b-84cd-113e1f3a8693 | -3.0302 | -51.53316 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1042f3cf-c889-34ed-8638-be02510ea257 | -2.40082 | -50.31398 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 491f2fc5-7c23-3cd0-90f6-450c87163754 | -3.18706 | -50.44313 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b273072c-da3a-3b54-8bc3-c0e8995dba47 | -3.39911 | -51.5964 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c712212b-487e-3bbb-a198-c71caac74aae | -3.58414 | -47.35543 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 6bfce89c-03a4-37bb-b2ab-97711a22ba3f | -3.17589 | -51.31315 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65c7338a-9bc2-342c-880f-0960927f27a6 | -3.17644 | -53.85445 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75d96d21-0228-3176-b98e-c0c534b23e69 | -3.11574 | -53.71386 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f431e062-60b3-388a-8e6f-4f27c199d2db | -4.29576 | -48.64928 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4e4e472-3d64-3a26-9b1a-a54e04ad627a | -1.52229 | -52.18439 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5d984e67-9de5-31f8-be10-d0c7e6fbf0c5 | -3.04034 | -50.32638 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d1d7d93-af75-338b-9eac-8ab468293979 | -2.18549 | -53.58322 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67cae88e-0b2b-39d0-8e91-ec60bc0f3645 | -3.40298 | -50.01728 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8565ef69-11bd-39d6-95de-43fc2085e3ac | -2.85919 | -48.45384 | 2024-11-09 05:20:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7be1e939-f442-3acd-9cc2-6c9d81a868d6 | -3.9577 | -48.17586 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe7b9198-a15b-397d-ae6b-8b1282ee80a7 | -3.90048 | -50.30671 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d15550e-a353-339a-bf7d-7c1303be65c2 | -3.7304 | -54.22593 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 837e0a1a-f843-3195-8fb9-1a5a87a09913 | -2.62789 | -46.77421 | 2024-11-09 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5f2fa98-4898-3df9-9af6-7a3ca3166f4c | -3.20241 | -50.63568 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19744e8b-4e0b-3640-b391-c8d0e866dd0b | -1.70994 | -52.49126 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66f83dda-3850-3d61-bbaf-702ca9f21bb7 | -1.38093 | -52.1999 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f19a0755-f0ec-3478-9f8a-e5a592bdf6fa | -3.22411 | -50.38131 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3449153-9b4f-3492-ba92-4de41040bec9 | -3.55584 | -47.38293 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f298dbd-da1d-3cca-88d5-62c5d372236e | -2.81479 | -52.96557 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e836807-a764-3d00-9628-259abee9bda8 | -2.88905 | -48.29631 | 2024-11-09 05:20:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac2c90c7-fe73-35f3-aa52-c81264f99598 | -3.40916 | -50.01433 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 125df1e5-f1cd-37f8-8aa6-5e7127194ba9 | -3.00837 | -53.43985 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3fbccc8-f23a-32eb-8cf5-dda313ddc37a | -1.50726 | -52.15666 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc54afc6-ea67-390c-bce4-317da97ac8a6 | -3.70751 | -54.34814 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bfe3ef3-d1d3-3f58-878b-b2fa991515fb | -1.73509 | -55.02444 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90277cce-f290-3477-a893-fdc24177f838 | -4.19624 | -48.55811 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 267cd4fd-d730-30e4-a2b7-6bdf0383f367 | -1.3211 | -54.64286 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49194242-5ac1-3fef-8adc-231e698918d0 | -2.1614 | -53.65457 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 752a84dc-2044-3a8d-8361-22d5f5a13e2a | -2.86592 | -50.32933 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a837f38-f442-32e4-89cf-e2d7ba61c054 | -2.77141 | -54.04985 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b535fde6-dfaa-3f78-8702-45e9ada5d600 | -3.04717 | -50.36412 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7781dfd3-0ac5-3a92-8d8f-002b91915197 | -3.24415 | -46.47584 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44c508dc-f5cf-3c74-a4ab-d8d9dbd105c4 | -2.23198 | -50.52366 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a65d15e9-316e-3e16-ab8b-03b633d12000 | -2.88043 | -51.30686 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c883fabc-7b16-342f-8734-e0ce4d5c194a | -3.63512 | -50.75656 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57154097-cc6b-3832-9a76-891a8bb0eb33 | -3.78657 | -51.2896 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 170da1ec-6983-3b0b-9d9b-4fb7a7ee74cb | -2.87955 | -51.47797 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README108.md)
