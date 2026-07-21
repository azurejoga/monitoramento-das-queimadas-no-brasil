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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b4f2d49-b966-3ea1-9354-94d4a04ef258 | -10.80163 | -50.42601 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 370e1a55-dbd5-3d0a-9ee6-ea610600b693 | -10.513 | -50.28997 | 2026-07-21 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9721309-ad93-366a-8619-c7a79a88b26e | -13.31234 | -45.13354 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 584692d6-93b3-3afd-a249-00c6f39fda5d | -14.79085 | -57.2837 | 2026-07-21 05:04:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 818338ab-0bff-3cc3-9067-843a0bab7faf | -12.51552 | -48.25243 | 2026-07-21 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0873e22e-0c02-3002-9da8-34565e4d7449 | -10.86587 | -50.42243 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e1d8dbe-cd6f-3469-9b76-04fb82f34345 | -10.47044 | -62.45051 | 2026-07-21 05:04:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d38322e-b389-31ca-a193-4e92cbc059cb | -7.68431 | -55.36892 | 2026-07-21 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b431c854-50d8-36dd-b183-e6ef79c8203c | -13.29959 | -45.1291 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7af000e1-8319-39a6-914d-223acf8b840d | -12.69412 | -45.32819 | 2026-07-21 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ecdea718-054c-3291-b280-f4660f5cd88f | -11.83725 | -44.77079 | 2026-07-21 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7891dd80-529a-3eb7-9e5d-292f4bea63fd | -9.10052 | -59.40002 | 2026-07-21 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0ca8d4b-9ebd-3fee-bbf9-450a02708d61 | -10.55204 | -56.33562 | 2026-07-21 05:04:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0caec97b-320d-388b-9af9-b21afb619096 | -13.30161 | -45.13236 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 601b6d70-f079-3844-82b1-215ed6942d6c | -13.21144 | -54.38399 | 2026-07-21 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65638ffd-088a-362e-b2e6-9e82730f278b | -11.63254 | -58.28087 | 2026-07-21 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f1874e8-101d-31ee-8e6a-05f20909c7c3 | -11.98092 | -47.10307 | 2026-07-21 05:04:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0efbe430-c8ad-35b4-a2ea-e8ff52951715 | -13.30202 | -45.12892 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 5941d211-7db6-31eb-98cb-a9580614036e | -7.68493 | -55.36506 | 2026-07-21 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 741f9096-b8bb-3510-9217-92a4340ec1df | -11.62871 | -58.28014 | 2026-07-21 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea802e0d-6e66-3b93-9a37-b5c1750d2f23 | -10.59642 | -46.53708 | 2026-07-21 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6529490-ef57-3600-ad75-4618c587ee2a | -10.85789 | -50.42565 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69cb7ff5-caa6-3983-90d4-bdff8eb70bb7 | -9.08374 | -50.58743 | 2026-07-21 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c98bce7-b18a-3af4-a8a9-eccf280724bc | -10.6332 | -47.4833 | 2026-07-21 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ce53aa5-1647-3b54-806d-920f2429d9ae | -10.85645 | -50.42778 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b15c57db-745c-3c2b-b299-4a355f9f11bd | -13.34565 | -54.34763 | 2026-07-21 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56dc0b31-76a8-3a1e-b6bc-d5d813d35cfe | -12.08312 | -53.34051 | 2026-07-21 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e30a187b-a578-3c69-bcb3-125e62656d7a | -15.46181 | -54.35409 | 2026-07-21 05:04:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02a18ee3-0f8a-38f4-ade0-3a64956c2d6a | -10.54852 | -56.33503 | 2026-07-21 05:04:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d954c5ff-d974-33b2-b69e-b13ae867ef7d | -13.30002 | -45.12565 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da571fcd-4510-3235-85ee-0d933b9dab20 | -11.37701 | -47.49085 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e0f2091-8a45-3fc6-89b9-356084cf6f0c | -12.13719 | -48.25639 | 2026-07-21 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0e7296c-5162-341a-a40d-cabfaf21d5aa | -13.34125 | -54.33237 | 2026-07-21 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cdbe8b7-e5f3-3ca5-94ed-59bdfe9c5427 | -10.55687 | -56.32827 | 2026-07-21 05:04:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8a8fe85-ac1e-312a-8da5-f92ecd58829d | -11.83771 | -44.76701 | 2026-07-21 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2667564-63f7-3afa-ad46-d49b81a1a07f | -11.36821 | -47.49661 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb682ae0-a911-3cac-8ff5-836a3f172bd3 | -10.79797 | -50.42546 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bd75fc6a-416b-335c-bf32-c2cfadf3b38f | -13.30574 | -45.1433 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09e5d2bf-903e-3ef5-92b7-d3f8d3b62f15 | -12.88444 | -58.29174 | 2026-07-21 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3987e51d-e2a2-3a3a-b39a-30ff2aee0f5a | -10.86441 | -50.42456 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ede92612-ce3c-3cc4-89ae-7353613a1415 | -8.75509 | -49.07863 | 2026-07-21 05:04:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ff5b8f36-ea6c-3505-bdb5-1c047b5e36b3 | -10.85056 | -50.42455 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7a8a038-5e19-3813-b79f-cbaeefc23610 | -10.85422 | -50.4251 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb0cab48-5c09-3d8b-be2f-8adfde656d75 | -10.63258 | -47.48766 | 2026-07-21 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9dea32fe-509a-3f61-877d-de0e836db662 | -10.82362 | -50.42933 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4dace3ed-0d20-3274-89fb-72a477a279a0 | -10.74627 | -44.83817 | 2026-07-21 05:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2b1e2050-9213-33ff-af3e-34f7ea5db525 | -12.3518 | -47.4277 | 2026-07-21 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 686ba9ea-8918-3816-899b-aaa75fe1a5ba | -10.62818 | -47.48711 | 2026-07-21 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 077dc609-e8e1-3f6c-a097-4814d8e0634d | -13.30656 | -45.13639 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 78b3a93e-0430-3a07-945a-fe7173a8962d | -10.55526 | -50.2766 | 2026-07-21 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11fe9aff-2cb2-3d16-b3ff-b13d0fd15658 | -12.5241 | -48.25357 | 2026-07-21 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba282964-e3e0-39bc-9515-5d9d2af2fa8e | -9.08189 | -50.5996 | 2026-07-21 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83e08422-12fe-3811-86bf-8f2e55d57da9 | -9.10408 | -59.40483 | 2026-07-21 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4fd99c5-bb4e-383c-ac46-6aa801cd042d | -13.68825 | -48.77877 | 2026-07-21 05:04:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f4f6837-351c-3aba-b21f-12af322b5cca | -12.14145 | -48.25697 | 2026-07-21 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52c788b6-b249-35b0-941a-2f85475c5d73 | -10.8622 | -50.42188 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bac52b02-9d95-358f-88d4-2715e79d3d0a | -10.85708 | -50.42345 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e96b20bf-dfcb-32ba-b631-af95b61ec7f8 | -13.21477 | -54.38454 | 2026-07-21 05:04:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d7f955f-28f0-32ea-90d9-eb99073be3b7 | -13.56375 | -46.11407 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da328483-a683-3ad9-ade5-b32f59eaffab | -11.5978 | -58.50607 | 2026-07-21 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f64cb45-eed2-35df-b6b9-2402a9d4b239 | -13.31193 | -45.13697 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fc86a541-81ac-37a2-86e8-43730bdbc98a | -11.39754 | -47.50638 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c18fc6b6-9008-341a-aa0a-c7fc53c816ac | -10.37967 | -48.32449 | 2026-07-21 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d57ebf64-5bcd-3e03-9d0d-36e2c8648a81 | -13.30821 | -45.12257 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 925986e3-373f-30ad-9ae2-99a3eeaaafdf | -12.45988 | -46.51883 | 2026-07-21 05:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4460118-73c2-3566-96bc-ef543e591c84 | -10.60112 | -46.53761 | 2026-07-21 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2b35965-f0ae-3ac9-a0a0-36aedcde8963 | -11.17143 | -54.12277 | 2026-07-21 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f97773fc-bc51-3fc5-8321-0cb188ff0456 | -12.05666 | -58.04147 | 2026-07-21 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2737263a-d2df-3a04-9ed8-0617d092d57e | -9.09981 | -59.40403 | 2026-07-21 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36684cc6-99ae-34af-a4df-54676f9021f2 | -8.94368 | -47.60509 | 2026-07-21 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de9acf73-5dce-3b32-acdd-053d753f50cb | -11.38662 | -47.49437 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f1c82aa-ca8e-3800-9e3a-9e1c6d618746 | -11.91163 | -43.84811 | 2026-07-21 05:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93c96554-9a6a-390c-81e6-63f2f8ee04e8 | -10.86156 | -50.4262 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a190ef74-6f89-3fc6-95b0-df6cdf5a9413 | -10.31189 | -49.64437 | 2026-07-21 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 464f6486-1820-359b-abe1-b28dc7dc6198 | -10.86074 | -50.42401 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d1db0fa-960a-36b7-8cfd-b48141034964 | -10.86012 | -50.42834 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99e4d922-ecaa-398d-8862-e702f792621f | -7.68556 | -55.36121 | 2026-07-21 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01ab8a67-9a33-31dc-b770-b1802f80dba1 | -10.01221 | -65.05409 | 2026-07-21 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e49bf821-dec4-30f5-9249-97a0bc3b89b5 | -13.31276 | -45.13008 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6730525d-b9e7-386b-933c-bbdb39d4bcff | -12.06041 | -58.04216 | 2026-07-21 05:04:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fc36ca8-582c-3d2d-b0d4-6dc376570581 | -12.13664 | -48.26047 | 2026-07-21 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e13a6db6-33e5-36b3-b47d-4d5c6518017e | -13.30697 | -45.13296 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 858238f0-2239-3a50-a121-72381658e80a | -11.37771 | -47.49335 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09204c0b-34ac-3e7e-ba89-467ed2bb7404 | -13.68773 | -48.78275 | 2026-07-21 05:04:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffe2baae-296f-3edd-ac6a-1e5c37c25692 | -12.66086 | -48.20036 | 2026-07-21 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06111b52-79df-31bf-8f7e-812818cef642 | -12.66516 | -48.20102 | 2026-07-21 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44b97d0e-ec6a-3847-92e5-03b94667bf31 | -11.37328 | -47.49273 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a44f0ab-65b1-347c-9206-2c76b1bb12d2 | -11.3448 | -47.99637 | 2026-07-21 05:04:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aaae642-aa04-3e03-bebb-a29af7085846 | -8.75438 | -49.08343 | 2026-07-21 05:04:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 21616efe-a558-3a8e-86da-c875c62de0eb | -7.68208 | -55.36065 | 2026-07-21 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c49c3a29-9c02-3836-9514-250443513214 | -13.56877 | -46.11477 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f29bf90-fdf0-36c8-b7d1-45ca5a335096 | -12.13801 | -48.25789 | 2026-07-21 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4230caa6-fc36-386a-946c-81f6f6c32b56 | -10.7943 | -50.4249 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d51245cc-3b11-3a16-8e0f-7baee08067cf | -9.09909 | -59.40808 | 2026-07-21 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5dc3106-fbc4-38fc-8eeb-00c62205a2ef | -12.08702 | -53.33748 | 2026-07-21 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b65e7af-c44a-3fee-b02d-07ea541e1e3b | -11.37528 | -47.51077 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a351ea7-2541-318f-ad91-fac032a30d26 | -11.83534 | -44.76978 | 2026-07-21 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adc3698b-55c4-3fea-b095-68c6bdd3a760 | -13.30615 | -45.13984 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e5bb09e7-99c9-3ec9-95aa-d07ef524f6fb | -19.18413 | -47.35997 | 2026-07-21 05:06:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| deea22be-9a6b-3258-817c-34862f3bcecb | -20.88766 | -57.48431 | 2026-07-21 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README13.md)
