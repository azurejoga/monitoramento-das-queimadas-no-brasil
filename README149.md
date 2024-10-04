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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfda4022-ffdf-3583-94c8-85ec1efd8a6a | -3.23893 | -54.50534 | 2024-10-04 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f369ba68-966e-38d1-81fa-53ecae57adbd | -3.06646 | -54.77611 | 2024-10-04 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da54360f-efa1-36b4-b806-2282641d625c | -2.97787 | -53.72692 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9dbe423-6504-348d-a628-0d54bd16da5e | -2.97733 | -53.73037 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7de8ab10-1790-373d-a0ce-5396ff294075 | -2.97456 | -53.72641 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11dc9928-cffc-3d5f-a6fd-29087b772f73 | -2.97402 | -53.72985 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b16c586-ad1c-36f7-8a86-3080afc13cbe | -2.97348 | -53.7333 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19f85ec8-24fe-32ca-a7c2-300a0c81e9dc | -2.97125 | -53.72589 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d62a31dd-cec2-36bf-9246-da0464b2b0a4 | -2.97071 | -53.72934 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd898da8-1a44-3271-a7b7-2dc20ed603bf | -2.95081 | -53.70507 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e98a172-6d68-3d4a-bd67-c3c3cdafac54 | -2.95027 | -53.70851 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdb8bd8f-af1f-34d6-9733-7eb19a53bfa9 | -2.94972 | -53.71195 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f05350db-3e45-3655-b19e-7403e15407bc | -2.94804 | -53.70111 | 2024-10-04 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c4f415-34ad-35e1-962e-86605c6a930a | -2.89878 | -53.86306 | 2024-10-04 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28be304e-0416-3fed-a51e-4eedb07c8d03 | -4.11794 | -54.91467 | 2024-10-04 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3b185e5-2d4a-3ed6-9dcf-65b14dc20ff7 | -3.82523 | -54.23533 | 2024-10-04 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0b4e26f-9861-3e1e-a3f4-0fd18a5b853d | -7.9812 | -55.06865 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96bdd077-ff44-3f69-9b16-544adc539596 | -7.97844 | -55.06463 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b54b1a8-6b3f-358f-b0ad-f184ff549ba9 | -7.97789 | -55.06812 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c639b569-5d4b-3a45-803d-d3abbd012a41 | -7.70425 | -55.2077 | 2024-10-04 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5206ed80-01a1-3f63-b3c4-43fe05b6309d | -7.10075 | -55.11494 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 135d4a51-c89b-3a1a-ba89-919e0c00727f | -6.67521 | -55.37304 | 2024-10-04 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe386ab0-1fff-39e7-9b6a-5475bd3a1f99 | -6.67187 | -55.37251 | 2024-10-04 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f25c30cf-6eb0-3054-8482-05c0efb3635a | -8.51406 | -55.1573 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6f0337a-b42f-3e8e-b6a0-6312dfc521b8 | -8.5135 | -55.16079 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11bc8eee-5dc7-351b-90e7-2096d2d7be01 | -8.51074 | -55.15677 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af09ac6e-0026-3f29-b680-1686d2c9ec6c | -8.51019 | -55.16026 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3be83d7e-3288-328e-a5c0-94c28339f11e | -8.4914 | -54.99998 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0fe65e8-3a5b-36ef-8e20-af805958a796 | -8.06716 | -54.78272 | 2024-10-04 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4bb36a4-ba6a-34ef-b7d4-e24a78d8c19d | -2.15161 | -55.25735 | 2024-10-04 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e119ebd-5e25-3de3-90f8-e409faa62089 | -4.34953 | -55.83312 | 2024-10-04 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b00a5914-8fb7-3ada-8c11-6941f912214d | -6.47169 | -56.00582 | 2024-10-04 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64fe6d6e-ffe4-3a60-a062-cf8170ab6a89 | -6.46427 | -56.0084 | 2024-10-04 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b08efae9-f224-3de2-960b-35f9fcc0d6d8 | -6.47229 | -56.00214 | 2024-10-04 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 170a7463-1ff8-342c-8d78-f883311120b6 | -6.46768 | -56.00895 | 2024-10-04 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3183e142-50f2-3695-ab85-6c7d04c5af3d | -6.26447 | -57.91253 | 2024-10-04 04:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7709bb5-0a46-3b25-a128-6d63025380e1 | -6.26372 | -57.917 | 2024-10-04 04:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d0e396f-671e-3810-bd76-b95b822605ef | -6.97605 | -59.09727 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd52ded-b0a1-3c58-aca9-ca2ac563c7ee | -6.97518 | -59.10248 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2a9b180-523f-3360-8604-20466ea60968 | -6.97207 | -59.09662 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 316de80e-b5ba-3849-8366-24bc9e61609e | -6.9712 | -59.10181 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c90dc75-4f94-361b-9d63-bb78ba8ec669 | -6.89495 | -59.05545 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1437f83-7a1f-39d9-b257-16680c6ff917 | -6.87909 | -59.05271 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8451323a-4eb6-33f2-9937-ce661f414f7a | -6.87683 | -59.04171 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9476737f-6308-36d2-985b-141401fb7826 | -6.87598 | -59.04688 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d1bf5fe-a7f7-3b0e-b377-b3561abf3965 | -6.87512 | -59.05203 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ddee4f-65b4-38cb-a7f4-6d85e68e0ec3 | -6.87115 | -59.05136 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60b6fb36-6af2-3596-b33d-20581df85681 | -6.86977 | -59.03519 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1965c45-d815-3309-9550-d16d0266fb68 | -6.87769 | -59.03653 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2befa1c0-b743-3db5-a114-c07b21e33bf1 | -6.87373 | -59.03587 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a61f2b42-4ee0-36d9-a183-35de4e0b8ac8 | -6.87287 | -59.04104 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b6c8dce-77d7-3458-902a-642cc00e436c | -6.83312 | -58.98679 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40d18b41-fe55-3376-8835-2010a74d8f9e | -6.83063 | -58.98407 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad1c66a2-4c4b-3b64-9a2d-fcc15da52b7e | -3.18914 | -59.04595 | 2024-10-04 04:55:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f9c471d-f7e9-3205-905f-37247b65577d | -7.23973 | -59.5438 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17289efd-6aff-33d9-8b35-5112e150b97d | -7.23566 | -59.54308 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69b98534-2c7e-3e30-a211-94ebe5e66d2c | -7.14005 | -59.31651 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c3f5f59-ddf2-3561-9571-68bf7bcd066b | -7.13945 | -59.32008 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5f1b895-70c3-397d-bf8e-d8da92f4fbae | -7.13603 | -59.31583 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 402b30d2-ed58-3d1b-9718-e1b06d04b736 | -7.13543 | -59.31942 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 458ab48d-39a6-3dd7-9287-4039321ad67f | -7.13201 | -59.31514 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d219526e-483a-3450-9ac4-ff7740d1d056 | -7.05509 | -59.29953 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed5d29ba-8458-3dfe-8cfa-9e5a857c7295 | -7.0545 | -59.30305 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28d447c5-124b-320a-b350-312ed4f85ba6 | -7.05048 | -59.30237 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c97422e8-8038-3f53-b53a-80459259e4df | -7.04989 | -59.30592 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb2bf08b-2320-36b5-adf7-6829f35b121f | -7.01557 | -59.36216 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e38e157-4406-395f-ae15-df01ffdd30cc | -7.01153 | -59.3615 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d335d338-1334-3943-a0fe-a9aaaf0d5cd7 | -6.71709 | -59.1267 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c0c53c9-3e11-3dd6-b9b0-bdc9226b6161 | -6.7165 | -59.13018 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28b59ae3-d30f-3c23-b617-cdb4b1adf640 | -6.7131 | -59.12598 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e996bd5-0778-37a2-b383-39caa2f3b8f7 | -6.71251 | -59.12946 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13d58cde-d8f8-33b2-a2c4-71bd5406af88 | -6.71192 | -59.13296 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65279aea-25c3-3c86-9383-fe1a94e3b93a | -6.71133 | -59.13646 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3349f4ac-eb2e-39f2-9a81-cb939ab622e4 | -6.70793 | -59.13223 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c88433a7-6f0f-3f62-ad93-04e7ed4f21aa | -6.70734 | -59.13572 | 2024-10-04 04:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 311d57e1-a8b5-31ed-99d7-2273becde85a | -7.93141 | -61.27776 | 2024-10-04 04:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75dc9145-c2fa-3667-9660-34829bcd4151 | -7.92688 | -61.27699 | 2024-10-04 04:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 843125b2-66ae-3c0a-bce4-9924393d4a11 | -8.14625 | -61.39759 | 2024-10-04 04:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63bc93e3-cc88-3b5c-95fa-dad8122ad131 | -8.1417 | -61.39678 | 2024-10-04 04:55:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5fd49d1-e49e-3dde-8f55-c1e4b6df1080 | -14.1934 | -46.47532 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a7a4c76-e19f-354f-be3a-201215980cb6 | -14.19303 | -46.47856 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0a1ac68-d9fb-3817-a2ce-c1f57f446a8e | -14.18767 | -46.47774 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6096eed-c138-3508-b99c-652103208f3c | -14.06258 | -46.51723 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da70f2fd-f926-35d5-a764-11d88563fca2 | -14.05538 | -46.3504 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f054abbd-7481-373a-bd66-d235fa46d219 | -14.06299 | -46.51386 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4753159e-c98b-3b54-803b-3804dc7c0305 | -14.06087 | -46.51419 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 453352cf-0a91-3037-bb67-3525255a7806 | -14.0558 | -46.34692 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8cae5e4-3c29-3fd3-a15b-6f9d8e842d06 | -14.06049 | -46.51756 | 2024-10-04 04:57:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aa3ec10-bf90-3b4a-a591-e23b4d84e48a | -15.40527 | -47.4129 | 2024-10-04 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b5f4acd0-612b-316a-8365-d1124234f5d9 | -18.83609 | -42.91598 | 2024-10-04 04:57:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 837dbd54-a356-34be-a3b6-85136abf8d9f | -18.83027 | -42.98498 | 2024-10-04 04:57:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5cc69204-d892-3b8b-9451-c9040d49f25a | -18.82968 | -42.99198 | 2024-10-04 04:57:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e2be63b0-187f-302c-a08f-68661ec6fbab | -18.8232 | -42.98488 | 2024-10-04 04:57:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c731005-94fc-361d-bd92-de2f5e91362d | -18.82267 | -42.99121 | 2024-10-04 04:57:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| abd07a32-3887-3592-b481-a1741669731f | -18.08293 | -42.59848 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6ac32544-f28d-3c81-be06-6992614df513 | -18.07912 | -42.59692 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4228b409-513d-3224-87c6-58dfa09f1169 | -18.07581 | -42.5978 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c6304f70-d3c9-3867-b7fb-071f63c328db | -18.072 | -42.59625 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 53a8a7c8-37bb-36cf-bb55-f6840eabee06 | -18.06866 | -42.59747 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ebf5e134-26b1-31f9-8a26-51746ce23f1d | -18.04119 | -42.62016 | 2024-10-04 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README150.md)
