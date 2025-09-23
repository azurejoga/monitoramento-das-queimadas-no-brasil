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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1efc3f0d-b6c1-3734-8de0-6d53ac8ff144 | -4.30577 | -55.34133 | 2025-09-23 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b7bb4c8-0ec2-3614-a452-9901e048a056 | -4.40047 | -44.37027 | 2025-09-23 05:10:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd21d01c-d0c1-3b00-a603-24ed19992b2a | -4.59556 | -46.591 | 2025-09-23 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7afeff98-4c3f-3911-928f-891739fbb471 | -8.52978 | -44.97009 | 2025-09-23 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 801331c2-dc85-31b3-a6c3-c8c45035d2d6 | 0.15517 | -60.67622 | 2025-09-23 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2eac1a7f-b79b-3f0b-95ac-87f92852d595 | -6.33757 | -56.1919 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcb85726-1328-30ef-9856-d270e1975872 | -2.64978 | -54.6757 | 2025-09-23 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0968c6c0-86ae-37f9-aa7b-452d06b184dd | -5.23643 | -56.0149 | 2025-09-23 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13ec518a-0da2-34f6-b639-f2a216a8b10a | -2.82578 | -48.5898 | 2025-09-23 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 958d19d0-f7c7-3577-90df-0be8b80acb9d | -2.25156 | -47.88259 | 2025-09-23 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a2f608c2-f0ee-3372-99a7-34fb2a5c35ab | 0.15911 | -60.67561 | 2025-09-23 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c197df1b-efab-3b36-9999-10ccccf6ed84 | -5.6554 | -51.47158 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0d98c5e-e6c7-3eec-9cc9-dc769e4a4b6f | -4.19919 | -51.01769 | 2025-09-23 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15a0147a-8995-3ec6-a647-d7506298baaf | -6.34263 | -56.20361 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2460afb7-f3d8-3516-a399-a71571b3e4e5 | -4.49104 | -48.11613 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e17c89a4-1459-3166-a6bd-50ff492563a9 | -4.7806 | -47.25458 | 2025-09-23 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06c7418d-b13c-3cde-aee1-805a67cef6b7 | -3.45218 | -53.82923 | 2025-09-23 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b143cbc-d7cf-3c12-85b7-ac021f1838a5 | -2.7917 | -49.59684 | 2025-09-23 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a522b46c-818b-31ee-bcc5-0ea2620eeb57 | -2.5656 | -48.97079 | 2025-09-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 700b681d-3c38-3ca0-b0ce-e14934c1d4c2 | -2.36641 | -67.21552 | 2025-09-23 05:10:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7f5e3a5-b338-3fd8-af62-b6662b3595e7 | -1.50777 | -55.50975 | 2025-09-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ce30f21-2ce0-3bb5-8186-bdc3cd0caeac | -4.7045 | -56.06674 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b84838c4-d3a2-378e-9f1d-df398b9724a1 | -7.89014 | -44.01909 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fe56c682-e20f-3562-a22e-83f067814596 | -5.69301 | -51.05418 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a17d419e-0d9c-383b-93fc-0811633c8518 | -1.12457 | -54.14278 | 2025-09-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44f87644-baa6-3654-8f55-59b2831d2a29 | -7.90128 | -44.02049 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 666adaa2-1d94-3752-888f-02efa80539d9 | -6.33703 | -56.19546 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e468483-340e-3948-8263-9d10dd00c738 | -3.01978 | -55.96194 | 2025-09-23 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcae0ddb-cd05-340b-911a-bb0996699736 | -6.34372 | -56.1965 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4415f8b-b276-34aa-99fa-a17ca0869d11 | -6.34707 | -56.19703 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c98563b0-1e0b-3cac-bb05-8711bacbfdec | -6.33929 | -56.20309 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bab4e766-8c8f-34c8-83ee-fea32670799f | -8.1356 | -44.46883 | 2025-09-23 05:10:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cefa0e73-e289-3862-bb65-bf4904e17588 | -8.52297 | -44.96942 | 2025-09-23 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55a74da0-1aee-3ae8-9390-536828c87b34 | -4.27183 | -48.18734 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff8a469e-f0a9-367a-8682-0790a595d190 | -6.95772 | -45.20627 | 2025-09-23 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 215659c5-fd0d-334e-a054-575f09c54180 | -6.34816 | -56.1899 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9a1836a-9e83-3b6f-aa61-a00a1476a008 | -7.88612 | -44.0263 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 24f6a1c2-2526-3525-a84d-95c65f00ca55 | -3.21645 | -49.17566 | 2025-09-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1f65001-4841-391f-90fa-eead98019b8f | -6.24605 | -55.36118 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24dd6c6d-0633-3c94-bd6a-806d094f9fe2 | -4.48406 | -47.67596 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc9f86dc-4b2e-3f71-8eb1-6fbd940d5208 | -4.30632 | -55.3377 | 2025-09-23 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9107b1c8-f13b-30f7-860d-44f26c7f8f80 | -6.41171 | -43.76616 | 2025-09-23 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fbed5149-3656-3a3a-86a1-9a14d6c9c1bd | -4.00974 | -43.2653 | 2025-09-23 05:10:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69aebc5b-414c-3761-920f-9a33a5c5a136 | -6.71798 | -47.20282 | 2025-09-23 05:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 052a8ca8-57c2-3cab-8f9a-69bf671c5cde | -2.36515 | -67.2141 | 2025-09-23 05:10:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de9f2c72-d0e4-333d-8324-1e435bf9ef77 | -3.85491 | -52.24102 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 492a2d20-59da-386c-b31e-30bc00d5dfe5 | -4.69229 | -55.65866 | 2025-09-23 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd0e6393-1a2d-3ef0-b5ab-d4913f0f4a28 | -2.25108 | -47.88572 | 2025-09-23 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f101e71a-462d-3e89-8559-b411a9cd57d9 | -4.0782 | -48.03851 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88ad083b-f825-398d-b43c-297d87f02c47 | -2.79632 | -49.59757 | 2025-09-23 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47db019c-840a-393b-8358-7982bdd09e8f | -4.13067 | -48.82153 | 2025-09-23 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 792c200f-7b75-377f-8ca8-fbce36ed6801 | -3.85174 | -52.23546 | 2025-09-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 179b05a4-9f11-388c-85dd-bc0c988ef2c8 | -4.07774 | -48.04164 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c3a564c-c86e-307e-a218-3bfaafc40ca3 | -7.88212 | -44.02539 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0cdbafea-1ebc-351f-b004-7386b82d927c | -4.40997 | -55.41695 | 2025-09-23 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7380f0c6-8963-3812-8af9-4e9103eaea38 | -3.24352 | -58.84728 | 2025-09-23 05:10:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c1929d7-801d-3e90-8af9-4c32cf7b76a0 | -5.65116 | -51.47092 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb25a428-a22a-3bed-9fda-742b0d299e47 | -7.16129 | -48.29644 | 2025-09-23 05:10:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 699e6e83-90ae-376c-92d2-ba3e88553e82 | -7.8941 | -44.02003 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9961fbca-479d-31de-b6ff-8989822b8a50 | -8.52501 | -44.9684 | 2025-09-23 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ca50bda3-37be-37a4-af70-19afd10dd924 | -5.69737 | -51.05494 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5549ca70-ad54-34e0-abbd-3a84a32959b0 | -4.6014 | -46.59179 | 2025-09-23 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b4f076e-b8ff-3d99-9e26-3990ed78c06b | -5.64324 | -51.46568 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b089510-cba7-32c6-a32d-672128d1c848 | -6.52118 | -54.87236 | 2025-09-23 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe7ed22f-0953-3709-bde0-fbf1fca22ea1 | -7.88923 | -44.02632 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1ab1668c-7621-3f0a-b69b-e518fcbd2970 | -2.25625 | -47.88644 | 2025-09-23 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac7bfe26-fafd-3dd9-803d-e6266f7dc01c | -6.89843 | -44.77042 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26f04026-dd0d-306d-a822-40ae626bd496 | -4.8443 | -48.69831 | 2025-09-23 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d82ddc69-2e44-3192-90e5-5e544a136498 | -3.07955 | -49.46537 | 2025-09-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b006d3b2-c9a3-3d76-ac8c-e190452bd4d0 | -3.39806 | -47.50146 | 2025-09-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1ec8cff-046b-3d69-a755-af2f4615f542 | -2.25673 | -47.88331 | 2025-09-23 05:10:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 767fd0d8-52a3-3598-8473-0f23ef2a8f7a | -2.22804 | -51.94865 | 2025-09-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 329dbaf3-619b-3c3d-9582-44939f90e5fc | -4.48456 | -47.67244 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c565633-8541-3f42-ba2e-d06b1f5b8738 | -3.40346 | -47.50222 | 2025-09-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e928883-3c48-3310-9b20-e840a9a06f86 | -7.16265 | -48.28618 | 2025-09-23 05:10:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccb102ba-41db-3960-aeab-ed8fee2fed91 | -4.84584 | -48.69831 | 2025-09-23 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea47cc7b-618c-3160-8150-772c0cbda83f | -3.64501 | -48.32125 | 2025-09-23 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91146e6d-ea02-3d87-aea2-2c632557ef8c | -3.79425 | -48.63272 | 2025-09-23 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad76a4a3-2200-3fa6-91c1-359dcd725ebf | -6.34201 | -56.1853 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcc81c2d-e135-33b4-9f95-3cf1a21cc13b | -6.26432 | -45.33566 | 2025-09-23 05:10:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 511d24e4-c78d-32ec-ad91-8e9e46aa285c | -4.48065 | -55.57508 | 2025-09-23 05:10:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10173067-1257-3fa0-934d-936b8435b191 | -5.17869 | -56.05663 | 2025-09-23 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4106fbd-8bf7-329b-b27e-672947806392 | -4.4038 | -50.69268 | 2025-09-23 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e49a1fda-91cc-36ca-a206-a139e37fb0cc | -3.8683 | -55.35624 | 2025-09-23 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a00dc850-94b9-352f-bc45-68e1863d1acc | -8.51527 | -44.97586 | 2025-09-23 05:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20736499-b842-321e-af18-e9b2c0659f4f | -4.84628 | -48.69538 | 2025-09-23 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19a9661a-3cab-3134-b3fa-8f22180f79df | -4.07778 | -48.04103 | 2025-09-23 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ce14f99-86d8-31eb-8f23-13d70b6121dc | -4.84471 | -48.69538 | 2025-09-23 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bed19175-1c39-360d-9e43-13fc459d76ec | -8.00428 | -45.71564 | 2025-09-23 05:10:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07fbc6ec-bc19-3adf-a3eb-28e61b3ad027 | -7.89728 | -44.01989 | 2025-09-23 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 614b05ae-c414-31b4-8a5c-7772d450ea51 | -4.49135 | -48.11515 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8271b843-9bd0-30a8-8440-fa9347e0eaf9 | -4.10652 | -48.74166 | 2025-09-23 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06dea20c-2dbc-3f11-9126-63e9fc304a96 | -4.49087 | -48.11837 | 2025-09-23 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ab7d9e9-fa59-368c-8f8c-d3e9c76dde39 | -6.89933 | -44.76378 | 2025-09-23 05:10:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 782e95f5-e0b0-3d7c-a043-f137a1c2fd61 | -2.78528 | -49.57614 | 2025-09-23 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e25d073f-0491-379e-a734-37028396c121 | 0.15988 | -60.68065 | 2025-09-23 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a5631491-24d8-3f00-a03c-05630cd6e957 | -3.35677 | -59.43656 | 2025-09-23 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0f7cb17-16f2-3a12-a2ba-abfd6c05d926 | -6.34427 | -56.19295 | 2025-09-23 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b04b28b5-02b3-34c5-a799-ee7ab821c37b | -12.44926 | -54.47444 | 2025-09-23 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5167009-e02f-36ce-a507-7425cbdadf35 | -11.65932 | -57.36013 | 2025-09-23 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
