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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 459762f1-3eb6-3f12-9fa4-6d016f33d949 | -6.82874 | -52.812 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8872873-98bf-3b11-a55e-7203f5b1cf5f | -6.85276 | -52.82433 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff9f5f44-0471-33ca-962d-af24f722e383 | -6.82511 | -52.8115 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ad433fb-b653-38d2-8d9c-cba1e1128ea2 | -8.05816 | -52.36423 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b252aee6-ae9a-3088-9242-567d12fa861f | -7.71086 | -45.01208 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5ef0205-eac7-34a2-8609-a08b3bb8c93c | -9.28422 | -47.08778 | 2025-09-02 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bca93b1-b6f6-3019-bdd7-4a856f3e9734 | -4.41577 | -54.89318 | 2025-09-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 631efce6-b47f-349b-8d5d-d4ca9692c257 | -3.21685 | -46.83062 | 2025-09-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 242908aa-55d0-3ac6-8b6e-32a18b723213 | -7.87097 | -47.96357 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d98e0300-c15e-374e-8d20-cbeafdee967d | -7.79225 | -45.45214 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c42ed4e0-414d-35e5-964d-68f64562d98d | -9.12918 | -46.05461 | 2025-09-02 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b41dd2e-0642-390a-93da-73c8c1f53970 | -6.40367 | -58.20711 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d23a1af7-8499-3581-ac48-f318562c74d7 | -8.71749 | -50.45145 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58316499-e252-374d-86aa-59b307282994 | -7.76482 | -49.48722 | 2025-09-02 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81efb21b-2c9d-3560-af9e-8597e777db2e | -7.76935 | -49.48783 | 2025-09-02 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61265c0d-9343-3be0-afea-63edd4895b64 | -6.87915 | -45.85794 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c44b5fd9-b635-34b1-a89e-c340da9cff23 | -4.30937 | -48.09801 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 549a1f5d-8672-32e6-9ada-765518794374 | -6.7928 | -44.6198 | 2025-09-02 05:04:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88083b37-769e-33b7-87c4-265640ab5d4a | -6.33964 | -58.17027 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8522713d-8b85-3ac9-8835-3c627faeb741 | -7.4183 | -44.80797 | 2025-09-02 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0afbf8d3-54fe-3682-b9b0-d6f8e310c137 | -7.78865 | -45.45109 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1747b190-591c-33d5-9d1c-aa08de52ba56 | -6.85657 | -52.79926 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c9f47c6-d463-30be-890b-3d4b789991c5 | -7.92207 | -46.45121 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64d5d7de-0d0c-3d77-8635-b0958da0453d | -2.90405 | -48.29623 | 2025-09-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bb9c385-6b89-317c-9950-dbe3e66f2f49 | -7.78272 | -45.45015 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98a9e0c1-b975-32e3-9a62-e5da7f908d4f | -8.46235 | -47.37434 | 2025-09-02 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6381a165-4880-3cee-a9f4-c5e411bb8956 | -5.01042 | -47.6445 | 2025-09-02 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61ac01a3-a74c-3462-88f6-bd0fa05904b4 | -7.55993 | -45.69506 | 2025-09-02 05:04:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eda9d7c0-62d4-3a30-8271-5f4a3de06b8c | -6.75617 | -56.39706 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69edcae1-3cbe-3fa1-9c56-e77f315925c8 | -2.55851 | -47.71631 | 2025-09-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 159515ea-f15a-34f0-9dee-277b3dfa83cd | -6.71765 | -42.266 | 2025-09-02 05:04:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 247bdd53-6180-3ef1-a64b-038c32dc4172 | -6.43555 | -55.6417 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfb65a52-3474-3608-aa71-e3c5528de235 | -6.85359 | -52.79456 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7703fa3f-59d1-3a29-ab81-c85446061392 | -6.84853 | -52.82787 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 005f226f-b51a-3683-9060-4944261096e1 | -6.21835 | -43.36763 | 2025-09-02 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea9c350d-f69c-3ebd-bd92-591521dae694 | -6.80216 | -52.8166 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b09bca0-6ccb-3e97-a422-7333057a1619 | -6.98543 | -44.3362 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 337b96d3-0e15-3959-9af7-71a9d91e73da | -8.35135 | -52.53085 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75d0cf94-6805-3a69-9e49-4ca7a82484e9 | -6.82983 | -52.82925 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8900b410-19d3-380e-9bac-51c83ffac227 | -6.47748 | -56.0059 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed01e436-5f79-399f-bfd7-74146eac3f72 | -6.84809 | -52.80639 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 019777ad-c4ad-35e4-b668-ec06feffbd07 | -3.22149 | -46.8344 | 2025-09-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bb4c1c5-7f88-39eb-8a64-377df3e2f398 | -3.23452 | -47.12852 | 2025-09-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| f447ef8c-31b2-30e8-85d8-d23e9cc4b5c7 | -8.71229 | -50.44464 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b795786-543a-3974-b693-ed9cbecdbd49 | -7.28094 | -60.66146 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 968405e2-d8cc-3fe4-8cf4-5f563f38956b | -7.98015 | -46.4753 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6a538bca-61a8-30a2-835e-256e99a712ae | -7.71023 | -45.01331 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeb1dfa8-3532-3906-b500-2ae897296337 | -8.88646 | -47.97038 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbf6e068-5232-3880-89ac-7ef8097c214f | -6.40306 | -58.21091 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4ba048e2-030f-3a26-b72d-61a6df6ef116 | -5.32476 | -55.99961 | 2025-09-02 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af949d68-df16-30dc-85d4-79649ac56ffc | -7.25485 | -57.54315 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d4f3f07a-a81f-3461-8eb2-ba580e065447 | -6.34947 | -55.56102 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73bbed17-3fbb-31dc-a92f-54262093122f | -7.99277 | -46.46563 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a7ab8a5-4c10-3f14-96cd-a7e8d4e44a29 | -6.19651 | -45.38903 | 2025-09-02 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bd0c6ce-6489-3dee-8097-717d63cd3df6 | -6.86029 | -52.80659 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4871152-7373-3aa4-8c80-129dc864c961 | -5.38292 | -46.28424 | 2025-09-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b84a9359-b06a-3999-a90c-7131d1451a0a | -3.59629 | -49.45894 | 2025-09-02 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0000176-1783-3274-af57-58caf95eb34f | -6.87457 | -45.84892 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07173284-fe96-3859-91b9-4df753779178 | -6.80452 | -52.82554 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05449fce-3e33-3e24-a313-911aac814395 | -7.71197 | -50.25786 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94e8b80d-555c-3f05-9ab7-b7235bb44625 | -6.87525 | -45.85853 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11712ef1-2e80-3483-b2fc-054a4e825b8d | -6.04077 | -52.17802 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49704b51-8f2d-3510-a65a-e8e9c7f424de | -8.46323 | -47.36782 | 2025-09-02 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 970fc273-cbb9-3190-ba38-54f4f3af8d2d | -7.3502 | -57.62822 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 276ba685-24be-3c7c-9a78-1a3f83c0e907 | -7.98762 | -46.46155 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8eaad13e-4089-38f4-afcc-86ea07e04bc4 | -9.1123 | -46.04757 | 2025-09-02 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8590546c-1921-3be7-b49c-c54ba789f264 | -5.85059 | -43.00616 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a3370d3f-c97c-375c-b47b-de3fedc6c980 | -3.2341 | -47.13133 | 2025-09-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| ae93f1e8-7ec7-3a5b-bac6-e55762ed71ec | -6.81237 | -52.82249 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01b1f50a-c1e0-3766-be0f-caf9946f9fd9 | -8.13242 | -45.03732 | 2025-09-02 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e45dd9eb-ac65-3784-9552-5cdd63d009c9 | -5.74915 | -50.20436 | 2025-09-02 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 160b9ccf-282c-359b-b43b-6fd861818764 | -3.7909 | -49.42783 | 2025-09-02 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24f03d99-81af-3ea2-aca6-ceb68a1fcc3d | -4.31165 | -48.08287 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c25f049b-cc3a-3b09-b2d3-dea7463104e4 | -6.87276 | -45.56156 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1d9263f-a205-33f6-8786-8b55dbb283ba | -8.81654 | -47.48688 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de33a885-8009-3d8a-824c-24a77bf99cf1 | -6.4327 | -55.61649 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f823246-8c05-3fbb-b642-c4a2172a5585 | -6.82134 | -52.83654 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4fd86eff-7d59-3425-9f3d-348cb9b162cf | -6.82197 | -52.83236 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e316f99-9839-3859-afe9-f3b3b2c16c32 | -7.57495 | -45.22932 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef88aacb-12a4-33dd-99ca-5b7ad6e43393 | -7.99181 | -46.47301 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 90b8f9d8-2efa-3333-9b44-65300779a770 | -7.63292 | -46.55124 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a09408bc-ca2a-392d-97a0-f226bdf8864a | -6.83235 | -52.81254 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e86207a-e597-3b72-8f71-1765b660cf7b | -6.77747 | -52.80857 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9bf2c3a7-11e3-3d43-be7c-f42f49ad9c8d | -6.72287 | -42.25805 | 2025-09-02 05:04:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 02044c11-1eb5-30c1-bc8f-fcb567834ac5 | -6.8226 | -52.82818 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd681515-e07f-3d46-b074-5d9524743a5f | -4.30464 | -48.09731 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf4c8866-9a35-361e-9b41-3d230a3a3a05 | -6.56885 | -43.71684 | 2025-09-02 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b48e460-c174-3a92-bc78-af9636935a27 | -6.04448 | -52.1786 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51349fd9-a47e-3bda-bff7-2e9ec46418a8 | -2.14105 | -48.00006 | 2025-09-02 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b851b1c1-8120-3191-9061-eb3c503e9fa4 | -2.98451 | -48.60452 | 2025-09-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30af30fe-ace3-3fe7-9d2a-c6960d8c6d63 | -7.69194 | -50.27595 | 2025-09-02 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1445807-ed6e-3da5-9fe6-ea53897fa58d | -6.85968 | -52.81076 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8067adef-4551-3190-a4f8-ce53d087e4b9 | -7.49689 | -45.35956 | 2025-09-02 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad265933-9af9-320e-acc3-0394c97a1d3f | -6.20175 | -45.39432 | 2025-09-02 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e265074-0d09-37f9-97b5-e0a7e8e52fff | -7.98153 | -46.46473 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f9ddf72-9cc9-379b-b0e6-3de76aadd5f3 | -6.77686 | -52.81275 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 60be8a2e-9d0d-3ebc-a14f-12fe75836ddf | -7.18355 | -59.7356 | 2025-09-02 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3302e905-b23a-34be-9184-a6539ed21267 | -8.71808 | -50.44736 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bb281e1-4c12-3bcd-86bc-ce20279b2fdc | -6.22355 | -43.3617 | 2025-09-02 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a53bdf51-7cf0-3a1c-abd9-7e5edf665d5c | -8.67145 | -49.98805 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README58.md)
