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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32bd7b60-a886-3e1d-aa45-86f264a4034e | -2.20588 | -46.61399 | 2025-12-18 03:46:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bd6902e3-4e0e-36ba-b6c8-002d245a7a8b | -5.6985 | -35.33692 | 2025-12-18 03:46:00 | NPP-375D | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68096a08-52e3-3c48-b074-7e4bcf1ec69f | -5.80278 | -35.47063 | 2025-12-18 03:46:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 176fbc21-b30e-3829-baf5-e44cc525cd5e | -6.06622 | -35.11081 | 2025-12-18 03:46:00 | NPP-375D | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b907ac67-0b56-31e3-b4c1-6a4693949b71 | -5.28615 | -38.07888 | 2025-12-18 03:46:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c146cee5-ac05-3955-a35b-c186d0a3d1f9 | -2.20864 | -46.59733 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cd072a88-7c9b-30d9-b2dd-0d16f1d1afe6 | -7.81534 | -35.24165 | 2025-12-18 03:46:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 22fbd91d-2664-3d98-a0d3-3b894982b1c1 | -2.19879 | -46.60854 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2a6e0e5c-efcb-3dd7-9163-83c1833a0659 | -5.41325 | -37.04964 | 2025-12-18 03:46:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8f1753ac-a561-3548-836a-9fd917800b35 | -7.87714 | -36.91355 | 2025-12-18 03:46:00 | NPP-375D | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b00b462b-ce9b-3ea6-bcd0-41fcfa50bfad | -2.20435 | -46.61535 | 2025-12-18 03:46:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 232e7d07-6c02-31f7-a777-83e213d8b8b0 | -6.81649 | -34.99146 | 2025-12-18 03:46:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f256b7dd-01d8-330e-8d17-08e104016c03 | -2.63717 | -45.67374 | 2025-12-18 03:46:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 97ec4e5e-65f5-33ce-b58a-3285964fbea2 | -5.41669 | -37.0502 | 2025-12-18 03:46:00 | NPP-375D | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 60b5adf6-5ee3-3218-a82c-1f7d930c3781 | -2.1978 | -46.61423 | 2025-12-18 03:46:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cdc6efc4-3539-3404-8243-7a4cab5ca0d4 | -2.21426 | -46.60403 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e053e3a5-17f1-3fb5-a813-9c41894c7fa7 | -7.46033 | -35.09272 | 2025-12-18 03:46:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac5d0d6c-d830-39cf-8054-98eb8ab010dc | -2.20682 | -46.60832 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cf735e77-2a1c-3ca6-bebb-920844efa3e2 | -7.84255 | -34.95937 | 2025-12-18 03:46:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff55d27a-98de-3f4a-8192-58e406c182bb | -2.20724 | -46.59866 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f7085448-3279-3c45-8d98-133274267b30 | -2.21184 | -46.61104 | 2025-12-18 03:46:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a436df3-fefe-3332-ae71-622dd633d64e | -2.25721 | -47.86547 | 2025-12-18 03:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 61c64402-33ce-38c9-90c7-a01ecb9c46d1 | -7.81147 | -35.2446 | 2025-12-18 03:46:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 396823ff-78e0-3f36-83ce-1b33d8825387 | -7.81866 | -35.24218 | 2025-12-18 03:46:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 79c92b6a-a53b-3348-9525-bc00a801677b | -7.81479 | -35.24513 | 2025-12-18 03:46:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b6814e2d-dab4-3639-bbb9-ccdd0badc07b | -2.20028 | -46.60709 | 2025-12-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 783ff482-d799-346e-b3ac-faeadf6ebc70 | -5.28683 | -38.07474 | 2025-12-18 03:46:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d9b85814-1b9e-3bf9-9328-79bca96a8740 | -9.29426 | -35.64822 | 2025-12-18 03:49:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c86e5b16-0fae-3d17-a41d-d919fed518b6 | -9.15569 | -41.06002 | 2025-12-18 03:49:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42cb9604-979d-335c-8969-32dfd1b49546 | -8.62203 | -35.16801 | 2025-12-18 03:49:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7f447fd7-0bad-30ca-a38f-9886b269254d | -9.27617 | -35.91395 | 2025-12-18 03:49:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 21a3b4fb-4ac0-3bb0-97da-66da730d3f53 | -10.0815 | -36.14731 | 2025-12-18 03:49:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 20d616c9-05d9-310b-8b3a-66dd7cedb850 | -9.81254 | -37.75805 | 2025-12-18 03:49:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c08c80d-9da1-3588-8d20-59878f442443 | -9.03046 | -35.64574 | 2025-12-18 03:49:00 | NPP-375D | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 07073de3-3158-3bfb-8c35-1f6e0146aaa9 | -11.1572 | -43.31628 | 2025-12-18 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 85cd7de3-2f44-3ece-820b-d9ad35ccb523 | -11.1518 | -43.32013 | 2025-12-18 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 30c81d6e-884d-3387-a3fc-c00c3da277ce | -9.15631 | -41.05642 | 2025-12-18 03:49:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc41f65d-f722-3858-aa72-389a30c96d32 | -8.95631 | -35.70861 | 2025-12-18 03:49:00 | NPP-375D | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bd99792e-58cb-31c1-babf-207db5a94103 | -8.95988 | -35.42609 | 2025-12-18 03:49:00 | NPP-375D | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 76f3db96-0f45-3618-9ce0-8a104dc1352b | -9.62417 | -35.72233 | 2025-12-18 03:49:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 68d35014-21dd-310f-b4b1-02e77c647e95 | -10.61958 | -37.13776 | 2025-12-18 03:49:00 | NPP-375D | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4b6bda93-19bc-37d3-9e2f-1793d3eb9282 | -10.62016 | -37.13419 | 2025-12-18 03:49:00 | NPP-375D | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f452afd6-6d4d-368f-af06-b10a6778bceb | -9.15975 | -41.06074 | 2025-12-18 03:49:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c22f76a-9ed8-35cc-acf5-de99f328e2e5 | -10.08095 | -36.15081 | 2025-12-18 03:49:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 227d49f1-cfea-382d-bbb5-e8b2078e9e77 | -9.16037 | -41.05713 | 2025-12-18 03:49:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ab8bdf9-5bdb-316f-8332-e4f4655adde8 | -9.35207 | -40.28723 | 2025-12-18 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ee60db30-a7aa-3802-8a7e-40f84f770e5d | -8.95963 | -35.70914 | 2025-12-18 03:49:00 | NPP-375D | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4398c43e-0dc8-36bd-a143-fade7c6c3ad7 | -8.34529 | -38.912 | 2025-12-18 03:49:00 | NPP-375D | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d2acff61-bee1-3779-9abb-b97fb3a3f550 | -10.08427 | -36.15135 | 2025-12-18 03:49:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| df7e9528-89f0-361e-86f9-b8657c464b01 | -9.96481 | -36.5382 | 2025-12-18 03:49:00 | NPP-375D | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 791d16cc-28a2-382f-b72d-3c7456aee4be | -10.08483 | -36.14785 | 2025-12-18 03:49:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5aa248c8-5c23-3dbb-91e2-f94219571bd7 | -8.62148 | -35.17152 | 2025-12-18 03:49:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 624ab2cb-c7ba-3ab4-9467-70102b5d7bd0 | -14.39089 | -43.97287 | 2025-12-18 03:51:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dc81788-93fd-3ec1-b494-a91cfa3f4470 | -17.02494 | -41.17232 | 2025-12-18 03:51:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0350a9dd-ca27-35ca-826c-e3a22b77044d | -14.39174 | -43.96825 | 2025-12-18 03:51:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90f79e6b-e7ca-3125-ab8f-7291b28cc199 | -16.79552 | -40.30657 | 2025-12-18 03:51:00 | NPP-375D | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bcb318e5-e8a0-3621-980e-758c795168d3 | -15.46255 | -39.15721 | 2025-12-18 03:51:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d061d8d1-e916-3e88-aec6-5c4ab298050c | -17.02857 | -41.17307 | 2025-12-18 03:51:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 893e06e7-bc5c-3ad9-8103-d74aa6fa07ba | -16.79484 | -40.31061 | 2025-12-18 03:51:00 | NPP-375D | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 32149cf1-98dd-3854-a1f7-46ad2072be63 | -14.39003 | -43.97747 | 2025-12-18 03:51:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15a19a9e-729b-372b-a7a4-af60e1fa0fcd | -23.60995 | -48.34798 | 2025-12-18 03:53:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ede53d-a83f-39a2-94f2-65546a5175a9 | -32.35674 | -52.37263 | 2025-12-18 03:53:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 62f8a66a-677f-3a98-8f23-52483139883a | -19.56521 | -50.99475 | 2025-12-18 03:53:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b5f87aa-b6cf-3e7c-ba34-492559debff8 | -27.56568 | -48.66126 | 2025-12-18 03:53:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 99beaf2f-00c4-3b5d-aa20-79021b68a0cc | -32.35582 | -52.3763 | 2025-12-18 03:53:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 91bac67b-d7f9-3b66-9682-249e3424af92 | -19.55891 | -50.99321 | 2025-12-18 03:53:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 443acee7-cdec-3ab2-99a2-6c92a11938bc | -32.36186 | -52.37441 | 2025-12-18 03:53:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 229bd496-2d62-3a18-8898-d003891cd57e | -32.35069 | -52.37452 | 2025-12-18 03:53:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| f3ed4d63-922e-3fb7-9ddd-b67d044b30f0 | -32.35161 | -52.37085 | 2025-12-18 03:53:00 | NPP-375D | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 85e33a79-d44e-3b04-897a-a9c45fa3d1fe | -0.8932 | -47.99998 | 2025-12-18 04:06:00 | NOAA-20 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 000c4a59-c90e-3e19-82cb-b4b03fcf0692 | -1.51661 | -47.36972 | 2025-12-18 04:06:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18daaa34-3a0c-38a8-aeaa-f1b785f6e64b | -0.89406 | -47.9947 | 2025-12-18 04:06:00 | NOAA-20 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f54756f9-0807-3cfb-8e45-8ba86084db69 | -1.7709 | -45.71071 | 2025-12-18 04:06:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a45ba121-e1cd-39a3-b36d-12385b45690b | -1.51735 | -47.36518 | 2025-12-18 04:06:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b9358ac-1654-346e-bff9-1a88d0536c53 | -1.68684 | -45.87156 | 2025-12-18 04:06:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 924234bb-5e96-3b16-9274-0201a4a9ebcc | -3.78627 | -47.74714 | 2025-12-18 04:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c09cc03f-6102-32fd-8ba6-7963959802e6 | -3.19051 | -50.23335 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4e3e5e4-a24b-3576-ac53-e9761224abc1 | -10.23919 | -38.94818 | 2025-12-18 04:08:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d15175d4-fb93-363a-9de3-5e677fed34fd | -2.20984 | -46.60398 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 34e8f8cb-1756-3d6b-bfcb-85faaae335fe | -4.05362 | -47.40914 | 2025-12-18 04:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 289ee702-5d01-379a-b281-07f4d6f39e6a | -10.08368 | -36.14673 | 2025-12-18 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 66066a99-1755-30e1-9b2a-0e1bd958a807 | -2.64842 | -51.73075 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25b0e94b-1f4d-3a5a-8776-faa896779e4f | -9.28733 | -40.46404 | 2025-12-18 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01f4b16d-8088-3768-984f-20d0be84416f | -1.40607 | -51.74386 | 2025-12-18 04:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02d74dd4-2d3a-3a00-a244-dbe785af6894 | -2.67605 | -51.67646 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e11d3c2d-1728-356f-916b-879e85040ca8 | -2.20194 | -46.59858 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f57a8e6-9007-39ae-b757-d30da2134ea9 | -1.61884 | -48.5556 | 2025-12-18 04:08:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fb4593f-9d3e-3eab-821f-eaa1694de1d1 | -2.66306 | -46.88942 | 2025-12-18 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 583e9a96-8f8d-37e1-bd10-0b0bf389e1fb | -2.115 | -45.35604 | 2025-12-18 04:08:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e67c6485-ac37-3224-a52b-84f62878a96b | -2.20622 | -46.59928 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 174af3b2-6b27-3533-bc0b-0b396b965873 | -2.92718 | -48.22578 | 2025-12-18 04:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55cc036f-14b7-3646-ac5d-15ca16e12d02 | -5.80281 | -35.46856 | 2025-12-18 04:08:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8550b4b-7137-3b40-9ea0-aa994dab22b8 | -2.64766 | -51.7352 | 2025-12-18 04:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4c25aeb1-2da7-3a2c-b8b1-0130d3461da4 | -1.62379 | -48.55637 | 2025-12-18 04:08:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73292adc-a612-3226-8a98-53f14f0c46bc | -7.78047 | -37.97567 | 2025-12-18 04:08:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef9263ce-09b8-351e-b665-d2817d19d526 | -5.07904 | -37.64913 | 2025-12-18 04:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 583cb292-852d-364c-a731-ea367ded2f49 | -2.20492 | -46.60727 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 313626c3-250f-34b2-ae11-fd546339bba9 | -2.21048 | -46.6 | 2025-12-18 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d818500b-d4c2-376a-9cda-1a8b45977afe | -2.66738 | -46.89018 | 2025-12-18 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f64af857-379d-30d2-9ec8-359e9f990dcf | -9.96605 | -36.53965 | 2025-12-18 04:08:00 | NOAA-20 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
