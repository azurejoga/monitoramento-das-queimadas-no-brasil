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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d211c33e-ecbc-3053-97fe-caeb5c6d6217 | -12.26771 | -50.72392 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4cc31034-8a09-350e-b332-d12f0c6312da | -12.26571 | -50.32257 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36ce7b89-efc2-3b69-87dd-78b9472a6335 | -11.95214 | -50.67826 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0459bfad-a12c-3811-a3ee-5afd5bc4a26b | -10.25173 | -55.25309 | 2026-09-26 05:12:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d732d07c-b35e-3b91-a9d3-593380e7aef9 | -11.90728 | -50.58457 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d160e9b-01b7-39b6-a412-3b3656764155 | -12.13578 | -57.17599 | 2026-09-26 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7633114-ba4a-3e83-86ae-3a3193a9cd6c | -11.79924 | -50.59897 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f8eac42-3c09-39cb-a475-34d0a8ced797 | -11.89309 | -50.57675 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c83e46c-6530-3aa1-a4cf-10d49d8a676c | -12.18382 | -50.33027 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 8c73bc68-0f80-31ea-a2b0-d60249857def | -11.03402 | -54.04669 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03fbe227-9372-3103-b3ce-00337b33c842 | -11.86168 | -50.54448 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54ebea18-826e-3575-9594-574713fdbe31 | -8.22927 | -54.73739 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b14c43d6-9f1b-3717-aa10-c366ed920ebc | -12.26326 | -50.35654 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8520808b-2bf8-31c4-ba57-ce413dd0b3d9 | -12.59826 | -51.94709 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ca107ce-8c52-3e7f-9446-dc9c8291f8c9 | -11.90319 | -50.58385 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62f79b27-6cbb-3808-bdad-d80470437c86 | -8.22503 | -54.74109 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fce13415-4b08-3573-8993-40169994bf0e | -11.9401 | -50.69397 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8aedc5c-1e3a-39d0-9979-b326b0f891f9 | -11.17947 | -50.05123 | 2026-09-26 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9ddd660-58e4-359c-b318-13a10865c45e | -12.1693 | -50.3221 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4c61c92d-34be-304f-ba0a-36ff14302106 | -12.25379 | -50.30887 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3aac5301-42e1-30e9-8518-db91735d2f70 | -12.27304 | -50.36094 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef072055-9a69-3238-b0bd-e5f612528962 | -12.59344 | -51.94532 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ca2c323-ac7d-3f0f-9baf-7c8f9c6852b3 | -11.99506 | -50.74968 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09c5025f-8f53-3ebb-8ff0-76ac600c6e6b | -11.92569 | -50.59883 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 44232164-8f21-30ae-96c5-00fd3b15b615 | -11.2746 | -54.43549 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 29d05406-da37-31e3-9537-a625ee33e0a8 | -12.6026 | -51.9466 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c526dc6d-e408-376b-aade-f2a166147873 | -9.53998 | -56.15986 | 2026-09-26 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af37cae0-11d3-3809-9375-0f3a122da40d | -12.26481 | -50.34441 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab7211ba-2866-3b96-89dc-6fb01e4fba80 | -8.19297 | -54.82344 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c08b6dd-d6a1-3500-9abb-6e1401bb0c72 | -11.02881 | -54.04963 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8dd84764-5b18-3e3c-b880-b809c7e7b2f4 | -12.00404 | -50.30441 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa7f255e-55f1-36e3-90a6-2ebdf4052c4a | -12.13709 | -50.30264 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f80e0382-6b2d-307c-808d-db1fc5a90891 | -9.63717 | -55.13139 | 2026-09-26 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e864300-b9a9-3183-8587-136415ef752a | -12.26133 | -50.3591 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10b358c8-83ec-3922-8f0d-dda998d7afe5 | -8.20031 | -54.79908 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1a61799-4c7f-3fa0-a51f-a7b5a825350d | -12.94573 | -51.06374 | 2026-09-26 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eb943acc-415b-3fda-aedc-7233cd9bf306 | -12.15985 | -50.31461 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7ea586e-1ea1-31f7-ba89-87cbf06acb94 | -12.60284 | -51.94773 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16c5d731-98c3-3d5b-930b-040e041da71e | -11.1704 | -50.04063 | 2026-09-26 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f9640a7-a425-326b-b97b-76c12926d62b | -12.26352 | -50.34086 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 807e58ad-ce72-309f-9888-2eaf5413a22b | -11.94576 | -50.68896 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2430ebc3-3ac0-342f-9864-505ac03c2786 | -9.5117 | -54.66148 | 2026-09-26 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cd3505c-546d-3aa6-bd34-f9c71d66fe86 | -12.2652 | -50.34137 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b8674bd-6c97-39fb-be3c-b4a344c42e16 | -12.24364 | -50.71478 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc94d5e0-7919-3bae-9b25-c5eaa5b5b3ba | -11.95709 | -50.67894 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71cadce8-630d-39d3-abac-103c7efc0dd7 | -12.132 | -50.30194 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc17f211-ce36-345d-9a18-c6158c527ac4 | -12.13239 | -57.17545 | 2026-09-26 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 656d406a-2c8a-3179-8eef-d71f0452d32f | -9.63656 | -55.13555 | 2026-09-26 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec0da60-f423-37cd-b4b1-f851cd60d326 | -12.26795 | -50.36025 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e52ae69-649b-376f-b7a4-26845a553ae9 | -12.26834 | -50.35722 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af3af2c3-3e29-3f6c-adc4-566469e07adf | -12.27248 | -50.84566 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e347368c-5bec-3e7b-9a1f-0f56a84729bd | -12.2085 | -50.33985 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21accb3f-490e-361a-8c2d-bf921386e0f5 | -12.0274 | -50.64985 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbe5f9c2-6e48-321a-b274-1c212e7f8691 | -11.9416 | -50.60093 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e9fe647-f5dc-3430-b40c-9d2c039a6212 | -11.17474 | -50.04746 | 2026-09-26 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 158e1183-715f-3b38-8653-44e1094ae572 | -12.25734 | -50.32175 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7c915cd-e579-310e-bb02-a8f2d32d8941 | -9.51538 | -54.66207 | 2026-09-26 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e78214f9-0e62-31ac-acd1-d495d4c14314 | -12.12767 | -50.29517 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47fad3e4-f033-3053-bdac-d784d527992b | -12.0878 | -50.23995 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45ce0ad2-176a-3658-b3aa-9b931721c21b | -11.96276 | -50.67393 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1613af1f-c530-336a-a6e7-25cd766d2780 | -12.2699 | -50.34509 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f683ae2d-f2d7-3ba2-8d0e-f02b98d6e99a | -9.54398 | -56.15662 | 2026-09-26 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09eb8858-b1b8-305f-800c-4df669abdb56 | -8.29734 | -54.7521 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a333f9ea-92fe-3ba0-afbc-ba2a5c820d7a | -11.05746 | -54.19149 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 851a5604-f896-34e5-b219-5b92b87e1047 | -12.21829 | -50.34426 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3f69d728-e313-34a0-9a02-b455457de8be | -11.27842 | -54.43607 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0c53ac68-4d2c-3967-9308-d46343bd8712 | -11.87888 | -50.56894 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b62b6074-76c5-38d5-95a3-84d4767d806f | -11.99971 | -50.29763 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5175dcc5-c78f-36a1-b448-7daa623d1964 | -8.22865 | -54.74163 | 2026-09-26 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce6ae846-46d5-3394-996a-570058574648 | -12.27267 | -50.72461 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 51945eb2-0de0-3adb-a2f1-2502bbbb31c6 | -12.26824 | -50.3446 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa571d6c-a827-3905-a820-8f8ee0fec01f | -12.20812 | -50.34288 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1001bc87-8ff9-31d5-bc04-8de95da0c20f | -12.24763 | -50.3575 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93d87ae1-8aa3-3a09-93ed-a22ced8fc655 | -9.51234 | -54.65711 | 2026-09-26 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c468fffb-fe5b-307e-9243-f458596fb1c9 | -11.96844 | -50.6689 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5d8bf66c-2d1f-36dc-aa15-8deaddabfef2 | -11.93236 | -50.59378 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 29e0aca1-585c-32e1-81cb-85fd1881bded | -11.93662 | -50.60024 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1aa367fb-ceb0-391d-be99-99dc0c756299 | -12.1606 | -50.32129 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e5ac16e-dd4c-3a88-a39c-2fdc734faa90 | -11.92738 | -50.59309 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9665445-7e47-30a5-b455-f0d1d8e0d6a5 | -11.02943 | -54.05116 | 2026-09-26 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08a931db-fab2-3312-8b33-98c0c85f4d63 | -12.17402 | -50.32584 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 24189770-a970-323c-bca3-d14b885d2f7d | -12.59802 | -51.94596 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1981191f-81a9-3712-a1da-efa086a45e3f | -12.26752 | -50.32312 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42020fc2-b801-3d8c-8b9f-4cca2a96083c | -12.14141 | -50.30941 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| bc1580bc-d878-3d7b-9e6a-328ae6c33fcb | -12.2132 | -50.34357 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5c00da32-f9c5-38e0-9db3-ac034a2b859a | -12.6068 | -51.95328 | 2026-09-26 05:12:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1f99926-0d7d-3474-aa75-f515cee29ca3 | -12.24725 | -50.36053 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| def18b8b-5273-3274-8f62-cb1ab7d07a9f | -11.95142 | -50.68395 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f48d146e-82a7-3413-b786-c77cd4cbf0f7 | -12.25851 | -50.71684 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 416c16a3-5b96-3603-ae9a-0270f50f0c67 | -12.2715 | -50.36049 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96017980-2e6a-3d61-928a-e9c3d112dacb | -11.99778 | -50.75372 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b095fb7-a4b6-3146-8f5e-8f3fd93c2a4a | -12.00442 | -50.30137 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0755d4c9-1841-3da3-a0cb-4bcfc7afc10d | -12.24859 | -50.71547 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e60f179-ed04-3ecc-9eea-9278f5883a83 | -12.17873 | -50.32958 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f3536cdb-7366-36b1-9d9d-9c3ba246b36e | -9.54454 | -56.15284 | 2026-09-26 05:12:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de6f1563-2951-384c-9e08-b889c6c167a6 | -12.26757 | -50.36327 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fcd26c6b-ce31-30bb-8dff-a36c5401948e | -9.64015 | -55.13614 | 2026-09-26 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a168218-fc4d-3925-bcda-e92f641016f3 | -11.94648 | -50.68327 | 2026-09-26 05:12:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f7c7ea6-aec0-300e-8112-b293de743f3b | -12.08269 | -50.23925 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f10cd2ef-5b63-35f8-80c6-f256718f75b5 | -12.17836 | -50.33261 | 2026-09-26 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |


[Clique aqui para ver as próximas entradas](README26.md)
