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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee2b1463-98d2-3681-8916-3100b0e4929c | -11.73718 | -43.45032 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdd12846-428b-3bc0-950a-7205ae0bccc5 | -11.67591 | -43.49843 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84c86e6f-a26f-30c1-bf76-817a4d5a5a39 | -11.75061 | -43.57661 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f9a91277-69b2-3a8f-9f8a-7c75a0f6e483 | -11.79532 | -43.56846 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c52f5243-d237-358b-a615-6676e50384fc | -11.52136 | -43.5173 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f2854908-0ef5-3c3c-a477-5e24f30d152e | -11.13347 | -44.59233 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b7fb1ac-01b3-378c-99c4-e4dec1956968 | -11.65525 | -43.61061 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e8460e3b-cf86-323d-bf59-309f88fd6705 | -11.22811 | -45.17452 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03d8a4d0-a551-3a18-8a34-c2d93acceef1 | -12.85977 | -43.81393 | 2026-10-02 03:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45289dd1-bda7-397a-ac4a-797abd8874e9 | -13.63866 | -41.35787 | 2026-10-02 03:55:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c943d57-3ea5-318a-827b-e129fa904e47 | -11.39312 | -43.40387 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3cac097-9258-3c9c-affc-d8865e11242b | -11.73577 | -43.57884 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 00e3c9cb-4df8-3c90-a806-5cfbaed1837c | -11.2585 | -43.5227 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72521717-d252-3e61-b2ae-a7fc80749ab1 | -9.83383 | -44.85522 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b18ba82d-dbc5-3e28-9b75-60ef4a1a4a07 | -11.74353 | -43.44154 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff9772ab-1c35-3e6e-a59a-0bc8b7c91a2e | -11.62724 | -41.83221 | 2026-10-02 03:55:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea635c6b-2cf3-33b6-aeee-251333d1f93f | -11.77406 | -43.57969 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 45a56a76-0895-37a1-a8ad-9d004c73beb8 | -12.98596 | -51.30047 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 819c2185-ae56-3ddd-b0bd-0edf4f47b8b7 | -11.67017 | -43.60812 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4272f39a-96ab-3b42-a591-c31dacbfe25c | -13.14787 | -51.228 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00a7bbe1-de2e-3247-bb16-aae0b0ef390b | -9.82995 | -44.81756 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05aeec1e-b144-372c-a593-8a8eb2629df3 | -14.09766 | -43.93293 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 496af29e-3013-3549-a2bd-15c174918c61 | -10.57162 | -50.07683 | 2026-10-02 03:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e913f19-8a5e-3310-be64-fb8d0f765a8f | -11.73666 | -43.5741 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 17f77aa3-eb69-36b7-80f3-5a2ec7b72486 | -13.33476 | -43.85893 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac87e9e2-7e7b-327b-a547-a89040dc1184 | -11.68675 | -43.59655 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08177ee2-c45a-3e1f-8ef6-1426c6cf3757 | -12.85604 | -43.80819 | 2026-10-02 03:55:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6bcf382-2bd3-308b-97bb-88f8ddf0f2c4 | -13.35328 | -44.4401 | 2026-10-02 03:55:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54c38917-a44e-3c63-9149-58c5fa4673ff | -13.85971 | -43.64047 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 686438e4-92a0-357b-8d0d-4336c78c4095 | -11.72139 | -43.43234 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96d54f97-95e4-3c52-b4f1-760bb213e944 | -9.82514 | -44.84361 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75e445d5-6d50-3344-9818-97a2d2695017 | -15.63591 | -43.2339 | 2026-10-02 03:55:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9e7a12a3-8528-33f1-a659-24aa92d5c218 | -11.16141 | -44.60986 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ab9d0082-45fd-3fbc-91f5-d484eccac2c7 | -10.91498 | -43.84164 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76bd9c17-0d19-3734-a746-7d9b20099a9c | -11.14242 | -44.60005 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af09d38b-402c-35be-b12b-67aa24553be5 | -13.85523 | -43.63958 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 436efedb-521d-30f1-b7b1-86a3d7f47990 | -11.74131 | -43.57495 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 8ab62769-d7b9-39bb-a2d8-a8339ca36037 | -13.02844 | -41.03793 | 2026-10-02 03:55:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e84abca-0c44-35e9-b7dd-fa3f6bbf7be6 | -9.77828 | -44.80499 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b5bc765-23c5-304a-8b7c-96408707c074 | -10.91019 | -43.8407 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afc93f9b-1810-3b4a-ac4c-984bdb9b1484 | -7.86869 | -44.17837 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 105e6f2c-f38d-3b78-88cc-e224dd5956fb | -15.31163 | -42.77953 | 2026-10-02 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3adf4c1b-b0f0-3352-979f-49cb4f03d019 | -11.76632 | -43.56958 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bafdd7d-2752-38bb-b23d-7e593d7ac16e | -11.15895 | -44.62309 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| c9c43057-2920-3540-bb41-90776be85603 | -10.21519 | -45.31069 | 2026-10-02 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 19c16108-e858-3983-9a6e-5b757b30cb67 | -9.50775 | -45.3354 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a39d50c-2db9-3c23-9f3a-10bed5653f25 | -10.3053 | -44.63316 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fb20cfb-8d82-3593-b821-357f3d225c45 | -11.6842 | -43.61051 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c25bcb69-1602-3dfa-8c0a-6d40c1637358 | -11.79142 | -43.56357 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a4b3d31-9d89-384b-a447-c049124b110f | -12.52302 | -43.11016 | 2026-10-02 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7c18cbb6-9634-382b-bf25-20aa4363947f | -10.2212 | -45.30825 | 2026-10-02 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9b46a70-7d80-3ba5-bb26-a9d2777cf466 | -11.15055 | -44.61224 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e18af237-ca3e-3cb7-9980-ea320ee50467 | -8.95979 | -46.83166 | 2026-10-02 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 745c335b-946a-3acc-95b9-d09204a9595d | -12.72779 | -41.8069 | 2026-10-02 03:55:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fc1c4216-15e4-3c70-8f90-8a0dc614cea2 | -13.14827 | -51.22107 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 246835b4-eaa3-3ed4-8a28-b93e5dc892ab | -13.34028 | -43.85491 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ece7356-4816-3f41-bae5-97dd5f2b74b7 | -11.15 | -44.61518 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 10a7f668-bbdc-31e7-b070-cc207d6161f7 | -10.60302 | -50.08167 | 2026-10-02 03:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d9a8540-f9d2-3476-b9a0-a10ce6ea5e33 | -11.27001 | -43.5658 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 977c993f-0a1e-3fa2-8244-e531033e4157 | -11.73059 | -43.43411 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7766ba7a-0921-3c89-8f9e-0760c886b8aa | -7.87387 | -44.17931 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fb1aa27-5269-3cf0-9b27-7a0c759c5de6 | -11.4667 | -43.43462 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 09b8a0ea-678a-3351-a394-1adcc95c8e98 | -8.9185 | -49.25737 | 2026-10-02 03:55:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73a27aba-5808-3a22-955c-fb785bd6395c | -15.67009 | -40.73258 | 2026-10-02 03:55:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 01fe6919-204d-3410-91c8-5e25516b352d | -15.11751 | -43.61686 | 2026-10-02 03:55:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c35961ab-1353-36c0-ae43-1d5cd6a70f34 | -11.1584 | -44.62604 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5719bcc3-7442-316a-8345-7bd1a374e452 | -10.30984 | -44.6372 | 2026-10-02 03:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c346187-5a50-3db9-bee1-0e8c09c65989 | -15.66643 | -40.73194 | 2026-10-02 03:55:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 06977de7-2110-3cbc-b323-2edcb4b68c44 | -11.73252 | -43.44298 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21133535-0a2a-3e58-b25d-14398efc503e | -11.6897 | -43.60675 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a25dde9-41f6-3ccf-a8c9-74d97d7f2c06 | -11.76469 | -43.57842 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 276f530a-9dee-3a7c-9e47-6829f11c6a00 | -11.45553 | -43.4174 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77b8d604-f885-3059-9089-0673463bcd88 | -11.13435 | -44.61531 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5196f817-1032-3bc5-916e-ccbf330dd31a | -11.69811 | -43.50787 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d46d6616-e8d5-32a4-8ff9-4aaeac154729 | -12.9234 | -42.44862 | 2026-10-02 03:55:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a8334371-2b14-35a9-aa0a-dbe0079addb7 | -11.78426 | -43.57646 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f9dffee-b7e8-31ae-8e8f-5bd55185fafd | -13.86689 | -43.63493 | 2026-10-02 03:55:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1036526-5788-39d8-ac60-9cf31e948966 | -11.73805 | -43.4455 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a89bece-24f1-3e9b-877a-5aa9216a9434 | -11.65882 | -43.59124 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 87f9ee93-6024-3ba8-acc6-cfee5b437644 | -11.78981 | -43.57235 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1157418e-7769-3296-a8f2-95f89b7dbee5 | -8.02655 | -47.47373 | 2026-10-02 03:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9df4157a-bba3-3f3a-b1c2-0372fe21e398 | -11.69436 | -43.60763 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 83aeb847-1936-3e6e-99b4-bfdeb2c139f8 | -11.25383 | -43.52182 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae948570-9db2-3817-ac61-dcc6dbec6911 | -12.99788 | -51.28244 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b13535ee-7172-3d77-b516-9e979c1382e3 | -10.26367 | -49.65887 | 2026-10-02 03:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| eb23eb3a-ce52-3a23-8646-b953da18f93a | -9.84668 | -44.84416 | 2026-10-02 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d3c903b-9729-3eda-9153-d27586f0c7ac | -7.87963 | -44.17698 | 2026-10-02 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d76bdfac-852d-37d3-a174-d98f00a4fb84 | -11.79444 | -43.57327 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a334bce-7ac7-375b-bd5b-b826fcf4f6b2 | -11.3477 | -43.3652 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa84553b-3ca4-3acd-bb31-9006f1e24fa1 | -15.93261 | -41.35772 | 2026-10-02 03:55:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7a79d0da-fa17-36f5-94e1-eaee7429175e | -11.67953 | -43.60971 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ae82f43-ca1d-37e8-9be1-a38856ce182c | -11.45924 | -43.42316 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bcd68605-50fe-30bd-ae4b-5e0662eb4303 | -11.24472 | -45.20079 | 2026-10-02 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71c7f9c2-5c37-3b6a-8f93-eb6cdffeefcc | -13.14663 | -51.22851 | 2026-10-02 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cecc03c-fd6a-3e3c-ae6e-5b0c59a3dfa9 | -13.32924 | -43.86295 | 2026-10-02 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d55ec5bb-6c5b-3e36-b592-d6217c7d3087 | -9.51987 | -45.33062 | 2026-10-02 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ed55cd8-6b3e-3776-8e1c-9ee9c5c04a4b | -9.33347 | -47.25329 | 2026-10-02 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38109289-146b-3918-8384-dc362d89d475 | -14.34501 | -44.72929 | 2026-10-02 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bd5b6be-deec-3a00-b5d2-dceb25f82241 | -11.15137 | -44.60785 | 2026-10-02 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ec49a0d6-9ab5-3fdb-93d3-549ddb98d888 | -11.69687 | -43.60646 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README30.md)
