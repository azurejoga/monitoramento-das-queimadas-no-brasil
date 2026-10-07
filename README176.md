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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df548548-59b1-3371-b2f9-32f2b5457b36 | -11.84652 | -47.37766 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6a2b5f96-5f8b-303d-8fe4-4b464febf8d2 | -15.10766 | -48.50736 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8661ab45-e9ad-3b42-b4e4-3fc6416ed731 | -12.43026 | -40.11652 | 2026-10-07 16:35:00 | NPP-375 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 4b558bda-0ac5-3bf6-8cd0-04cbad5dc0ca | -11.78044 | -46.7766 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 33283e98-f988-3afe-b0a2-ea43a33db5c4 | -12.40196 | -39.08318 | 2026-10-07 16:35:00 | NPP-375 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 61e9792d-909a-35a1-b08d-64d136c1f852 | -12.16355 | -44.73755 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 13441e4d-8ebd-340b-b135-962345944b66 | -13.68545 | -49.10459 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 837df828-73c9-31ae-a891-cd5bfda967aa | -11.37163 | -39.89664 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOSÉ DO JACUÍPE | BAHIA | Brasil | 2929370 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 08eaf0c6-3aa1-3b6f-a445-3e0a842a1cb5 | -14.90775 | -44.31597 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 551da132-7075-3bf4-aeb9-72eec50c6ff3 | -11.8457 | -47.37093 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3c682a4b-33be-3387-b89d-450c770f90e1 | -12.9898 | -47.06286 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8ecb31ad-b663-33f2-b4f5-fe88313a3de2 | -11.64261 | -43.68599 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| cb5ab30e-4d96-3761-b98b-b1e413cf259f | -11.2361 | -44.87326 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2437a6f0-da0d-359c-b93f-74544bd12775 | -11.62768 | -43.64542 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 203e52fb-46b7-33e3-81bd-b1b95a405c88 | -12.19895 | -48.42006 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| f9720bf6-9663-3de0-bab2-66c10d1440f2 | -14.53621 | -44.03418 | 2026-10-07 16:35:00 | NPP-375 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8e9a7e1b-67ff-3de2-9ab5-cc77c883f204 | -11.35759 | -40.00065 | 2026-10-07 16:35:00 | NPP-375 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 33b07635-7ecc-3bb3-bc5d-5d91d733439e | -14.04767 | -49.17891 | 2026-10-07 16:35:00 | NPP-375 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5cb1bb83-9274-3732-8618-342abeb74961 | -17.42037 | -39.81675 | 2026-10-07 16:35:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 07e90add-70c2-34da-939b-bc5f3f453987 | -17.41696 | -39.81735 | 2026-10-07 16:35:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 23a040b0-a4a6-33db-a8c4-45b25137c1b3 | -12.18064 | -44.75825 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 901d2da7-dadb-362d-816c-dde30bf11a86 | -12.21985 | -44.69027 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 46a88279-aa2b-39f5-9a61-028686ad35f7 | -20.31 | -41.77763 | 2026-10-07 16:35:00 | NPP-375 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d7bc4b38-9d82-3935-a061-b92c12a733df | -11.22828 | -45.28051 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 5ee1545e-77dd-3aaf-a2a5-a1828fb669e2 | -12.22372 | -44.74017 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 9dc988ae-e5d6-3c67-b548-b260ee4d7103 | -17.14977 | -40.80595 | 2026-10-07 16:35:00 | NPP-375 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 530e5f95-7bb7-3a90-ac14-0db4585e2eb4 | -13.78478 | -39.42295 | 2026-10-07 16:35:00 | NPP-375 | PIRAÍ DO NORTE | BAHIA | Brasil | 2924678 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 27cb8e0f-6ed8-3304-b4ae-537507c46e19 | -12.99094 | -47.07048 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| e1f75c43-430d-3f23-8c5b-941572136140 | -11.22623 | -45.27287 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6c2d7529-e092-36a4-aee0-508af008daf0 | -11.71117 | -43.42117 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 647cf4f3-5087-3339-95a1-f576ab1584eb | -12.17265 | -44.75169 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| e09a8dee-21b8-32a9-ba78-1b98ec40d951 | -14.199 | -40.27111 | 2026-10-07 16:35:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f4d20d31-7998-39f4-ac2c-68e197682c7a | -17.55496 | -44.70218 | 2026-10-07 16:35:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef87c252-24e4-3402-8c59-871fd0dc099f | -11.2268 | -45.27672 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b6bbe311-e7bd-3c12-8ac5-1ed7e561fae8 | -11.23287 | -45.28772 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| ae3f1119-fefa-35fe-8c00-2a6af41ecaac | -12.23219 | -44.73487 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b2c28b64-1a28-3d30-aa35-46ee57ab7b91 | -11.23101 | -44.86249 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4b4a6d30-9c37-33db-9f0b-1a4785e6a005 | -11.47496 | -43.39754 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 658f7805-c6c9-3241-8504-0561a5443dc5 | -12.22204 | -44.72878 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 82265b3b-659d-353b-8212-7c7ad42a6ece | -10.59027 | -36.69601 | 2026-10-07 16:35:00 | NPP-375 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4ce94bf0-b44c-3639-8167-2e1274d95657 | -13.69347 | -49.10686 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 51dbf9f0-f086-3440-b517-cbb043efc2a7 | -14.15553 | -42.18388 | 2026-10-07 16:35:00 | NPP-375 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 06bdc764-afe2-36ac-a97b-a243614c3fbb | -13.67888 | -48.80006 | 2026-10-07 16:35:00 | NPP-375 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3b2a4b0c-8da9-380b-b252-c71525643010 | -12.99437 | -47.06733 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 514e867f-3d1d-3873-b94d-44b2176988b4 | -14.41069 | -41.34126 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 2c19a715-f4a8-366d-9b5e-bda98b58dacc | -13.32859 | -38.97804 | 2026-10-07 16:35:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9260da85-7392-3b08-93d9-92429de4c8e7 | -13.33668 | -38.98117 | 2026-10-07 16:35:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| c482d8ee-8357-3a88-aed7-33d1f4f93921 | -11.7145 | -43.42065 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 43376683-3c73-3142-915d-67e54ac6f19e | -10.92701 | -41.38963 | 2026-10-07 16:35:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0e7e81ac-cd38-3812-bd83-cacbaa4f6ded | -11.22995 | -45.29213 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 40fbb065-d728-3748-bb08-6ce591963d70 | -10.68309 | -41.21618 | 2026-10-07 16:35:00 | NPP-375 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c9b5e084-ea79-38f3-8f04-42fb549afd99 | -13.32124 | -38.97932 | 2026-10-07 16:35:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| aa60394b-3da9-397e-ab56-0ab57651efc9 | -16.8591 | -40.58859 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 10c4a908-fc20-330a-8d81-58197f0f0430 | -11.85663 | -43.55755 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.4 |
| d168d2e6-0170-3493-9f47-56eea124c406 | -17.74585 | -42.59452 | 2026-10-07 16:35:00 | NPP-375 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| d058eaff-21c3-36e9-b76f-507ca875d2ca | -11.46004 | -43.38902 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 3b2cb4aa-5f16-3b92-8721-133cfcf4b16a | -11.83452 | -47.34701 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d532b00c-89de-3934-848a-c12de5b0a154 | -13.27428 | -44.00174 | 2026-10-07 16:35:00 | NPP-375 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c151940-3eb1-30a9-a6c1-0bff7d925854 | -17.01767 | -41.03815 | 2026-10-07 16:35:00 | NPP-375 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 74e57ea9-a610-35d8-b694-17b43aa4e6cd | -17.49853 | -39.31249 | 2026-10-07 16:35:00 | NPP-375 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b3831820-f257-3a37-ae0a-5871e8948370 | -14.58668 | -42.41926 | 2026-10-07 16:35:00 | NPP-375 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7ed6d25a-a9cc-33dc-9ac6-76a2c7911288 | -12.18697 | -44.75341 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b309e9f3-29c1-394d-bd81-8950552d2ad8 | -11.22851 | -45.28832 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b4257f99-876c-3348-b098-b44c92072139 | -12.99827 | -47.06681 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 22491355-c973-31d1-af5a-10c1c4e4b3df | -12.18864 | -44.76484 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 6e22e9e9-1bd1-3e10-80d4-e2795167e15c | -12.18176 | -44.76587 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 70524322-d9c8-3580-977e-f9aecc9c6f40 | -18.33694 | -42.24139 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fc02a2b8-6bf1-38e6-9545-2028fdbef4d6 | -12.18809 | -44.76102 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 8f0af638-aa93-3a83-baae-21338fe6bbf2 | -11.77398 | -46.70201 | 2026-10-07 16:35:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c9bf380e-912a-3c44-bf0c-d95a6162977c | -12.1681 | -44.74462 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| b6e563f5-70fd-3035-ab1c-2e09dea14dad | -13.11197 | -48.99844 | 2026-10-07 16:35:00 | NPP-375 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b7c6cdab-014b-3705-9319-406823d3b0fe | -12.22522 | -42.11805 | 2026-10-07 16:35:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f098f4a9-e1de-3d56-a0a6-a022b8a83f5e | -14.35248 | -41.27659 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 4fb68caf-410f-3b40-bf4a-b236f35d8a8d | -12.21922 | -44.70978 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f1bfa811-7637-3264-8a1d-868087fe0006 | -11.85029 | -47.37539 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ae211f32-d5bd-3ddb-b39e-2050d74e85d7 | -11.84382 | -43.56324 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 9335b9f7-7030-3a73-9db9-bb007b13daa4 | -13.69387 | -49.09871 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 9f6fdff1-d6a0-3821-86e4-5c7772fbce46 | -11.23388 | -44.85819 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2028b70c-f261-3e3f-862b-ab52828ec2ae | -11.83697 | -47.30607 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| afb913fc-b8b3-3f77-9f2d-a5b4abeeebf6 | -13.19006 | -47.8837 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8404bc0c-bb98-3ee9-886c-8715012dd100 | -13.94944 | -48.78648 | 2026-10-07 16:35:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 35f9d6ce-31ba-386e-9b81-b185e9974624 | -19.06942 | -42.93515 | 2026-10-07 16:35:00 | NPP-375 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c1afd429-f694-3ded-be83-9a5511f92da3 | -12.22585 | -44.73974 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 0af57104-cd6d-304e-b437-3db7917e2051 | -12.04356 | -43.38564 | 2026-10-07 16:35:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9d847d2c-717a-3ac2-8d94-d54cee9bd623 | -12.22266 | -44.70926 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ccec6a22-76ee-3f28-8ccb-0e21114f12be | -12.1812 | -44.76206 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3a1e7503-f5d8-3ae7-8079-bb3ea838b00a | -12.16477 | -44.72181 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bfc75e48-7414-3c79-8ce9-ba2f6f2895e7 | -11.84111 | -47.36644 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 79157241-1dd6-30c9-b80f-79ab9a53387a | -11.23555 | -44.86948 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 065128fa-bdf3-3009-8815-25055a9aeb84 | -10.85147 | -42.81028 | 2026-10-07 16:35:00 | NPP-375 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| aab815d5-527c-304d-9542-14bfcc2f02cb | -15.16301 | -47.91385 | 2026-10-07 16:35:00 | NPP-375 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce013e16-3431-33f0-ba27-485d291316e6 | -12.19032 | -44.77628 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 980f6e0c-062b-38fa-bb5b-f916b48eceb7 | -12.22366 | -44.72451 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b7c8c4c4-2503-32de-8207-9f6835422c53 | -12.20395 | -44.654 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| af27296b-bfe6-32bf-a918-36328087b95f | -13.33374 | -38.9862 | 2026-10-07 16:35:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 52.5 |
| 8d8bdd06-05f0-3fb9-9d1d-1895f10e7270 | -12.17154 | -44.74409 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| b77b86cc-42d2-3e41-8373-078b8a8e2f9e | -16.85239 | -40.58977 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 6ddb56f7-f616-32de-8c0a-d2ead942f7ef | -11.69339 | -43.66 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| bee1b333-cf6a-3ae6-90a4-ce230ac3da16 | -17.98869 | -43.92376 | 2026-10-07 16:35:00 | NPP-375 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1dbdfe41-838f-3a6b-8fdf-86de98ded454 | -13.89096 | -49.12072 | 2026-10-07 16:35:00 | NPP-375 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |


[Clique aqui para ver as próximas entradas](README177.md)
