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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce1d7415-c682-30f5-b5ff-bf5aa1cec2b7 | -11.0223 | -54.1379 | 2026-09-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d688aba9-93b1-352d-bd49-e2232b89e564 | -11.8495 | -46.833 | 2026-09-21 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 7341f05e-6cf2-3eda-9f2e-2d154d4ecf3c | -11.801 | -49.8345 | 2026-09-21 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 833fac23-8415-3511-9a23-71c87360f14a | -6.4486 | -59.9717 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 396aca66-a3ee-38f4-b6cf-1ab26ce7a9f3 | -10.4675 | -50.2624 | 2026-09-21 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6e367419-6519-3760-a317-4deeaffdabbc | -5.9151 | -59.9522 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 90feb1d8-e7d5-3656-b747-eb727886ee97 | -5.6411 | -43.3687 | 2026-09-21 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a497bd3c-d932-3031-87fa-3cbe8b121071 | -11.8168 | -50.0482 | 2026-09-21 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| bc159031-c9b8-311c-9bf2-60e37d25bf18 | -10.0898 | -50.2795 | 2026-09-21 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 914f83fb-a002-3375-b7c7-197f65642460 | -9.247 | -57.1488 | 2026-09-21 14:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| a284dd10-25e7-35c5-90fe-025e34cfa7ad | -13.5075 | -51.8728 | 2026-09-21 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9e68b160-8154-37cc-951e-b77361ea53bb | -3.177 | -42.8376 | 2026-09-21 14:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 383f81c4-c319-3d49-9d39-5a4aa51def61 | -9.7504 | -46.0637 | 2026-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 10b70a53-3f2a-3036-a2dc-51b91630b6e9 | -8.7267 | -44.8836 | 2026-09-21 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 12910f35-a05e-3c63-a179-50c61743b158 | -11.4353 | -45.3459 | 2026-09-21 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0ebe504a-f80f-3522-8a64-ed83b142194d | -9.6853 | -54.3318 | 2026-09-21 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a63a2655-f14c-3b43-be97-126dcb7bbc1d | -6.3918 | -45.2175 | 2026-09-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a469e7ec-64bb-353a-ae66-ef715997ed81 | -6.8379 | -45.5656 | 2026-09-21 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b38eb377-fbe9-34f9-8546-e9a81cccc63b | -7.3259 | -55.6153 | 2026-09-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| fe743072-7043-3849-81b8-44123ec9dd85 | -8.7706 | -45.8567 | 2026-09-21 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 194.0 |
| f4288432-56a8-324d-98f1-b1b6ed4ddf82 | -3.3454 | -42.7597 | 2026-09-21 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 817496ac-66be-38c9-8e36-a0cfeab6848a | -3.3823 | -50.4486 | 2026-09-21 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 7407deef-3d53-3fec-a8ca-29db36c47fd4 | -13.2602 | -51.7548 | 2026-09-21 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 67e65cc4-6bff-3966-99b0-27c277c11537 | -12.5231 | -50.0051 | 2026-09-21 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 97200182-caed-3db4-b403-658c0c53d733 | -9.9768 | -50.2694 | 2026-09-21 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 19fa8087-1b91-38a8-9e87-0af63c6e55b1 | -5.7692 | -43.7077 | 2026-09-21 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 5156e111-7d0b-3f9e-a750-2c70dcdfc142 | -3.584 | -40.3264 | 2026-09-21 14:20:00 | GOES-19 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 77d4eeaf-5edd-307a-aa5d-a343fd4e8f02 | -5.9335 | -59.9515 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 150.8 |
| 112088d2-ef70-38f7-a26b-9bd08cb83e30 | -12.9091 | -50.9672 | 2026-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 8a8c562d-38e3-3ab2-86a0-2002dca3f601 | -10.8014 | -50.7391 | 2026-09-21 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 64c1b60d-56a1-38a2-8062-fb3f96e95567 | -8.7729 | -44.2568 | 2026-09-21 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| aee266e7-40fc-3cfe-ba08-dad1ca4b71cf | -3.3267 | -42.7606 | 2026-09-21 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 84877f6d-d8b4-3c56-91bc-b61dde38dae3 | -3.6632 | -58.8643 | 2026-09-21 14:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 79219ad0-3d1e-3975-b2ec-9830f52e32c4 | -7.2937 | -46.7798 | 2026-09-21 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 677f265d-b0ba-342f-bdbe-c5760d160837 | -11.6802 | -43.4209 | 2026-09-21 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 11b00ff2-071e-3346-b3c3-2eadba520fbf | -10.9544 | -50.6165 | 2026-09-21 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 325c8ebd-90b5-3556-a149-3816ce651224 | -10.8921 | -53.9857 | 2026-09-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 159327de-a093-3076-aec1-bfed3d83c085 | -14.1819 | -51.7866 | 2026-09-21 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| f88cfd69-9b69-32bc-8039-e0fb9328f43b | -9.4567 | -45.4178 | 2026-09-21 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 9df04b9e-5863-35b8-87f0-b561c04f3ceb | -5.6779 | -43.4358 | 2026-09-21 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 2f35d0c3-7af6-38bf-8de5-14269bb199a8 | -9.2759 | -46.1852 | 2026-09-21 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c39472cd-a115-3574-8121-feb736537bc3 | -2.8791 | -57.799 | 2026-09-21 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 9b46382a-88f8-3be5-8028-3001cba17f58 | -6.1466 | -47.5065 | 2026-09-21 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 70ac1597-9422-31de-89d7-0347a59d7a24 | -8.7723 | -44.3031 | 2026-09-21 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1de43b33-895c-39cc-85c5-5d8595537848 | -10.955 | -50.5738 | 2026-09-21 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e0ecd032-f192-30d3-8543-a5ccfe47d04b | -10.885 | -51.5558 | 2026-09-21 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| dd5ffbcc-05ba-3f2e-9d3a-0f5702741e91 | -12.8711 | -50.9505 | 2026-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d8a856e8-e43a-3bd1-b70c-85bc325febc3 | -7.5704 | -57.6766 | 2026-09-21 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 3d0442fe-6af1-3392-a50d-49981dcfa379 | -9.977 | -50.248 | 2026-09-21 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 66fa6a20-7df8-36cc-b4b1-29a238ad0a71 | -6.7184 | -55.0884 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 0b58fd42-6cd1-3544-b91a-8a030dfab844 | -10.8011 | -50.7604 | 2026-09-21 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| cdbe511d-2ba2-3284-8915-78c958abad30 | -2.8608 | -57.8188 | 2026-09-21 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 054e7acb-1518-36cf-a3d8-5965765da6d9 | -6.5634 | -44.9084 | 2026-09-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a163d681-1607-3d51-9e5f-bd48cbf2f289 | -5.9334 | -59.9707 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 178.6 |
| b7357df0-82e0-39d0-91c3-0e4d3903e14d | -3.0507 | -50.2702 | 2026-09-21 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 24c661ce-5c46-3928-b545-8d8c1a1ab4b5 | -6.3195 | -60.0147 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 5b9fd174-9239-3f2a-a8f5-f0a42dc66e84 | -6.5569 | -45.566 | 2026-09-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 48da0ac2-f0da-3098-ba06-b6f2a4d624c1 | -9.0428 | -48.1603 | 2026-09-21 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 3117302a-da3e-3c63-8c6d-bae63f1c9d86 | -10.3725 | -48.9153 | 2026-09-21 14:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a7b5a818-b6ab-36c7-9d5d-996f0e0c147a | -6.8058 | -55.8217 | 2026-09-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8bad232c-7a66-3f59-bd6b-49fcbb3d8ce2 | -6.001 | -51.7903 | 2026-09-21 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 48d3bef7-f14f-3979-861c-30cb5e35660c | -6.3198 | -59.9572 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b68df905-de7d-3fb4-b752-ac4f3c5f347f | -6.1653 | -47.5052 | 2026-09-21 14:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| dc62e83e-78be-37f5-b23c-2649746cda8d | -6.4301 | -59.9916 | 2026-09-21 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| fec78046-5eb6-348b-bc97-94aa37f3d04f | -5.804 | -53.5223 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 955933dc-8722-3dcd-8b30-cbae93283d66 | -5.6221 | -43.3934 | 2026-09-21 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| e9bcc1d2-4d31-3d37-bf38-435a726a680a | -11.8362 | -50.0244 | 2026-09-21 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 338d24ba-9c36-37f2-81cd-3be94f4c84cb | -3.4461 | -58.0199 | 2026-09-21 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e08e1341-1620-322a-a64a-cb7c1f974b8f | -6.0973 | -53.913 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3d58c92a-41c7-36ed-be3d-8f4667e2c947 | -6.392 | -45.1948 | 2026-09-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 247.3 |
| 96f8fb54-a948-3dfb-a6dd-2135dcee761a | -6.5759 | -45.5419 | 2026-09-21 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 28c8c9b6-fe7f-391d-b54e-749821099112 | -8.1874 | -54.742 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 292a4db9-e7b8-36cc-976b-89324d39b189 | -8.7726 | -44.28 | 2026-09-21 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 4f507055-f8ee-3343-93b5-b11480402720 | -13.2791 | -51.7737 | 2026-09-21 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 05064d86-3c9c-34de-8642-0f4eab73f2e4 | -3.3453 | -42.7832 | 2026-09-21 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 91c5f278-65a0-357c-a96a-139e169329e3 | -6.0033 | -44.7247 | 2026-09-21 14:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| be860607-a1b4-3970-abbb-3fe62da7ab4c | -6.0197 | -51.7686 | 2026-09-21 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 0c8d8dc9-f861-3c0e-ba5f-34dca3ed7aa8 | -13.3251 | -51.2997 | 2026-09-21 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| bb58ed0b-2f24-3681-a879-d9b2c4d86a58 | -9.0239 | -48.1622 | 2026-09-21 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 5b66900f-6e1a-3f4f-bb06-848270dd6fa9 | -10.43 | -50.2449 | 2026-09-21 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b497da24-7a6d-3305-8769-6fe4b3f3f343 | -11.4545 | -45.3432 | 2026-09-21 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e54aae37-cf9d-3de3-bc71-dc13962c1206 | -7.3289 | -55.2155 | 2026-09-21 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 51ae642d-abde-33d4-bbf2-c317688dae04 | -10.9547 | -50.5952 | 2026-09-21 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 34d0751f-1907-35bc-beda-966002052fca | -8.7912 | -44.301 | 2026-09-21 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a76b26d9-f77c-3e6a-a4fa-5f5b408af584 | -7.3291 | -55.1955 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 377a48ea-3f04-3e06-83d2-d6dc1ba93a22 | -10.9358 | -50.5972 | 2026-09-21 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 4c9e5e5b-c66c-3fe6-ae72-a7e664fca561 | -10.5906 | -53.9918 | 2026-09-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b747b046-1d52-3359-9bcc-3006fd728efc | -10.3728 | -48.8936 | 2026-09-21 14:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2cf4cc0d-2647-30ec-b9be-416b0b1c39f8 | -3.7856 | -60.7525 | 2026-09-21 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| be022db9-d5de-3b9c-b475-23937ba08c38 | -11.9115 | -50.0801 | 2026-09-21 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 43aea2cf-b554-38df-acac-2c17951daa7d | -15.4677 | -48.4084 | 2026-09-21 14:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| a33e4063-f408-3e5a-af59-7e28757ff7d3 | -11.118 | -54.0268 | 2026-09-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f515429c-879c-3921-a001-1c287beb387c | -7.5888 | -57.6953 | 2026-09-21 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5046f346-a5a9-357c-8c7c-411f88afe85f | -8.7911 | -48.7502 | 2026-09-21 14:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 148.9 |
| de81062a-869d-39f6-a873-66e4c5c7b09b | -5.6594 | -43.4139 | 2026-09-21 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 45cd174b-7269-34ed-b63c-2561668c7b09 | -8.1686 | -54.7634 | 2026-09-21 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 68c4948b-a2a7-327a-85f1-586813e3a73a | -10.8735 | -53.9668 | 2026-09-21 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 3e1c28de-cb88-32f5-a6e7-54fa9a90544a | -5.6223 | -43.3701 | 2026-09-21 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 6bb4cb13-4b9d-3ada-9984-590496d74f82 | -3.8392 | -61.1682 | 2026-09-21 14:20:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| b6aad5e2-1d43-3a13-a0b8-62d77b76619e | -12.3018 | -50.7203 | 2026-09-21 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |


[Clique aqui para ver as próximas entradas](README128.md)
