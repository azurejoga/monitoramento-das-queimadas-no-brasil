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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36dbcb32-4836-36ab-90ae-660c6a40aa0a | -3.38602 | -53.27272 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bb00c66-600c-327d-bd3f-47344e84f9cc | -4.44324 | -49.27535 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2c6c8a4-cb27-39e4-9337-09d82e1fa689 | -3.19749 | -54.32977 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9fdc1de1-1972-3c23-b9c7-55df1e181ea2 | -4.57047 | -48.01946 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| aeda699a-0556-3f80-b63b-881f42e3910b | -6.20721 | -45.3767 | 2024-11-21 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e2fcbca-909c-359d-9078-2e121d49f988 | -3.61805 | -51.08704 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7c5655c-16d7-3b03-90a9-93465655fd3a | -3.27991 | -53.84851 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdc0f3af-c71f-3920-826f-19d42ffa2b23 | -3.23968 | -53.51457 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cd51e31-3e05-36e8-9e7e-1d94d14ef77e | -3.28142 | -53.83914 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12e343a2-0321-3a96-8cc7-cb4fa1981f2e | -4.0889 | -51.08533 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37ee4097-30a0-34ea-b02d-9545b86f663f | -3.22489 | -53.83999 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f81e4e3-7e74-32e2-b2e3-ccd02a5fc44c | -4.09517 | -54.04597 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9b52219-7cb4-31e2-9f60-5034cc09949c | -5.93901 | -46.19378 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f828e9f-8c6f-3efc-af01-0fd506fc1333 | -4.95111 | -46.72258 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 930a73b4-22c6-3384-b428-7ae82c10f257 | -5.93743 | -46.24903 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fae5022-1de6-3f7b-84a4-f09af84b1dbe | -3.29291 | -53.85537 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68583e42-2350-3ef9-ab32-74cd996e0e3e | -3.19377 | -54.32286 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 578322df-e032-3606-a072-970b6101c51e | -4.39109 | -45.59583 | 2024-11-21 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 097bb151-a626-33ec-9527-1d51bbad84b8 | -3.60255 | -51.56083 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3435b213-9f34-3d52-9899-2f6d72c0acaa | -4.39166 | -45.59217 | 2024-11-21 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf2d2bd7-e2e2-30c1-bc47-f87c5419326e | -3.394 | -53.71854 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de0d5d1e-81ee-329c-aa70-6c4821d175f0 | -4.0606 | -49.28124 | 2024-11-21 04:31:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ae34e8e-d2eb-3714-a1d2-67b3945a2827 | -5.03504 | -45.91997 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 183fd9dc-5778-34f3-894c-8a2e8a968ba9 | -3.0481 | -54.40678 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b2dd740-6666-3fbe-a76a-4b67a1245222 | -3.75769 | -52.41133 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5202af76-e47c-3401-92e7-0c5a7727b4a2 | -3.66395 | -50.44415 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60eda5da-f7a2-3de8-9426-d6ae92e8b022 | -3.64022 | -51.45159 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c16221a-2da5-331c-aeee-20c0bd618ecf | -4.38948 | -47.77294 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecb9bd0b-cb68-3bb0-8d66-026c8c5821c2 | -3.83802 | -50.01476 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b58d7865-e619-326c-9f9c-9bf052d34e5d | -3.80174 | -52.22121 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8715508c-64f2-3b4a-9ab5-5794f0202708 | -3.91124 | -49.0403 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc01451f-ca1e-3498-b8ee-44f6fa179483 | -5.71731 | -44.80984 | 2024-11-21 04:31:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 71086e8c-120d-39c3-8e0a-5e4cff03f102 | -5.87533 | -40.0392 | 2024-11-21 04:31:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf9ac7bb-9ec2-30d7-814f-e5eefeb71027 | -6.20274 | -46.22348 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b39ec47-d5c8-3f0d-8b14-3a155d37cecc | -5.22292 | -44.90909 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce6e11e1-8aa8-3389-9573-a5a66ffedb55 | -4.76743 | -46.44714 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9739f76-ef6a-33b4-9714-657efd108b87 | -6.30318 | -45.34047 | 2024-11-21 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13c36185-cb65-3038-885f-b3fab3d896ba | -6.82218 | -46.77877 | 2024-11-21 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea5bb68f-3540-3c8b-ad78-327a8300a30d | -3.6683 | -50.44047 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dde7f911-bb11-37b6-85e0-90398a33df71 | -3.28749 | -53.83055 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 884484d2-b631-3162-99f6-ab5365ccb4b5 | -3.11671 | -53.70092 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebc63889-ddcf-3a0f-9601-3b3f5bc6e93b | -3.10072 | -53.74072 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12c8fb38-042d-3e27-a22e-3f10ad8b2f8a | -4.76798 | -46.44363 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05390464-fc9a-3ccd-a82d-c8e720d083e7 | -5.42738 | -45.34415 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20ae460c-7506-3ead-9994-0fe1f24027ba | -5.61698 | -45.08944 | 2024-11-21 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7245e92b-33c6-306c-ba5e-ed62bb1f88d0 | -4.43426 | -48.30026 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a56402-7f89-39f3-825f-6d06b6708ca7 | -4.33884 | -50.42203 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dd51db5-7760-3d15-b388-a775a1b57d13 | -4.35398 | -48.31992 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e641ba5-be5b-3ba2-af84-7468e72404fe | -4.9019 | -48.38786 | 2024-11-21 04:31:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf578d21-c1f7-364b-afba-df34fc90d53a | -3.54757 | -51.52977 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f70b507-e49d-3b95-9fce-1751a752c2fe | -6.03467 | -43.38899 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 81817fc3-361c-3855-8cf7-1ee345e703c8 | -3.94949 | -51.22602 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8831494-b2ac-35a2-8f8a-f763f4db9c7d | -3.82499 | -52.25785 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a8bd7f9-29b3-39ed-a735-853bb4dedebe | -6.31807 | -49.67418 | 2024-11-21 04:31:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d10cb990-ac63-3d62-819f-6fdc895bb206 | -4.79543 | -45.79847 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ff3ea91-e944-3adf-b2cc-423ad681c288 | -4.60921 | -45.74031 | 2024-11-21 04:31:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9a3e58e-29ed-39be-bc09-0fd42812abd0 | -5.62209 | -43.9519 | 2024-11-21 04:31:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 191e7741-635d-317b-9459-00b7840e541c | -5.07809 | -47.93913 | 2024-11-21 04:31:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da1f3b46-d6f2-3a18-ada0-dac108a473d0 | -4.3944 | -45.5964 | 2024-11-21 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 09256372-aeed-3e5b-b072-6f6008156eed | -3.52049 | -53.8056 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 650f905f-c121-3f91-9fb0-047aaab2e8f0 | -4.10691 | -51.04617 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c91a1767-65f2-35f0-9a77-ecdce3bbdd31 | -3.29325 | -53.84745 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b95fd8ee-9ef9-3fef-bbae-a10fe3fb7fc4 | -4.8886 | -49.90063 | 2024-11-21 04:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc653be4-33ff-32ab-8bc7-ad254a9e4b1a | -4.38616 | -47.77242 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b495dfc8-828f-344d-b092-4c33ba0e2663 | -3.47384 | -53.28126 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f22e764-8e3a-335c-9ac4-13f47201b0f5 | -3.48427 | -54.69973 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa049a74-3847-3c52-90a0-f4853ad73266 | -4.2263 | -47.18088 | 2024-11-21 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa41ce7d-c03b-3b0c-a9ce-c23b6c45aba2 | -7.56971 | -49.4042 | 2024-11-21 04:31:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 310e040d-47db-3fb8-ac2f-1a98bc0a21cf | -4.13631 | -47.73006 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1671a8da-04f0-3fb6-9512-0384986f0bcb | -5.41114 | -46.44182 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85b46675-4129-3552-a5b5-5a67162dac5c | -3.27225 | -53.83775 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30fb254d-e6ff-3d97-b60a-62b9faa8a8fb | -3.99291 | -49.92659 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 023cea19-d97d-3c38-b717-0c55c7c363cd | -5.50474 | -48.36092 | 2024-11-21 04:31:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7370715e-ccda-3259-9883-5489cbd0b406 | -4.95322 | -47.80494 | 2024-11-21 04:31:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a201b987-9ab6-34ac-931a-6269ffb718e7 | -3.41919 | -53.28458 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d656417-4b6a-3ade-b426-72330e4d0d91 | -3.3818 | -52.46197 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc1e22b5-63bf-38c1-b08b-c07c775c38c8 | -3.70927 | -51.84181 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c19d3696-b067-33f8-ab80-ef757a0daaed | -3.46455 | -52.72603 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f86b9b66-5a16-3e98-8d9d-af3fb6a14ae7 | -3.54993 | -51.43986 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6485947-38ae-3429-90fe-1ad7b1eaaf1d | -3.4694 | -54.54755 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9db1ad27-057a-31f6-8b4c-a968fb8a0bf9 | -4.96308 | -49.84355 | 2024-11-21 04:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5364fca4-2e94-3e18-9f1d-a86b4a98520f | -5.17305 | -51.99583 | 2024-11-21 04:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f39b77de-8069-31ff-8739-792c687c3ca7 | -4.00357 | -49.92831 | 2024-11-21 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72643a61-ae8e-3799-abc3-caf589a5af93 | -3.29024 | -53.83739 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d68b52c2-f754-3d95-97f0-2e881a10e733 | -4.63479 | -49.54493 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3fc7c70-0355-3d2c-9390-15d709d03fd7 | -3.28409 | -53.846 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e21b62eb-4d22-3daf-8ad5-015c8b70a759 | -5.52214 | -43.32683 | 2024-11-21 04:31:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 868a711c-24e7-344a-9916-e8606571fe25 | -4.10112 | -50.74211 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 114525c6-f4d4-37ca-b291-ca6be3c9aac1 | -11.51574 | -48.1308 | 2024-11-21 04:31:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8cd8098-ab40-3503-9f34-36f9c63030ae | -5.0443 | -47.95872 | 2024-11-21 04:31:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8a38a43-6abc-30b5-8145-bfc4f6ed326f | -3.81622 | -51.35594 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cde03cf5-79c3-30fc-842b-da49af84dcec | -5.27611 | -45.44914 | 2024-11-21 04:31:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 511fd028-888e-3a19-a96c-94ee61e53e63 | -6.61032 | -42.38353 | 2024-11-21 04:31:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a3ed28d1-07a1-32d3-8a35-40f44c469933 | -5.80901 | -38.32788 | 2024-11-21 04:31:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f1535b22-dc52-3e95-8980-e544adcf1b1b | -3.29132 | -53.83595 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b502562-3ca1-3268-988f-e3620f183e0a | -3.75053 | -52.32768 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d374ae4-94cc-3c23-84d9-2e54616c3b10 | -4.1265 | -49.43476 | 2024-11-21 04:31:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6e1a050-8491-3585-81ba-500250096b7f | -5.9467 | -44.24742 | 2024-11-21 04:31:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b573b066-794f-3244-9b20-9629fb7c236f | -4.96485 | -45.51669 | 2024-11-21 04:31:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f13485ef-3897-3ef4-bad1-d9d1c1052088 | -10.7319 | -49.51651 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README49.md)
