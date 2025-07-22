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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61e813b2-a786-32b9-998a-721942343eab | -5.6758 | -43.6683 | 2025-07-22 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 0743b63e-cbf1-3375-a1dc-02c857b3d3f4 | -4.388 | -43.2896 | 2025-07-22 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 189dca5f-1e15-3db7-8031-6db797dd2a6d | -4.3693 | -43.2907 | 2025-07-22 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| c6b6c973-bd65-3d11-8c5d-6619747406d5 | -8.921 | -47.3595 | 2025-07-22 00:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 9b15559d-565d-3471-a0be-39fa7ea282e6 | -7.2587 | -60.1897 | 2025-07-22 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e0fb4b1e-fa3a-3c5c-99ec-371eb28d5d43 | -12.5113 | -57.7626 | 2025-07-22 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 358af73e-a842-3587-8825-d3a69b0965d7 | -12.511 | -57.7825 | 2025-07-22 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9fb1591c-182d-3b96-b211-4f7d00de04cc | -12.4923 | -57.7642 | 2025-07-22 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| eb5eac1f-be28-3a59-92ad-3f3bca033976 | -15.9333 | -43.5166 | 2025-07-22 00:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 067cff28-2899-3d99-b83e-b6620dbdc2d2 | -3.1648 | -49.4648 | 2025-07-22 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 56981cb8-f015-37fe-86b4-c3556c7aae53 | -3.1649 | -49.4435 | 2025-07-22 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| e91bedf5-4e4e-3c27-a920-b55a30eed32a | -5.6946 | -43.6669 | 2025-07-22 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 235d6910-cef8-3073-957f-344e8803dc4c | -3.1832 | -49.4642 | 2025-07-22 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 4b690fb2-e82d-38d7-b03d-7413d2b2120d | -3.1833 | -49.4429 | 2025-07-22 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 230.5 |
| e2bd0229-9209-329e-8221-42e9f99940f1 | -11.7317 | -48.1849 | 2025-07-22 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 1656589c-d4c4-3930-9bd0-bb36d41e3fc6 | -8.5211 | -43.3063 | 2025-07-22 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 1806dc18-8792-3f1e-8d2e-69d6e3e31692 | -4.3882 | -43.2663 | 2025-07-22 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 24613dbd-0969-3fa9-8678-dccbf2dabb8b | -3.1833 | -49.4429 | 2025-07-22 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 222.2 |
| 1da5d4ea-fbd9-3d39-8045-439a782892a0 | -4.3693 | -43.2907 | 2025-07-22 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1e842f2e-0a38-3a30-b876-cdd8fc813bf3 | -12.4923 | -57.7642 | 2025-07-22 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 417205e0-182c-36be-a86c-e607ef3fedb1 | -3.2018 | -49.4423 | 2025-07-22 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a8e2b986-c918-3f4b-b993-6e2a246ca9f1 | -3.1832 | -49.4642 | 2025-07-22 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 171.2 |
| 4673747c-87f8-36e0-9601-f36229b2027e | -12.5113 | -57.7626 | 2025-07-22 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 188.1 |
| 3df66397-9e55-32a7-bf2d-9344e54ef80c | -12.4921 | -57.7841 | 2025-07-22 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 8151156d-de98-3f60-8a76-79b21fbff55f | -5.6946 | -43.6669 | 2025-07-22 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 66d54691-10c3-39d8-9213-2e393499f022 | -3.1648 | -49.4648 | 2025-07-22 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| bd5a345a-38b2-3dac-a13e-0d7d7b491b88 | -3.1649 | -49.4435 | 2025-07-22 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 2bdba27a-31b2-3c8a-8998-c0df221feebf | -4.388 | -43.2896 | 2025-07-22 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 346.7 |
| 9efe81ea-41f6-320f-b3e6-d072b936a5f5 | -5.6758 | -43.6683 | 2025-07-22 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 337a457b-a429-3d44-b8d3-248a9b464655 | -7.2587 | -60.1897 | 2025-07-22 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 63cf5525-a4f1-3919-af0c-9c70c25d6e50 | -15.9333 | -43.5166 | 2025-07-22 00:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 6bbdd998-6efb-341c-a896-c7657e14d55c | -11.7317 | -48.1849 | 2025-07-22 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 717f58a6-ce38-3b95-a42c-b2533638db78 | -12.511 | -57.7825 | 2025-07-22 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 27343a28-a6c7-3695-89e1-2a759e81a11b | -12.4923 | -57.7642 | 2025-07-22 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 0c538298-a3ef-32f0-85f5-073e97d53017 | -4.3693 | -43.2907 | 2025-07-22 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a936fb90-c768-33dc-92f9-ebd64e3bd6ab | -12.511 | -57.7825 | 2025-07-22 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 8bd59e6e-6c71-3639-a0a3-966b4bab2963 | -8.5022 | -43.3085 | 2025-07-22 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| c2d69569-bc22-3833-ab1d-dd02e7cf4859 | -4.4067 | -43.2885 | 2025-07-22 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9c89adc5-4a60-3d53-a6b6-d4c1e0a6ddcb | -3.1648 | -49.4648 | 2025-07-22 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 8c09d756-6292-3171-bfa6-66a53e4c4dc9 | -12.5113 | -57.7626 | 2025-07-22 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 52a74da0-c3fc-3894-8069-994b94f29794 | -3.1833 | -49.4429 | 2025-07-22 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 200.0 |
| e50220a4-fe5b-3418-92d0-34ca054ea3e9 | -7.2587 | -60.1897 | 2025-07-22 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 5fea570d-0200-3712-b82b-d29761634dba | -5.6946 | -43.6669 | 2025-07-22 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d9a85385-6ba1-3e98-82cf-e6499752f5dc | -12.4921 | -57.7841 | 2025-07-22 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 53ff9f00-e972-3653-b8ba-63f7dffbac66 | -3.1649 | -49.4435 | 2025-07-22 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 5f4dc9ca-1c4b-3436-8e7d-4e701d2363cd | -16.1001 | -49.9457 | 2025-07-22 00:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 4b105ff0-8d66-3855-bcf2-c610a47911a6 | -8.5211 | -43.3063 | 2025-07-22 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 8c853463-faaf-3b46-b68e-0f8d3bd73917 | -16.0997 | -49.9677 | 2025-07-22 00:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b562174b-7e98-3543-9678-de406b45eab1 | -5.6758 | -43.6683 | 2025-07-22 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 977de381-4b2b-3138-9dc4-328e74869033 | -3.1832 | -49.4642 | 2025-07-22 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| e178d2f9-3578-3609-9a5b-288374c6fb30 | -4.3882 | -43.2663 | 2025-07-22 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 3449c300-0aec-3b98-919d-2b7faa94793c | -11.7317 | -48.1849 | 2025-07-22 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 49e0eb5a-379c-3259-bc97-141c645b4dfe | -11.7508 | -48.1825 | 2025-07-22 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| dfe79939-cffc-3963-9805-f106137c9ca2 | -15.9333 | -43.5166 | 2025-07-22 00:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 75dbc490-dcc8-32c8-adf3-59d074f156d8 | -4.388 | -43.2896 | 2025-07-22 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 323.6 |
| 190f9894-9338-393b-95ec-dde7ccf81543 | -22.12157 | -43.15537 | 2025-07-22 00:22:00 | TERRA_M-M | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 8249b830-4cfd-3534-b1ae-c2c7cf07a7bf | -21.03883 | -42.0586 | 2025-07-22 00:22:00 | TERRA_M-M | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| eea07fd7-772e-31dd-b78d-22f379e5b507 | -20.47781 | -44.19581 | 2025-07-22 00:22:00 | TERRA_M-M | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 63a9a1aa-bb43-399a-a9c2-bebe6802755c | -20.34809 | -41.48886 | 2025-07-22 00:22:00 | TERRA_M-M | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 8bf75d26-61f8-3cd4-85a1-33e0fd026876 | -20.06718 | -41.4054 | 2025-07-22 00:22:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |
| 7e9c8cab-c91f-3667-b381-77e3ed8a522f | -20.06561 | -41.39498 | 2025-07-22 00:22:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 08a9f199-fa07-316b-b90f-86e6cfe85309 | -20.0589 | -41.40297 | 2025-07-22 00:22:00 | TERRA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| 55cd9469-71ce-3fba-ac69-56adef010d0e | -15.9316 | -43.51995 | 2025-07-22 00:24:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 9ccff6eb-13f4-35bc-b926-893878d07d5f | -11.73827 | -48.18633 | 2025-07-22 00:24:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c139f70a-0796-33ed-bf5a-eebacf253bde | -11.56859 | -44.84594 | 2025-07-22 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 16bc64b1-d430-3942-bf53-2e64a42df4e2 | -16.10572 | -49.96601 | 2025-07-22 00:24:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 09e498f5-c079-3c2f-8b23-8652def507f8 | -15.70762 | -49.3034 | 2025-07-22 00:24:00 | TERRA_M-M | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 85c5dc17-0379-3840-b5da-c7382c8d0bd9 | -10.60972 | -45.23597 | 2025-07-22 00:24:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 92265418-5433-3be2-b3d2-13cd79cd9872 | -13.68992 | -45.6868 | 2025-07-22 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 95f6f853-79c1-305f-a63c-d7389270da4a | -15.54271 | -47.99509 | 2025-07-22 00:24:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7ffa4932-f1d3-3b4b-b439-50857866102e | -14.77461 | -47.1236 | 2025-07-22 00:24:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5c41531e-13b9-3c7a-87c2-c16ac8d5bf8d | -15.70947 | -49.31952 | 2025-07-22 00:24:00 | TERRA_M-M | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 26120b31-d341-3b2b-9720-cc926a12fb4e | -14.64558 | -46.82603 | 2025-07-22 00:24:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 319af301-edb5-3c27-8835-95211efe644f | -11.72825 | -48.18766 | 2025-07-22 00:24:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 723f0a83-1cf2-388c-b848-1587dec40c93 | -16.69451 | -41.00949 | 2025-07-22 00:24:00 | TERRA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| bd6e3c61-2fe7-3605-bf12-a8d3be85c3e7 | -11.90233 | -44.07332 | 2025-07-22 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ebd7ee6f-d942-3f98-a493-3c0555bcd153 | -15.9303 | -43.51073 | 2025-07-22 00:24:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 54504532-39ab-303f-a761-7983c1bb0d6a | -12.65626 | -45.06075 | 2025-07-22 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 382e374c-0ea2-3d7a-94e0-f87b0426e0db | -18.99514 | -45.78447 | 2025-07-22 00:24:00 | TERRA_M-M | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6edd5817-af71-3683-ba1d-2ba6e0331e89 | -11.19424 | -48.62859 | 2025-07-22 00:24:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| de45e954-8d8f-3eac-a9c0-83f3b61c50c5 | -14.64224 | -46.83239 | 2025-07-22 00:24:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 44bd7bfe-368e-37c7-b4e4-19417f2c47d0 | -14.74601 | -46.29756 | 2025-07-22 00:24:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f3b99b44-6817-3bc4-b425-e9092708e79c | -19.41125 | -44.95927 | 2025-07-22 00:24:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ffacf731-a6ab-3070-9419-3768bc840487 | -11.91126 | -44.072 | 2025-07-22 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 6c1b098d-4f69-3af5-97f3-6b3ccc2f4ff2 | -11.19266 | -48.61642 | 2025-07-22 00:24:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fce0ace3-042f-339d-a2b3-2be2d1e468ef | -14.64364 | -46.84309 | 2025-07-22 00:24:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e8645aed-10f7-36e9-8b4e-22b24a5e6be1 | -11.56928 | -44.25932 | 2025-07-22 00:24:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| d263331a-289a-3575-9788-c23feb60940f | -13.70144 | -45.7043 | 2025-07-22 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c9a3f2e7-a378-3098-9f6f-5b4a6c872d9c | -10.61857 | -45.23468 | 2025-07-22 00:24:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 73bcaa5c-67f8-38cf-a89b-02633282d8ef | -15.15376 | -43.67903 | 2025-07-22 00:24:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f8d9c3f3-673d-3a21-806d-73f808a46de2 | -13.65839 | -45.72642 | 2025-07-22 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 8258e664-f7b5-3418-b852-3ed40fedeacf | -14.64693 | -46.83673 | 2025-07-22 00:24:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 60c12c4c-bf6c-3874-8ed3-49d5940495c3 | -13.69242 | -45.70559 | 2025-07-22 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1472f31a-ce95-3d13-b840-106cc3a79822 | -13.64939 | -45.72774 | 2025-07-22 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0646ee77-f2bc-3db8-90d9-9996b1c6e89d | -10.23353 | -48.06044 | 2025-07-22 00:24:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| daa2714d-e6ac-3e5d-9587-13961620806b | -14.77132 | -47.11904 | 2025-07-22 00:24:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bfa3850e-c7c4-396e-b62d-9878ca45480a | -18.80677 | -44.41682 | 2025-07-22 00:24:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5feebbcd-d0b3-3dd4-aa24-edcc6691ed0b | -9.95977 | -44.28147 | 2025-07-22 00:24:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 68a5da5e-3a02-3fd5-b7e1-12e5e24c2baa | -12.65873 | -44.2743 | 2025-07-22 00:24:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b34f3620-fd83-3ad2-9502-1d2d526695ce | -19.73125 | -46.03605 | 2025-07-22 00:24:00 | TERRA_M-M | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README2.md)
