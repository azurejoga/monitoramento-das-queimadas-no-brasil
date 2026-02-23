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
| 710ff10b-4a01-323c-9fc3-b452442a86a9 | 4.29931 | -60.757 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 891c1a42-2439-3ee5-9013-fffd040d315e | 4.14784 | -60.86356 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c05b124d-b058-372a-9d56-7911f3f9c611 | 4.11781 | -61.16191 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dac512e-dc7c-3a17-845a-213f7e16d628 | 4.11383 | -61.15878 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 988de552-52d3-3b10-90c0-c6dfdff8c40f | 4.093 | -61.18125 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8967848-1a3e-33ce-8077-16935136d755 | 2.86348 | -60.78148 | 2026-02-23 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 12ab1064-3817-365b-8b9d-f4fbebd44a7a | 3.93701 | -60.99613 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52e7105b-19f7-32c0-b17e-db364cabd90a | 4.09415 | -61.18852 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f4a3c27-e327-3c0e-9a8c-c74730a77609 | 3.22501 | -59.92727 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12040930-5d28-3d9a-a236-37f012c58d6d | 4.16383 | -60.94193 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3e2ccf5-7999-37a2-8d8f-12e730fd804f | 3.42008 | -59.92464 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62725f0f-6c30-3bfc-b18f-9c0e4b3e1ab3 | 3.94551 | -60.98334 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d524a3b7-277c-3e55-aa17-ed76aed9854d | 4.28974 | -60.80476 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe4cbfbb-bdbb-338e-8c59-5b700b9ca374 | 2.31602 | -61.69921 | 2026-02-23 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6fc06e9-3594-397c-9afc-87be845332f4 | 2.23431 | -60.70008 | 2026-02-23 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc96c177-52f4-3d82-863f-ac307f7a18de | 4.09538 | -61.21811 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca33f957-051c-3df8-88f9-f01d146bee12 | 3.17784 | -59.98897 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 74065c32-e214-3762-aacd-8c977ddd9f83 | 2.711 | -60.23226 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cb64f12-20d5-37ae-b7f2-0c9a48434693 | 3.22863 | -59.92669 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| debd6dd4-ede5-39c0-a63b-7ff451ec755e | 4.08792 | -61.19308 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28a340d9-8ecc-3cde-93ca-afd3e712264d | 3.42234 | -59.91568 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1542b1a-9545-3bc1-87b1-c4e9c449d161 | 2.93403 | -60.24197 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a2f580f-fcc5-33b4-901d-6c126c1f2b06 | 2.88515 | -60.6832 | 2026-02-23 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c979f7f-dbbd-34a1-b315-e597e29cfcf2 | 4.17792 | -60.89796 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8cf0538-02c9-3151-b852-9f86a03a8b13 | 2.70742 | -60.23284 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abe293b4-dc09-32c4-b147-e9e99fbbee85 | 3.25465 | -59.92683 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc61fe4f-4a90-3750-870a-2110c4f0c412 | 3.20961 | -59.94701 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6010695-4e63-3baa-a4a8-29ef7fbc15e0 | 3.4246 | -59.90672 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a30a0f5-76c5-3b04-b542-076da6112612 | 2.97919 | -60.27246 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37e85092-59d2-399e-89bd-338407d40255 | 1.91229 | -60.36124 | 2026-02-23 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7ef343b-ed6b-31b8-86c4-e9777d061378 | 4.17542 | -60.85992 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df7c657c-8b11-31c1-8f52-3da132b7aa71 | 3.25665 | -59.93943 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca3ae151-55f6-3801-affb-acbcf9e815fb | 3.5335 | -60.88801 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93b09efd-9f30-38f1-ae71-62de99a3bce0 | 2.23368 | -60.69613 | 2026-02-23 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e07cb37e-a3e0-3d30-8890-e451771248c1 | 3.25961 | -59.93466 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1afe16d9-daf4-33a3-b1cb-218a30465948 | 3.18545 | -59.98099 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e69775ed-148d-3dd9-9777-7f101d93b055 | 3.19718 | -59.96192 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11d4608b-38a1-344b-915c-2adfb3cd935f | 4.07151 | -61.19937 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8209eae8-9553-30fc-8632-be7850e5e53d | 3.18671 | -59.97467 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29bb1fea-658b-3b27-b224-99920c4b293d | 2.77031 | -60.28178 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5046549d-a271-3197-acaa-846ae4fe5bda | 3.19786 | -59.96611 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7462723e-b657-382b-8166-9c08ad00e9cb | 4.09181 | -61.17375 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99971cf4-4c42-3d65-a375-c33a0a222bed | 4.29285 | -60.75726 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f2d1c67-68a9-3337-a488-500f6db7f0ec | 4.08901 | -61.17807 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e794a991-1a8d-3954-8c04-d1c7026e3036 | 4.23277 | -60.95456 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21448bc4-71b5-3999-abd5-8772eac6eae2 | 4.08908 | -61.20035 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71b1e999-18db-33ab-932d-fd7b6ee249ae | 4.0885 | -61.1967 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8ff0a22-e827-3ca2-a057-a17157df0d70 | 4.09422 | -61.21079 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 047b6fe1-9ed4-3fc3-8cf8-f444eebafc54 | 4.28917 | -60.80122 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d28ec18-eb59-30f4-b5fa-893fd9f8f18a | 4.11848 | -61.18819 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3013569d-7c18-3a2c-8ba1-09dd050669bb | 3.22206 | -59.93207 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 303eca6e-5486-3183-9771-e56af26617b4 | 3.34973 | -60.04957 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d422ccf-4d15-35f8-a70a-2834b8caf140 | 3.92156 | -59.94446 | 2026-02-23 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cf6477c-643b-3005-8cf9-1bd56b48c238 | 3.54492 | -60.87061 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| febdb871-d893-37bb-a0fe-499efded7878 | 4.11955 | -61.17294 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94ae9430-dd6e-37c4-8567-7abc700f08f4 | 3.94894 | -60.98283 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f812693e-0818-3aad-9acb-63f31bacdfb6 | 4.12662 | -61.08494 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c48b65d-379a-3a55-8300-b257dfdb50de | 4.29024 | -60.78564 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b89fd1f6-c3db-3198-96a4-eae563c95ff2 | 4.23217 | -60.95084 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3b21460-78d7-3023-8080-d9309ee74473 | 3.18441 | -59.98363 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e62ca04b-7091-308c-9ce9-d617cadc0d3e | 4.28962 | -60.78164 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71956421-3235-3ecb-b2a7-c89ac62a7e31 | 4.12717 | -61.08475 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba230d41-6e55-346d-bfea-9690b8ee8181 | 4.0948 | -61.21445 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ce29bf-c03e-388d-a8d5-ad0f0cb209de | 4.23337 | -60.95828 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3826c00e-aa5f-389a-b37b-c9832018fde9 | 4.16727 | -60.94144 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91f64d49-5ba1-3772-9f1a-4a69bf4c74fa | 3.42725 | -61.9881 | 2026-02-23 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4d2b01c-4c27-331e-adb1-f10f987ace83 | 3.21685 | -59.94584 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d0ee093-19d2-347f-a939-84e1d3f873df | 4.23559 | -60.95027 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b816ada3-cce0-3dec-b120-2082fef95cd6 | 4.07433 | -61.19517 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38288620-15fc-3250-955c-9ecb69b5e6f9 | 3.42848 | -60.6528 | 2026-02-23 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eae299fb-58e7-3ac9-a650-8c79b36ae99f | 2.92011 | -60.42561 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 30c83af8-6509-3f93-a32e-300c316f1368 | 4.29319 | -60.80434 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05a70ebb-f87e-3fdd-8f91-36c5bfcf53a6 | 4.11732 | -61.18083 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38e06696-3fe8-342b-8e10-18c624dc4378 | 3.4106 | -59.93476 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53c122a4-482a-387c-811b-eedcf05336f9 | 3.1808 | -59.98421 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b71633fb-61d9-35d6-a342-fcd352cf8d9e | 2.76673 | -60.28236 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 315ecfb3-dbed-3ad7-9480-2954e3e80328 | 3.42189 | -59.88991 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68e35666-3c2c-35a2-9fe6-80b65d03cf54 | 2.3166 | -61.70286 | 2026-02-23 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80c74456-7294-3d2b-9f64-617b868f8b9b | 3.21912 | -59.93686 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bbd73f6-fa68-3425-a52b-b84686584ab0 | 4.09358 | -61.18489 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 658d9d01-3cf5-376c-a572-6e8ed77e9d9a | 3.20012 | -59.95714 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 95ee6543-220b-3d9e-af8b-e90cf7cc4ec1 | 4.29242 | -60.75806 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b62ba27d-6d68-347f-8671-40b415c48e01 | 4.20203 | -60.11254 | 2026-02-23 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b16aac1f-7878-3125-aaf6-c4ce049ffcb0 | 2.95129 | -60.28109 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34ef30bc-5eed-3df7-92e0-94f680de9d0f | 2.28497 | -60.51573 | 2026-02-23 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e013cace-35a7-3917-9aa7-d62325e8773a | 2.9542 | -60.27644 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c75b50b-627d-3c87-be35-cfce10654a5c | 4.21146 | -60.10338 | 2026-02-23 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f9d28d0-0588-38fe-b511-692dd802cc14 | 3.25532 | -59.93104 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eae9add0-f8a8-304a-804d-d7bdcd22e4c0 | 4.17838 | -60.87864 | 2026-02-23 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 455d6ac4-a4e3-3d50-bc33-2e82405b95a2 | 3.18737 | -59.97887 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d992680-17d0-3561-ba74-d1cce4a9ebdc | 2.31321 | -61.7034 | 2026-02-23 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 658b22a9-0626-32b5-a150-ac9fd885e483 | 2.91947 | -60.42159 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 43158826-8e06-3e47-9b9e-9bb9bb1d18da | 3.19425 | -59.96668 | 2026-02-23 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d10edd1-12e4-3af1-bec8-71c04f03c602 | 3.79374 | -60.48925 | 2026-02-23 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77b530b8-b826-3453-9731-e6a87e1f4697 | 1.18681 | -59.99306 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b30a555-0f46-3897-9e34-ca4473bb7064 | 1.20188 | -59.96799 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebcb4c22-57b3-3206-a1de-60bb7b7efd47 | 1.19515 | -59.97358 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29d3a787-1b86-33b1-869d-2e1ac09a3ed3 | 1.86289 | -60.62309 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d56a195-24d8-3a74-82a8-1fdd5bb47b64 | 1.20999 | -59.97128 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f46c49d5-1bd3-3a9a-9ae7-57e664900df4 | 1.42859 | -59.95454 | 2026-02-23 05:42:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README4.md)
