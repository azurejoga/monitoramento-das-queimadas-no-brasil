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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2d9c057-5865-3fb9-9943-835c5db176c6 | -12.10229 | -44.75093 | 2025-05-18 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc733143-9633-3dfc-ba00-bfedd06ae75c | -9.32092 | -44.83344 | 2025-05-18 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62a23c73-cbdb-3f88-80ff-261c5f0af2dc | -11.42638 | -54.30038 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fbf4624-18aa-3e91-a6e9-33e543e3a4e1 | -11.4225 | -54.29339 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1d1149a-10d6-36a7-8656-5a0c28364abb | -12.29461 | -52.47146 | 2025-05-18 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 008dc1c1-cc38-3913-a152-520ced879d51 | -12.12072 | -54.66436 | 2025-05-18 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4e23a8e-d962-306d-8e07-82e8e75f3802 | -11.57806 | -47.61246 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90cf2a2e-74eb-3e5e-8eca-3627cdf61fea | -12.12131 | -54.66133 | 2025-05-18 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b0762a9-1f6e-33c2-8dee-6090f68b79e1 | -12.36704 | -56.40398 | 2025-05-18 04:19:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca538cc0-12fc-3dfa-8e78-37b7ca84dbbc | -13.03732 | -53.72082 | 2025-05-18 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb812899-e8ba-3fd3-a7d9-f6842bf934cd | -13.30898 | -45.39776 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 31f26d3b-3e61-3db2-898e-69c010b93245 | -13.58528 | -47.36928 | 2025-05-18 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f83a0b8-297e-35f2-b154-3deff329186f | -13.29896 | -45.37411 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 850f9ab5-ad7c-3fa6-a243-0b90988bf0f3 | -11.79021 | -49.31623 | 2025-05-18 04:19:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ad87ad2-d119-327e-a577-328834664550 | -14.01992 | -55.13049 | 2025-05-18 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee820d36-17b5-3ce4-8e6e-f18ef1642b29 | -10.79125 | -48.83677 | 2025-05-18 04:19:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ccd3ddfc-0a3f-364a-b1d6-43933a36a431 | -13.14499 | -56.81057 | 2025-05-18 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97c5c051-c542-3847-b6f4-14fbfc9463b8 | -12.59294 | -45.44426 | 2025-05-18 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58669db7-d53d-3aaf-8195-8c46ef6a035b | -12.03498 | -54.96622 | 2025-05-18 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac32ef3f-b3ac-33b1-a69e-83a993a6bd3b | -10.65999 | -44.49352 | 2025-05-18 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7a0a0d28-e63b-367e-9390-80aac69a941d | -12.12641 | -54.66227 | 2025-05-18 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08fabbb5-e5f1-3bfb-9f49-73f9e543d458 | -10.67745 | -57.60745 | 2025-05-18 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25f30e0b-ed85-31da-a842-c0c14a9a869d | -12.12013 | -54.66741 | 2025-05-18 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01be2f9c-a17d-3778-90a5-37c1c326f1b2 | -12.04017 | -54.96728 | 2025-05-18 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d2189e8b-f8cc-32e7-add4-de8c5795e8ba | -13.65598 | -47.88817 | 2025-05-18 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7d53cd0-d07d-3cdb-b347-678fa1beb1f6 | -13.50518 | -47.39693 | 2025-05-18 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f17dfd60-73e5-3bef-b93d-bafd5cdcfc18 | -11.48588 | -43.80673 | 2025-05-18 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3d94b73-1613-32e5-ba53-c91bfb431a29 | -13.56238 | -43.51062 | 2025-05-18 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee538fed-dc1c-3dac-9aae-ad102ff9d4a0 | -11.40047 | -52.96111 | 2025-05-18 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a5b9112-97e0-396f-b44d-4613942f58a1 | -11.58208 | -47.6093 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 80f5d956-c435-38ea-8135-5c9b3440b73c | -12.16735 | -48.80853 | 2025-05-18 04:19:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07cdde69-5612-3a78-b67f-204c4e2ee712 | -9.65922 | -45.2311 | 2025-05-18 04:19:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3b7831f-75ed-352a-b075-375a8ffc84a8 | -15.29034 | -53.20223 | 2025-05-18 04:19:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2f37bd6-4520-3865-9d25-aa3d15b991dd | -11.56361 | -47.87338 | 2025-05-18 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88de8172-3724-35f7-88b6-b42bc44a349e | -12.25735 | -44.60432 | 2025-05-18 04:19:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59aefe04-9e90-3bab-837f-6130100d63ff | -12.03436 | -54.96952 | 2025-05-18 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 615a6e08-6023-3acd-be44-e9a4b2d6cdc1 | -14.01368 | -55.13546 | 2025-05-18 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ac7a3ca-7b2c-3cf6-9456-74f392275e06 | -13.29618 | -45.37 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa26f1a6-54e2-3de4-a9fb-09fa1fa5785d | -9.29381 | -46.71212 | 2025-05-18 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 520a732f-a769-38fe-8987-05410b1c4771 | -13.04298 | -53.71672 | 2025-05-18 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed126806-3a2a-38e3-b7c5-5b085bdf781e | -15.82393 | -48.1256 | 2025-05-18 04:19:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fb161558-0ca4-398b-a8d0-b017fc804db0 | -12.16381 | -48.80789 | 2025-05-18 04:19:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b72b129f-6d27-3024-b957-e7df6e11e067 | -13.88961 | -43.44847 | 2025-05-18 04:19:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f631ca7c-6d63-3a0f-9547-187353e89632 | -11.39677 | -52.95528 | 2025-05-18 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5b83c3c-a016-305a-a2a3-79888d4a0f88 | -13.29841 | -45.37769 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e923f49-1186-34e0-8157-30632acf732d | -10.75615 | -57.23058 | 2025-05-18 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 014c533e-d108-32c6-8d8e-18a36f3676a6 | -10.47688 | -49.14628 | 2025-05-18 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bb0ac1bd-4bef-3a72-bbc5-06e2418f350e | -12.299 | -52.47228 | 2025-05-18 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 628e0913-bd9f-382f-ac67-1169b5ad2903 | -13.21482 | -43.14671 | 2025-05-18 04:19:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f673dac4-e962-37eb-ae87-650804a582e4 | -13.04087 | -53.7204 | 2025-05-18 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 096ab1dd-bea6-372f-aaef-e8be9de690c3 | -12.12524 | -54.66834 | 2025-05-18 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7fd9415-484f-38fa-a283-22a02149c181 | -11.42192 | -54.29642 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8af3af0-ce4e-383c-83cb-cf4a994a2bb1 | -12.03955 | -54.97056 | 2025-05-18 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dda9500f-2f55-35ce-b8b4-af6363deea8e | -11.40137 | -52.95619 | 2025-05-18 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2295f5bc-8bd4-3850-91ce-2a436a255c43 | -13.04201 | -53.72179 | 2025-05-18 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b64d6b3c-df4c-3972-abd9-cd01c9e5b2c6 | -10.65664 | -44.49299 | 2025-05-18 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95a80d66-d00e-38d0-8434-36ccfef38d07 | -8.43146 | -49.10176 | 2025-05-18 04:19:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a0adf4a-98d7-3ba2-9149-0607608bed68 | -9.66688 | -49.7141 | 2025-05-18 04:19:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e48d1eaa-e307-3bfa-bb2a-151269596b8b | -8.43524 | -49.10235 | 2025-05-18 04:19:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 637cbbb8-4386-39dc-bb26-15cd185427e0 | -22.77582 | -47.62669 | 2025-05-18 04:21:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8042cb0a-048e-3da3-b7b9-0809f67d7c35 | -21.15358 | -48.00245 | 2025-05-18 04:21:00 | NOAA-20 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 559fd095-a148-3810-8ca8-9deb8dc134a6 | -17.14739 | -44.80923 | 2025-05-18 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e393d88e-8d6a-30f9-a7d2-76c8480d27ce | -22.74425 | -47.1403 | 2025-05-18 04:21:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1f69dbcb-3ac0-3098-9ab1-f36ff5846a66 | -20.764 | -46.76807 | 2025-05-18 04:21:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 95264ff1-536c-3965-8a0b-3f97ed608252 | -17.74887 | -56.31015 | 2025-05-18 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3153b177-25e9-39ab-b096-893bba911983 | -17.6663 | -46.68645 | 2025-05-18 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6640ac57-4e5c-37c3-8199-50b71c1716de | -23.3369 | -46.77167 | 2025-05-18 04:21:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 559dae07-a12e-30a4-97d3-2031c6177675 | -19.06654 | -53.45724 | 2025-05-18 04:21:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9f554ea-f64a-3c43-b873-4b0a856ddcb8 | -17.00859 | -49.78218 | 2025-05-18 04:21:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06f44fad-b537-3ffd-b752-63d34c3ae87a | -20.92738 | -44.40252 | 2025-05-18 04:21:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0151113-4a9d-3e9d-b4ba-a627d4401397 | -17.74296 | -47.06763 | 2025-05-18 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcebe8f3-0465-3804-9dfa-ca93e162063b | -23.63183 | -46.42527 | 2025-05-18 04:21:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 959aa8b3-49ce-3b51-86f7-a7422a23deab | -22.77249 | -47.62609 | 2025-05-18 04:21:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 2ae5b652-2cf1-3f14-b053-367e0dfbfd29 | -21.18041 | -43.97776 | 2025-05-18 04:21:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a8fade97-5afd-3a5b-914e-a65d7535c2d7 | -23.60882 | -49.01015 | 2025-05-18 04:21:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 431e9c66-2e70-32eb-b195-64b7d810e3d8 | -20.72575 | -54.40755 | 2025-05-18 04:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf942435-b958-3e7d-943c-ea7d9b5f651d | -23.34031 | -46.77227 | 2025-05-18 04:21:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 562dd8c1-ed66-3d77-b2dd-1ce23f3e708e | -17.67426 | -46.83304 | 2025-05-18 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d400db1-bedc-3f93-99ad-fa61eb44632f | -17.92112 | -45.53238 | 2025-05-18 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94c6d603-60d2-37ec-a519-01ad79295184 | -17.91771 | -45.53182 | 2025-05-18 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d404ed-b883-3e01-b8b0-55b755bcd732 | -17.76234 | -56.30798 | 2025-05-18 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 560a3bd0-3146-3a74-8956-ca30cac1caa4 | -21.18581 | -53.17878 | 2025-05-18 04:21:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41e3addf-3528-3102-9069-767aad082bb5 | -19.41705 | -44.34099 | 2025-05-18 04:21:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27ca499f-fef8-3d1a-8e06-358a75232208 | -17.76168 | -56.31113 | 2025-05-18 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 715b3cf5-a146-3077-90ef-81b9938bbb15 | -19.0624 | -53.45633 | 2025-05-18 04:21:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49cfff3f-61e2-3660-9bc8-a1ccbd0a91e4 | -23.61213 | -49.01077 | 2025-05-18 04:21:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9a44f4a-4a1e-3608-9a78-2b7a56cef450 | -17.75396 | -56.31132 | 2025-05-18 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c307aeb6-2240-3e1b-ac82-c5fd19c9f4eb | -20.95139 | -56.60701 | 2025-05-18 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| e713c55d-04c2-32dd-85bc-43648b3f3e06 | -20.95371 | -56.61163 | 2025-05-18 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3069a65e-08a0-3a58-a034-1ee9baafafa3 | -22.67811 | -42.85307 | 2025-05-18 04:21:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f193f850-7ce3-3872-b956-52ad12246448 | -17.57872 | -47.48446 | 2025-05-18 04:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4159268b-13f5-3947-8dfc-0261cf99c13e | -23.6049 | -49.0133 | 2025-05-18 04:21:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4485b068-e47d-3279-91df-b02fa2799262 | -20.47915 | -53.67539 | 2025-05-18 04:21:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d4d07b5-225d-393f-8c76-73055025adfb | -17.91733 | -45.53219 | 2025-05-18 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cfb15de-b20c-32f1-b42a-0464d60a7854 | -17.14334 | -44.81263 | 2025-05-18 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da34d942-a46f-34dc-84df-f3acbcab6949 | -17.77804 | -42.80922 | 2025-05-18 04:21:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 487bde98-104b-3571-b67e-5c70bc2dec7b | -20.95627 | -56.6081 | 2025-05-18 04:21:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 091a6031-756a-331a-86e1-0ace07bf4faf | -23.4062 | -46.55554 | 2025-05-18 04:21:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dffef3b2-046b-3a27-a4b2-89225207adbd | -21.17977 | -43.98266 | 2025-05-18 04:21:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| be6f8e47-f10a-3914-9e31-578a58c715be | -17.14798 | -44.80528 | 2025-05-18 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README6.md)
