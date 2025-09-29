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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a769aa2d-c883-3208-884e-e5ad58a6dc81 | -11.42337 | -44.91373 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 796cafe1-690b-3e62-a895-0b0b7fc96123 | -6.83148 | -44.8251 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fdbf486a-b4b6-35f4-ae07-2c0eec609fce | -8.65159 | -43.98654 | 2025-09-29 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d3dbff8-155a-384e-9ea5-6f9fc4719e28 | -5.98369 | -42.35878 | 2025-09-29 03:47:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f01bb262-576d-3204-be94-f82cfbff49c5 | -15.27857 | -47.87638 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ca06016-0923-3a6a-b739-a9cef8acfde5 | -10.39649 | -48.15142 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4774cd91-1865-34a9-acfe-adcc7a768a81 | -8.2617 | -45.47493 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 250a2d84-b556-36ff-895d-dc42c7b52d42 | -8.73142 | -44.88551 | 2025-09-29 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab9f008a-bb08-3a54-bca6-1d76d45be622 | -11.7662 | -47.56051 | 2025-09-29 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 061a8584-5459-3012-889f-1cefde98f82e | -8.29721 | -45.46951 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 887c7e96-6ca4-3923-8e44-3d4833d37930 | -6.27941 | -42.49128 | 2025-09-29 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 742cab03-6790-306c-9abe-375c7d322f2e | -12.89567 | -45.21831 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ae4ff2d-5b3a-3431-a998-13cfa0280611 | -9.30773 | -45.72073 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8d66815-1490-3cde-849a-95171cd967d7 | -6.0574 | -42.47832 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4763bd3a-d23e-3527-8511-b0d5293c5328 | -15.53546 | -47.88061 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2356c47-00cf-321f-b903-219b8457d816 | -15.41448 | -48.23434 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8de0ab3c-fc54-3318-8203-dc56e6545117 | -6.58056 | -43.40723 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1e035e5d-3180-3973-868d-e7040369a457 | -9.05112 | -46.71513 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4104c1f2-7744-3ff6-990a-ae8a64825b52 | -11.98402 | -47.12298 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54c202f2-a329-3a1c-ba8a-99cc70f6722e | -10.81015 | -46.67843 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6048cc93-c512-3a6b-9753-00b39d77505d | -9.05198 | -46.71056 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d0786ea8-930e-35a2-9e17-7f8a4f988bbc | -15.90369 | -46.24145 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17d7c0ad-89b6-3284-bc25-65951381def4 | -11.92993 | -48.03752 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 673af2a1-4cf1-3e05-8488-18e7aeaa3a3e | -12.66475 | -46.91053 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2957a43a-e9e8-31c7-85b1-4c77e581e0c6 | -10.40165 | -48.1588 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c0fd515-25a3-316f-9588-61fa54865892 | -7.58859 | -44.78998 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 601e54b1-9cc9-30bd-ae3e-82106bdd7ab3 | -12.94569 | -45.17591 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb556277-78f0-3021-bf0a-cd8cb4a1e1c9 | -7.58612 | -44.78431 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7b0185f-bd52-3975-8e10-c1396e73c1d5 | -11.93191 | -48.0278 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6cc9cdf9-d1cc-33b3-a524-4a3d52b6b9b0 | -6.10995 | -41.82606 | 2025-09-29 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ab0fc743-5619-3515-9570-4b70986d9ece | -15.4692 | -47.93969 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d3a1d91-e168-3d1c-a51a-fc05b2eb49fd | -17.28448 | -42.70054 | 2025-09-29 03:47:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0c7a6fe-7bb7-38a9-a47b-187a87800cfe | -17.71885 | -46.72161 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd02f5a6-6cb1-3050-8533-2d78d063db22 | -11.79859 | -44.90564 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b99b55af-11b0-34c7-8bdc-a3724502bf95 | -8.73206 | -44.88196 | 2025-09-29 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd2a1032-56e0-34e9-b299-aaa108a76c2c | -6.12053 | -41.81857 | 2025-09-29 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ab8b0cf-6214-34ba-a613-9ab0cc830b9a | -15.32491 | -47.91246 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a3b0f69-9581-3a79-bba6-1a57f17e642f | -15.2727 | -48.76454 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e85ec521-9697-3087-a964-87726646ce1f | -11.3662 | -45.07817 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 68dbdf61-8399-3db4-b28e-3de1daa7c8d0 | -12.65676 | -46.92134 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c3ce972-60bf-3af9-93fd-95e3b18ab6f8 | -8.16743 | -46.39698 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cebf3781-2973-37d5-8773-acdebe194451 | -12.69678 | -46.9068 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0ebb29d-2438-3b88-955a-dd8b3ccf0e4d | -15.47751 | -47.92828 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea8e19df-ed3d-339f-9bf5-2e7eea1bb2ba | -7.85349 | -44.5901 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30ed4327-1b0b-322f-875d-0641c0063370 | -12.89287 | -45.21361 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d0adf4e-0668-3be6-9462-cfc889b4d40a | -11.51378 | -43.5451 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2e24784-7b84-338c-8dff-817ed190871f | -12.2764 | -44.12031 | 2025-09-29 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11b6b63c-26b6-33dc-8b5c-91a5e5bf6ecf | -15.70681 | -47.805 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb34b858-883e-31ef-a483-94781a6ef5bc | -6.06839 | -42.61145 | 2025-09-29 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2ab0c9c0-4ba8-3712-82fb-fa64876b5d26 | -11.41782 | -44.91531 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a23a028d-cb7e-3375-a94a-3718aed6f58f | -6.46803 | -44.01386 | 2025-09-29 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d95dd59-33a9-3e7e-8866-35cfb228aa58 | -15.61408 | -46.25632 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6aafe40e-6fe4-3306-8b4f-e717c76d589f | -7.87931 | -44.59835 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e90929d-c9ef-3e36-ab4b-2933e457d90e | -11.91934 | -44.75817 | 2025-09-29 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d14b953a-5ffa-3457-a2cb-19583bf4f21f | -16.5069 | -46.03316 | 2025-09-29 03:47:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df5230cb-6d21-3dbf-bb5e-0eef7ff65547 | -11.43358 | -44.95823 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 509bd3a4-b9e2-3bd1-ba00-df014013a59f | -7.86403 | -44.59224 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d12fb95-a6a5-3c93-943b-2d34f05f1e16 | -10.801 | -45.36438 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a85bee9c-1feb-3287-9450-d1df8b7c489e | -12.96291 | -45.1949 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85eda00b-1c53-3d6c-ab49-2bbaade53171 | -6.11472 | -47.18412 | 2025-09-29 03:47:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| f4aca8cc-8d94-3bfc-a708-018176868518 | -10.79703 | -46.68444 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13f45392-88eb-3e8d-ba5c-7cfd714c1c6e | -8.26874 | -45.49932 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 65a27e31-daf2-3afb-ab4f-405993c52531 | -6.91139 | -43.99902 | 2025-09-29 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46f8818f-1537-397b-bb11-2d46cc1830af | -11.40347 | -44.90767 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f100fd5-bb7d-37e2-afe7-08a7f31f7c87 | -12.58788 | -41.28432 | 2025-09-29 03:47:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| db55b2fe-ad15-3f79-a7b6-b7b10fcb4fbb | -7.58558 | -44.77559 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a49e36e-a16f-3b60-a63e-93e092739055 | -19.55979 | -44.21988 | 2025-09-29 03:47:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7822863c-fd0e-3a6e-bf59-ce6a915cce9e | -16.40551 | -47.03023 | 2025-09-29 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e42402f1-9145-3792-94b5-aac90a7f80a0 | -17.28549 | -42.6951 | 2025-09-29 03:47:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8582afae-2e99-39b0-9787-cd96726aefc9 | -11.66155 | -44.29091 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2aeb6448-3044-3185-9ea5-3ef85f6ec6cc | -15.27481 | -49.50611 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8da98f7f-7aba-381f-8bae-795215d6e977 | -10.48431 | -49.37351 | 2025-09-29 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4571b887-e163-366e-9a1e-0ab697a20108 | -8.71805 | -50.05229 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8664cab0-aeb7-3634-ae95-507f6551e8d3 | -8.30334 | -45.49906 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d852410f-e5d8-3106-bdf6-dce23ea7bb68 | -10.47864 | -49.36855 | 2025-09-29 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7e5822a-2e8c-368d-a141-1bf2adfef1b4 | -15.55417 | -47.8764 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a79746a2-b129-3742-b732-cd0878e81bc1 | -11.36508 | -45.08412 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af0553dd-4267-3622-840b-0b8896c68466 | -9.77953 | -46.94238 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d10e8ba8-f97b-3e0c-8967-e2d79323f9b7 | -17.71499 | -46.68894 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c7a21ac-5e92-392f-a846-fcbf98e73524 | -10.80359 | -46.68148 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7773abac-5496-36bc-9532-4cfcb2f73c41 | -7.58911 | -44.79832 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 335c493a-2f7e-3bd7-a352-65539becde0a | -6.25685 | -43.6498 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2a09c82-d7d0-39e0-9086-2d93e9c45ada | -5.90842 | -45.8531 | 2025-09-29 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 569b04ef-c206-3234-8e81-a96638242161 | -7.21717 | -44.78654 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fa1f02d2-861a-3232-86aa-be38916b44c4 | -12.00644 | -46.61566 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a88b491-ef2d-3eb1-b00c-2f949a7fb13d | -8.30401 | -45.49538 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cafc0b6c-8e94-3876-9693-f4b616aa95ef | -11.48236 | -43.51709 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c9b2b6f-5592-3d49-8e53-8d8a97d95015 | -15.91365 | -46.218 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ea3515c-7e87-35df-8cda-6c25e8bcac17 | -15.61917 | -46.25764 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0a6013e-222f-3cb8-85a0-1e15a68d6d01 | -11.50623 | -44.85245 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| baa38770-4daf-3b1c-bf68-1c0c8f7ef843 | -12.16547 | -47.77581 | 2025-09-29 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd555809-d69e-3f2f-b995-7c22b204d111 | -11.9974 | -47.11043 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c69ff62-4810-3707-8e9b-b4087e6329b7 | -11.97819 | -46.58195 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61e0424f-c87a-37cc-b650-6a76d328485c | -15.21426 | -50.10361 | 2025-09-29 03:47:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b823f2d-23d7-37f9-93f2-1e9951ac89d7 | -8.66024 | -49.4308 | 2025-09-29 03:47:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d27c988c-45f3-32cd-bb5e-9a4c2e4a8f55 | -6.11185 | -43.45542 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46ec3abf-bcc4-36cc-83cd-4f8337f89225 | -15.3429 | -47.91219 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7a14ea0-fa05-3229-8400-b6413adc557a | -6.42832 | -43.51171 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b216f8fb-8845-3abc-a1ec-43bdbcc5683e | -12.27736 | -44.11514 | 2025-09-29 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3c8965e-a86a-3bee-85a5-5994a6810785 | -7.58916 | -44.78677 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
