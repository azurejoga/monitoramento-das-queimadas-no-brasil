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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70f6de92-f9f2-331c-b9a8-17eebda2892e | -3.42884 | -49.04927 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7b2c1bc7-58aa-3af3-b5ef-5a34fa1ef827 | -6.89096 | -59.14892 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd2f66b3-6618-38fd-aa2b-ac6a763f1c38 | -7.24356 | -57.67037 | 2025-08-15 04:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81843324-60bb-3a46-b2d7-5d9ce15122b2 | -9.21608 | -45.33368 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5196671d-824e-3fff-b0da-e7d755afe526 | -6.07784 | -59.96022 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fd7b8d0f-6542-37d5-8cb7-082eff882be2 | -6.93208 | -59.54138 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| bed46cc1-801e-3f52-ac8a-d956b5ad1b45 | -6.21825 | -43.33789 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 787a5057-128a-3d42-aa15-b09904251474 | -7.2925 | -41.58683 | 2025-08-15 04:27:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e7aa2ee3-1bd4-3bea-babe-befcb36fd2ee | -7.3977 | -44.86636 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 776c1967-9ab5-3c5a-957d-2a8d4d96fd35 | -7.14724 | -44.40358 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64efe393-05fa-382f-b5e0-f8ddd4b4958b | -7.38961 | -44.86924 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a83aae2f-966a-3161-a54d-e011bc88a18d | -7.86749 | -48.23003 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a78e723b-bb60-3b00-b744-ce89c90b958e | -5.36976 | -41.23227 | 2025-08-15 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b1a2623e-5a53-3e42-8991-359c02ff29af | -3.95914 | -41.47795 | 2025-08-15 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 95cba929-df87-3bbf-a5a5-c16b2f0b8e88 | -6.07628 | -59.95264 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 9a5b4694-706f-3d68-93d2-ffdaffafd624 | -7.02707 | -44.28229 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9186dc57-cdf2-3979-9b5f-1eae58b8b382 | -6.67057 | -58.81779 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbb4f6c5-72ae-38b6-87d3-9b1247eac2ae | -6.24413 | -43.22884 | 2025-08-15 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4630b5b6-25ed-39d4-af5e-6a35bf71d788 | -7.28852 | -41.58623 | 2025-08-15 04:27:00 | NPP-375D | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 389b3d6e-6a8d-3eaf-928f-7b50755bcc48 | -6.93591 | -59.63655 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c223f0d6-db7e-3a30-9f35-c02a111c917f | -8.29042 | -45.00268 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6141ce3e-0b67-31da-b42c-e6e4fbfe3472 | -6.33053 | -42.79972 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d9f78be2-eeaa-32c9-9cf0-061fcc2e7f33 | -7.29758 | -60.62526 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92874667-0a48-30a0-8a0c-41d3b800d1eb | -3.44887 | -48.97204 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b14e38e-6a25-388d-9c48-cb6946672a4f | -6.72705 | -58.82996 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96da880a-8944-37a7-9256-c93d57449be5 | -6.64961 | -58.81983 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11a45c67-6c42-3583-b8d1-59f49f91c167 | -2.91104 | -48.30056 | 2025-08-15 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f79baf4-73be-3173-a7a2-406e7e3a4c4a | -6.89299 | -59.1503 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3212c042-325a-366c-a9d0-f3f6d090a080 | -3.32123 | -48.72237 | 2025-08-15 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3186e1e8-ff2d-3999-bec7-5126813a0ad1 | -6.91109 | -59.15306 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69f60021-ef4e-35f2-b235-5eb81143c995 | -8.52287 | -43.29414 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 97cd9e67-0490-3c19-b214-2e71920333bd | -6.33846 | -42.79672 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24088b23-8c0c-30ff-b556-60bd43069b70 | -7.2888 | -43.8232 | 2025-08-15 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 252b6750-7645-3363-9cb4-bc67b6f04337 | -6.93212 | -59.53633 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 2ed3335d-5aa0-38ad-8667-b6859df10a59 | -6.90547 | -59.14573 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01e1c647-5034-3348-8f65-584feb03eebd | -6.90641 | -59.15307 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 044915c2-fa33-3e93-adfa-1f57bd331f4c | -6.10875 | -59.9366 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6325c613-ddc4-32e7-98cb-98dfa8b119c4 | -5.54164 | -45.37206 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbdfafec-02b6-35a9-b4ec-82dc7091272b | -6.91896 | -59.1481 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea14c884-8bd2-33a0-bcf0-b005e419628b | -9.74773 | -48.57402 | 2025-08-15 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad6ea128-fa7c-3589-8467-cc5a8b288320 | -8.30911 | -45.01681 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cd3601f-3b37-3553-a070-a80dd47e1195 | -5.75974 | -46.66827 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fe722276-09d6-3c18-bfd6-2261b7101b74 | -9.03042 | -40.52284 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dedc462f-9ade-37d9-b62b-457a11815f60 | -7.32034 | -44.68662 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2967c386-a5d8-3488-890f-da8465d2ba34 | -6.48916 | -42.86175 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6252d72-06b9-34a4-82a2-ace3a59abcb9 | -6.89658 | -59.15618 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f62c008-df16-319a-aadf-af47cc75a94f | -10.53725 | -42.5512 | 2025-08-15 04:27:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 01b6904a-dae3-3357-ad3e-a7048501ba29 | -6.06923 | -59.95083 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e9114ec9-bc13-37fa-a0ce-ab48bb7d9cdd | -4.38969 | -41.91378 | 2025-08-15 04:27:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cffc3248-d6de-3bd9-b96f-a8f2ab85b20f | -5.37297 | -41.23794 | 2025-08-15 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fd8ee14c-7af0-365c-9fbc-2139eae84305 | -6.65856 | -58.8275 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1c820752-2bf8-389e-8fe7-9c779a989c57 | -6.92519 | -59.53526 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2011d3b8-46ea-3279-bc96-308b3b98d110 | -6.66181 | -58.8279 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 57ee0f6f-e00a-349c-bb5d-5fb45159760b | -6.94134 | -59.5298 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6b0c3432-aa37-3348-8b0c-f4b8dfa35103 | -6.55252 | -49.50389 | 2025-08-15 04:27:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbf0efd9-b358-389e-8f03-365f0284a9d0 | -5.54109 | -45.37555 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b454d8b-7241-3d24-9fc2-be7466da7363 | -7.08271 | -59.22482 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 517f5c35-be30-3702-ad4b-fd0005ec4c91 | -7.3048 | -60.62693 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 245d133c-fa4a-343d-a762-ef59f73932fa | -6.6688 | -59.08698 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba94fa84-81a4-320a-83bd-a716ecea761c | -2.58355 | -51.92317 | 2025-08-15 04:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58e70ebd-94ab-395c-b093-0e03e2038858 | -6.53962 | -56.19803 | 2025-08-15 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 445471ee-9cea-346d-bec9-fe179568849b | -6.86929 | -59.84039 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaa1bce3-3def-333b-8afa-239e56e5443c | -9.18899 | -45.32947 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| defbdec2-bf57-3bac-ae8e-72bce1c407e9 | -7.38847 | -44.87652 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db42885f-e4d7-3d17-8dbb-fdb7153f3995 | -6.96752 | -42.8694 | 2025-08-15 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 50d95fde-44b7-3c88-b49a-c8da9d5d1d6d | -4.6678 | -48.86449 | 2025-08-15 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86528c17-1579-347d-b536-3e68ce6c89c0 | -7.85603 | -48.23577 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b3eba26-2019-3452-a01b-f3f659860fa0 | -8.52351 | -43.28983 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b17a8b17-131c-3fb2-aafb-92376bb02a73 | -6.37267 | -43.38427 | 2025-08-15 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58e10a4d-1a69-3919-b776-c009aab69d98 | -9.03539 | -40.51927 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 42cbfc5e-be4a-3ad0-b0a4-1e1bf06b934f | -6.96231 | -43.8634 | 2025-08-15 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92d2def6-79f8-3691-b263-c9d71e2f5215 | -7.0816 | -59.23079 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ed75721-985a-3d72-9d50-8a295a2706c7 | -6.09619 | -59.94155 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24811065-5335-3075-ae20-a0d237a2a09c | -9.9574 | -48.33736 | 2025-08-15 04:27:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4198238f-3872-38de-a1db-7be6c1b87b30 | -3.43326 | -49.04549 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b4f2f105-82e5-3973-bb52-0c9878871d09 | -5.60089 | -45.38128 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f1b5db8-b3e1-3ac6-8a88-a722d2833339 | -5.54552 | -45.3691 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84071db9-6c4d-3758-ae14-27df602f33ee | -4.48137 | -47.67039 | 2025-08-15 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8521cfa9-9c96-39e3-a40a-f689939d8291 | -6.72246 | -58.83372 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b129eb8f-da1f-3ee8-9e99-dd06e14be411 | -7.07596 | -59.22357 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bc48aa24-10f6-3c55-acb4-b4a7e22c9f23 | -6.96321 | -42.87317 | 2025-08-15 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 8f6c7deb-0eb4-3b7c-a00f-46f822e0a2bc | -4.43586 | -40.92433 | 2025-08-15 04:27:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 366eae13-5868-334b-9253-9052f3535657 | -6.93084 | -59.54295 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 7c0f57f7-77b5-3674-bce8-de2117db8759 | -7.07817 | -59.21172 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fe1cfed4-3028-340a-9c61-a99dcaeaf312 | -9.04035 | -40.51567 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ed20be0-b2e8-3831-8cdb-cb8b2d263155 | -7.14836 | -44.39621 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23e64f69-7311-3d61-99ec-8acaa42576f8 | -6.92395 | -59.54172 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1f8e316-11fa-376d-8816-b045ca8b3cbe | -6.88203 | -59.15948 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c5253c1-c18b-38e9-8e67-f416b2c0ec1c | -3.08036 | -48.84768 | 2025-08-15 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45fd83b1-39e7-30a6-8f10-e3ab2d3d84d7 | -9.00745 | -48.72251 | 2025-08-15 04:27:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83076d06-c49d-30f6-b014-fc51239da40b | -7.29033 | -60.62377 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbba467d-6bdf-34c8-94be-74c2d4882fc5 | -6.92636 | -59.53378 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b3e414f2-5eeb-309e-9d97-8aac6b3c42fe | -7.07707 | -59.21762 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2e3c340f-b5e9-39f1-83d3-a2ebdd6134ba | -6.41508 | -42.8076 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a1c8273-1825-3ad5-bef7-497e4a0b5d4f | -7.38622 | -44.89101 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7ee0547-283d-33c1-9e67-f10a55d90797 | -4.39507 | -47.77643 | 2025-08-15 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee7528c4-f7c2-3b3b-99ae-bce1c228f6c8 | -7.32808 | -60.62346 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6c2b88a-0f5e-3e9d-b043-ec5914892ebf | -8.36836 | -42.24605 | 2025-08-15 04:27:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 143bda9b-ffbe-3fbf-bf7e-3a12efe99465 | -3.08135 | -48.84872 | 2025-08-15 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b1003b2-0225-3ec0-8c10-38b6a614770a | -9.85262 | -47.82291 | 2025-08-15 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
