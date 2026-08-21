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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e85f6e2-8236-3135-a36a-cb34a3b6e756 | -13.38505 | -54.36951 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| dc6925d4-73a7-3346-b71d-4d10ad950545 | -13.43971 | -43.83854 | 2026-08-21 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b622f10-adfd-3cc7-ad44-7cbc3c93de69 | -18.11531 | -43.73746 | 2026-08-21 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71736ead-c18f-3644-910b-9c619678cb8b | -13.16051 | -42.41605 | 2026-08-21 04:49:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1736a4d9-47bc-3e66-835e-a206627a2408 | -11.19543 | -54.00426 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 043ede48-3c2d-3f3c-9953-239e3a1936dc | -11.18499 | -54.02546 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9eae591-5fb4-3ad7-8bf7-c01face37b02 | -11.1664 | -54.01089 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1b32a678-63d2-3e06-bddf-47fcd18a3943 | -14.4568 | -45.62014 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45a66c23-d878-3c86-8988-7888b2b72b44 | -11.19779 | -55.05095 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb385c22-fee8-3628-be87-4dd7a3a0617d | -15.00374 | -52.68367 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61d9a9aa-66ee-375d-892b-1ca20c735755 | -12.15861 | -57.2177 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f2f938d-f8ed-3545-b912-888c9de03432 | -14.46553 | -45.62642 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80e0ce49-3f27-39a3-bcbb-e43fa48c82c3 | -15.70899 | -47.79907 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4de8edba-d785-3279-827e-460b594dae66 | -16.73199 | -49.26816 | 2026-08-21 04:49:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caa01421-fad3-3a29-bd49-996e115fe8ff | -15.6809 | -56.25714 | 2026-08-21 04:49:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3720b647-34e8-3c35-a300-5bff685bd909 | -14.22871 | -51.9302 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4078cca9-b7f8-304f-8f8e-8848dd05a195 | -14.09507 | -58.85881 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 861298ca-bba9-3f5a-b70d-00c61e766b82 | -14.02376 | -58.86629 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21205fba-1953-35cd-beea-e0757c94dc34 | -13.24771 | -51.63932 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b4b7d79-9a56-30c3-8fbd-0ae9e3671b82 | -12.92728 | -56.62815 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f71f5227-d0fc-32f7-9f5a-54b8720a900b | -13.44682 | -51.7815 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a98dcadb-815c-32f1-aa47-b97f19d6732b | -12.26223 | -43.16742 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5eb34002-b868-37d3-b883-e4ae1e1ed974 | -15.35579 | -53.73716 | 2026-08-21 04:49:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 81e80b54-67ff-3bf7-b90b-b545af502553 | -13.24492 | -51.63515 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 356a426c-2216-335d-8cea-0b9324bff3f8 | -14.06956 | -58.87897 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b1efc06-acbe-3e30-8c63-feb72db5f356 | -15.71309 | -47.79979 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 213e35f7-6d4f-374b-ad5c-449d88c091c4 | -12.00652 | -53.43048 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8538c936-8807-3e70-86e6-bc22b71c8321 | -12.71649 | -44.49256 | 2026-08-21 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6130e4e-54c6-354d-9f5c-aec2752d4fd1 | -14.56845 | -52.99207 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f130d30-2688-3059-a86e-b62cafaa557d | -14.24472 | -52.13942 | 2026-08-21 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54bec480-4005-3f23-86fc-dd193561e54f | -11.18462 | -54.0063 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c29802de-0200-3fc0-be26-7e00f6ffa0cc | -11.18802 | -54.00686 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43fceb8d-b806-32d3-be71-7f4f03948724 | -14.24085 | -52.14248 | 2026-08-21 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f23d001e-7dde-359b-a124-6ac9c2885ee8 | -12.51303 | -54.75727 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bde5a056-671b-362f-ae8b-811c34fcc851 | -14.43699 | -51.81504 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b763c9f-2f51-3abe-b794-d615c11d2e55 | -12.38403 | -46.44736 | 2026-08-21 04:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 091b3caf-917e-3d1f-a443-86d146a099dc | -18.12093 | -43.73743 | 2026-08-21 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 692e6751-3d6d-36c7-9fc0-3e7d9b419415 | -11.1822 | -54.02116 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfcb2726-38d7-381a-a318-6618abb35402 | -12.50548 | -54.76001 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad2978f4-a8a9-3b52-887a-722469470481 | -10.38371 | -61.20641 | 2026-08-21 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a114608-5932-3dc6-a68f-1831e5d8989c | -13.43575 | -51.80923 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ae33298-b9ee-3b29-bc86-84f59f407b8e | -12.74399 | -48.48145 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f880e485-2eca-35e1-8729-b7c5a1abe317 | -11.20824 | -55.05176 | 2026-08-21 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20a09ec7-923b-3729-ab84-c71a1f483983 | -13.4026 | -54.36859 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d0636d7c-5a72-3e53-978a-6e1aeeb5123e | -13.93783 | -53.86089 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fd28f6e-676f-3033-b672-241ffb5fd90b | -13.40998 | -54.36602 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 191c2abf-7ff5-3ad1-8075-94a340953d48 | -15.19433 | -47.67797 | 2026-08-21 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c8d2283-a035-35be-93fc-05b0758b994d | -15.71821 | -47.79261 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acf7282e-a184-3163-a8d8-8d7ebf96fae7 | -11.18742 | -54.01057 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcefaf12-8110-3f11-ba5f-7a69254981c5 | -13.57661 | -51.64267 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa3a1275-5cdd-35f5-8de6-55e24d327923 | -13.94785 | -53.86253 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d71c2ef-f5f6-3189-b3e9-4fa3aba3e30e | -14.72143 | -47.14356 | 2026-08-21 04:49:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbf5887c-85c3-3b7b-9aaa-72af1e3e09d1 | -13.38938 | -54.38552 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c8dafecd-4939-3571-9d3f-56815ef50812 | -13.25604 | -51.62959 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9572788-cbdd-3d25-9e26-73435c081663 | -17.93357 | -44.40174 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bddc528d-9b2b-3d57-9b11-e157c3d57544 | -15.49608 | -53.90424 | 2026-08-21 04:49:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b169d3ba-ecf2-3021-9341-3abfc7c06f33 | -12.84705 | -48.43646 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b899457-b58f-3c50-a55a-af387eea616b | -10.38773 | -61.21407 | 2026-08-21 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 156e2629-7d7a-32d8-bbbd-18db6e511fd5 | -13.24437 | -51.63877 | 2026-08-21 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43e5a418-9d85-371a-9b65-c537f5cd2066 | -14.0283 | -58.86792 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b16fddad-25a0-3981-b1f0-3dc0fc366c93 | -12.52277 | -54.76285 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a763e9c6-0852-33d5-a915-4989ceb6cedb | -11.81531 | -56.60471 | 2026-08-21 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0983afa-ca80-3476-92c0-53d08cf72bc0 | -13.45793 | -51.77591 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b47c9ad9-bc01-3e47-a074-82ae03ee2904 | -10.38896 | -61.20749 | 2026-08-21 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de406e86-9ed4-3662-9d04-c758986a0145 | -17.33279 | -43.62765 | 2026-08-21 04:49:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cea8de4-b224-3527-827f-4ec416fb18bc | -12.86367 | -48.4288 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d53585eb-e4b0-3822-a347-06d907e1ec25 | -16.05293 | -52.17053 | 2026-08-21 04:49:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edf8fe1f-bb62-3630-8ce3-bbd4a65f8fca | -14.31784 | -51.90025 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06a16f7f-e1c9-3ecb-9530-0127cbc02056 | -12.50612 | -54.75615 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30997e76-9d55-3fc9-a04b-b8016a53bc9d | -12.84394 | -48.43093 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 399948a6-6962-3d9b-85ff-e4eddda9a07d | -11.20619 | -55.06394 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e367557-6f64-3fd6-8ba6-0981d6d592d2 | -12.12426 | -57.20874 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb910076-414d-3f94-88ef-ff8ac6733bb7 | -15.54363 | -53.96746 | 2026-08-21 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d399b31f-80a4-3654-9d61-9bcb95babe0c | -15.20211 | -52.80763 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8fa2f39-11f8-3924-a506-0b7f8776e895 | -13.38209 | -54.38091 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| c982d445-5ce4-3273-9653-107dd48e2688 | -11.20048 | -55.0546 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90e3d83c-435d-3a87-9577-b9e890252078 | -15.06439 | -48.7063 | 2026-08-21 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0860b59-5dda-3c3d-8a99-fef5895d1b51 | -12.49921 | -54.75501 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2c3567a6-f7e1-3f6a-aeef-0a91002f6d79 | -12.77738 | -48.40676 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ef7e202-4cb0-3971-a25c-482a5d526e63 | -12.53721 | -54.76136 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a06cf3d8-c523-38c1-9496-cd97b7c4ce75 | -16.72572 | -47.69396 | 2026-08-21 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb337f45-f946-3305-9d15-442df774703b | -14.45336 | -45.60943 | 2026-08-21 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5119450b-6fcc-3335-8767-19a972430074 | -14.43932 | -51.81493 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c36045e-ceff-3783-884d-ee407648fac0 | -12.85017 | -48.44183 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e7cc082-ff51-36da-96c0-27bd91091381 | -11.82793 | -58.83359 | 2026-08-21 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cbcb407-4dbb-3d59-bbed-5e55236af3ca | -18.02896 | -44.60514 | 2026-08-21 04:49:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d2f80f2-637a-31ad-b6f8-a896ecdbdd3c | -13.38844 | -54.37006 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9063c9bc-aa88-3415-9f12-c5445e6e9609 | -11.1794 | -54.01688 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93a99c76-f3ab-3a02-97ae-f504061083c2 | -12.75226 | -48.47778 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce18c520-f7e9-3c4e-ba4e-3b342ea58988 | -13.43296 | -51.8051 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40097809-7864-39c9-89aa-0cceee579fe3 | -13.38722 | -54.3775 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 96672b87-89a4-3232-a513-b8ae04d92da5 | -12.49575 | -54.75443 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 355fd59b-ccd2-35d3-a77f-f543895431fc | -13.93173 | -53.85619 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ce4597bd-6d8c-38a0-9396-8cf28321cdd6 | -13.38444 | -54.37322 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6ab0900e-deae-3d2e-96b3-475042af2f3a | -12.52058 | -54.75456 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3345ccf3-251d-373b-ab7a-ae753aaf2f4f | -14.10497 | -58.85238 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 809aba7b-32f1-3ef3-896c-346096a41811 | -13.443 | -51.82883 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ec69473-0383-3c01-afa5-79a8e4a316c0 | -12.25983 | -43.16979 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e37db2a1-dbb4-3f4c-9d38-f201227f83c7 | -17.33316 | -43.62402 | 2026-08-21 04:49:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68219ec9-1c0b-3ca9-bc57-c15c32bbfa89 | -15.4939 | -53.89648 | 2026-08-21 04:49:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README48.md)
