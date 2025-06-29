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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fefa1d3-aba1-3d41-a871-e96129fff06b | -12.48477 | -58.47105 | 2025-06-29 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82abc328-11d3-372f-a33a-d858994e857f | -13.1417 | -56.80996 | 2025-06-29 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07202a9e-f2a9-3d0f-85fb-32c1fe29123c | -12.11105 | -54.58422 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11168564-92d1-3011-927d-745f8224a066 | -6.62634 | -47.28502 | 2025-06-29 05:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6cacf7c0-11a6-30f4-9989-901e50b2670a | -12.62515 | -54.21553 | 2025-06-29 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 75eb5028-d5c3-39b9-ad14-b40b5f2c485e | -12.10184 | -54.6738 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc855c2d-ac33-388a-a219-fd08c5c1ba16 | -15.72971 | -49.56009 | 2025-06-29 05:25:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1c04b38-72c3-3e65-84d6-aaf518d127e2 | -12.98089 | -54.685 | 2025-06-29 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 045bc532-371b-3417-9ed2-3164309516d8 | -12.99485 | -59.0544 | 2025-06-29 05:25:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6222c249-09f7-3b78-8b0f-cb8254d184f7 | -12.62097 | -54.20943 | 2025-06-29 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cb7e6377-9b29-3ec2-9ddb-ded739786ee4 | -12.42089 | -54.87022 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b127611-c72f-3cde-a29b-f05fff9cc36f | -18.78983 | -52.5833 | 2025-06-29 05:25:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 20caef42-5b5c-3387-a561-58c3180dacbe | -12.105 | -54.67032 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d6312d5-d230-30f3-857e-2af63f40b61e | -12.10717 | -54.66952 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 218c989f-fe93-3ad2-8f15-0181e07d9921 | -7.29691 | -55.31454 | 2025-06-29 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ab7368ec-8519-326d-b6ad-f77139267a2c | -12.10096 | -54.66468 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dafb308b-4d78-3aaa-b246-e076ced04c28 | -12.5055 | -58.35126 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e3c1b79-5fb0-37b1-946c-2a3eaed406f8 | -12.62582 | -54.21013 | 2025-06-29 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e07ddecb-9789-3d42-bf9f-433fb98bb93c | -13.29527 | -57.09056 | 2025-06-29 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05298e12-ce84-3517-9ba9-720df6f593ad | -12.10514 | -54.57726 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fdc4c22-38f8-3652-97b0-9ff411d7af8f | -12.99423 | -59.05862 | 2025-06-29 05:25:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b290d78d-ab40-35e4-ab1a-6d8303ab508a | -15.72829 | -49.55273 | 2025-06-29 05:25:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8939a93a-3870-3483-8cfb-e8cd61b1f762 | -12.60355 | -57.8746 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddf28793-6edc-3d9f-86ca-3bb35a347862 | -12.61117 | -57.87577 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a97e8f1d-9d85-343e-83ba-e0ef8ca8ee38 | -12.61498 | -57.87635 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7cc06c09-8cd5-33f5-9ab9-4aeee5f64492 | -12.11387 | -54.5836 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4857832-3217-31e8-9959-9dc0c8bc9261 | -12.11053 | -54.57277 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38d7324a-4bac-3847-8857-157ddd75922a | -12.50487 | -58.35574 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d05d1a6-f177-3ade-a972-f0c5ff4c7501 | -15.72766 | -49.55925 | 2025-06-29 05:25:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9c33f00-0fe2-3c40-98f8-13760461d654 | -12.09783 | -54.66819 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dabb85c8-1ffa-39f8-90af-2b065cbfe364 | -12.10447 | -54.58232 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cb29950-99fe-3957-aca8-ea35579d0f09 | -13.01731 | -53.42623 | 2025-06-29 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cacda21-840a-331f-b3eb-b88e67333a04 | -12.60736 | -57.87518 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eeb2c2ec-af3b-3718-92cc-fe7beea97323 | -14.69226 | -53.3907 | 2025-06-29 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b44ab012-614a-3561-a0c5-9785dd8f77fd | -12.61186 | -57.87094 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c01e7f9d-a141-3a5c-a98e-7c6b5722bae0 | -12.10033 | -54.66964 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e69b5f84-7afd-3253-89f6-814629fa2079 | -12.99637 | -54.67656 | 2025-06-29 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b951d8d8-594d-33bc-bf4a-3c3904072714 | -15.7303 | -49.55351 | 2025-06-29 05:25:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 813ffd5c-e9fa-344e-98d3-751c92833928 | -13.10429 | -52.29781 | 2025-06-29 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e75fa129-8c21-337a-ae38-711137b630bc | -12.10917 | -54.58297 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5236037-07c4-361b-bc18-59fce61f0753 | -12.60669 | -57.87997 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03a63a75-3496-367b-add5-2546a23dc3c9 | -12.99126 | -59.05383 | 2025-06-29 05:25:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd10ef2e-afd8-3bb5-8196-d245b65ee54e | -11.78449 | -59.32126 | 2025-06-29 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9c29a8f-691b-3f5a-a4f9-a14aff680a30 | -12.49276 | -58.46774 | 2025-06-29 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 839b2838-1573-31df-b185-df415deadfdc | -12.49212 | -58.47223 | 2025-06-29 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 21df91f7-2526-30e6-9280-3622e01525ab | -12.11168 | -54.57916 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5bdd731-cde4-3a65-82ab-236b8624a114 | -17.76235 | -52.44702 | 2025-06-29 05:25:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03c781ad-73fb-3c19-8220-f3a7adc1b8d2 | -12.11455 | -54.57851 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 204d8406-5fb8-3c6b-976f-fdeda0a46f73 | -12.47006 | -58.4688 | 2025-06-29 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de55db22-9276-3a3e-a4c1-7476c5fcf8e3 | -12.47374 | -58.46935 | 2025-06-29 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 650f814f-38c0-37d2-b73a-9525932d499c | -5.91912 | -61.30171 | 2025-06-29 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8381e449-2d2d-3268-a883-13aca7992aee | -12.10698 | -54.5785 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22f372b0-7c82-3722-8b27-5646b5c8742f | -14.53014 | -53.76837 | 2025-06-29 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a99ab92f-4ed5-3b9d-93ac-2de09216e44c | -14.53489 | -53.77232 | 2025-06-29 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 731b85c3-c075-34b1-bc88-6d1bd77027c2 | -17.76278 | -52.4428 | 2025-06-29 05:25:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75437cec-ee8e-3bfb-9ed5-e29641e1f5c3 | -13.1422 | -56.80618 | 2025-06-29 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb2243c7-bd6c-3067-b564-1e4def932f9f | -7.16076 | -49.51351 | 2025-06-29 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7b81e0c-c74c-38cb-9251-acb0428b5e9e | -12.10984 | -54.57791 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a83737b-ac08-3e0b-bb93-038c555cb042 | -12.4811 | -58.47047 | 2025-06-29 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4737b668-9772-3767-a985-c3b7c70018a0 | -13.0011 | -54.67719 | 2025-06-29 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c2f56cf-80ce-3a9d-b695-3bcfd9522d14 | -7.29636 | -55.31839 | 2025-06-29 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 86b540de-e12d-3004-a415-da165b100de8 | -12.10762 | -54.57336 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4f4dff7-e365-39ec-8a3d-18d397e2b12b | -14.69266 | -53.38726 | 2025-06-29 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1739ffba-9adb-30df-8de8-9b196339afdd | -15.73444 | -49.56006 | 2025-06-29 05:25:00 | NOAA-21 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de903517-c67a-393a-b7de-43346a236963 | -12.10582 | -54.57212 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb5fed92-287d-33b0-aee7-8f0bee1fb43b | -12.1025 | -54.66885 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e49c143b-29fe-342f-b97d-91a62c9f088a | -13.10474 | -52.29405 | 2025-06-29 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d022e60f-dbdf-3e88-8972-6aba183d6d1a | -12.10316 | -54.66391 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03c0b9e9-a269-34c7-bd8e-b4fac648ff03 | -12.11232 | -54.57401 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f8212ba-85d2-3cac-941c-3d2b72c64c8d | -12.10563 | -54.66535 | 2025-06-29 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73181077-b146-383b-879b-659694286a99 | -12.47742 | -58.4699 | 2025-06-29 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f187e78b-8175-3104-9ee9-4e1a891338f7 | -14.30321 | -59.90555 | 2025-06-29 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be251c57-5995-3a27-9a54-ccd20a59137c | -12.61049 | -57.88056 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 488240de-5d4f-3c37-8a88-9fdf84a000b2 | -12.60288 | -57.8794 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6360b54d-1a88-397a-b6d4-c96c4def31f8 | -12.48845 | -58.47163 | 2025-06-29 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 87bfc54f-6a36-3075-bf4a-dbaa985f020b | -12.5018 | -58.35072 | 2025-06-29 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55701c59-40a3-3dc1-a932-79e0f5c3ff42 | -11.78099 | -59.32069 | 2025-06-29 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4b2a100-28be-3de0-8f5a-2a8bb9e9f734 | -13.01768 | -53.42311 | 2025-06-29 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20a40818-621e-3ad4-bbc4-4d812792b498 | -21.19663 | -56.93597 | 2025-06-29 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 328b918a-b394-3d3a-8784-051bd00f7d7d | -21.02196 | -50.1775 | 2025-06-29 05:27:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 155d102a-8ed7-3929-9728-e3bb8af5459f | -21.20118 | -56.93656 | 2025-06-29 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 822047e7-6290-35f8-a1ca-65eeaecf344d | -21.02232 | -50.17254 | 2025-06-29 05:27:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2da26eae-4818-3daa-9950-3e1b6f6004e6 | -21.02243 | -50.17077 | 2025-06-29 05:27:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| efcefeb1-b209-38aa-b8f6-b329cc8fabae | -21.2017 | -56.93191 | 2025-06-29 05:27:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bb793ff-153a-327b-aaa6-19c8e4c260c2 | -11.5499 | -52.7867 | 2025-06-29 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| b01a2376-fb31-3a20-a04c-c29b8e4e0db3 | -11.5502 | -52.7659 | 2025-06-29 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| acb7c736-95ea-31c7-a93c-44eef4d262c5 | -11.5502 | -52.7659 | 2025-06-29 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 379e9d2f-a18a-389d-b17b-16a7487a6178 | -11.5499 | -52.7867 | 2025-06-29 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 02c35e35-ee2b-3333-a01b-a0e9fdafddd0 | 2.75124 | -60.36833 | 2025-06-29 05:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba2bfea9-d180-32de-83e6-b9723b233f8a | -11.5499 | -52.7867 | 2025-06-29 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 13433428-453a-37e1-89f8-572a7c822b8d | -11.5502 | -52.7659 | 2025-06-29 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 45ab6b36-459f-3484-a048-6607b87df4c3 | -9.72136 | -56.18552 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7043762b-8216-34a0-8737-1d58a287a539 | -9.11053 | -59.04949 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1b1e549-77da-37d0-9cd8-c2a50213d251 | -9.11231 | -59.05378 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f24028a3-c654-3444-b65c-6300c34a9c0c | -9.47484 | -57.83667 | 2025-06-29 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c1985a9-50e6-3279-a399-8690456143b9 | -9.10802 | -59.04709 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b67fb25b-1de6-36a2-8e1e-9453506b5994 | -10.03647 | -54.33564 | 2025-06-29 05:50:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7106bda-5a9d-3358-b79f-1a838c02f4c3 | -9.11273 | -59.05078 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a7abfc3-d27e-338a-853a-df8b0bf9ad39 | -9.7027 | -56.18293 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e3d23c3-1daf-321a-a1a5-3e7ce5864cf4 | -9.35013 | -58.83909 | 2025-06-29 05:50:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
