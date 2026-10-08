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

## Dados Diários - Página 231

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fda7360-f257-3d06-9f54-67af6f58e80a | -14.66645 | -42.48349 | 2026-10-08 15:39:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| b5435762-2461-3293-a37c-66ce54a21b6a | -15.62939 | -40.12965 | 2026-10-08 15:39:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 17baacc2-c175-3af3-b7ae-44b1a4fbfa04 | -16.34848 | -44.7167 | 2026-10-08 15:39:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0d280564-1e2a-306c-acbd-008cb0ae504d | -11.59482 | -43.66999 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 0a03aeac-d6e4-3748-9214-74a8a4239904 | -13.29714 | -41.50684 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 192451fb-0937-3d77-911e-5eda78f04a89 | -14.41898 | -41.51763 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 631c0b68-c551-3228-9dbd-30ede9bf149f | -14.49778 | -40.82312 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| cd916846-2bf1-3e27-baf4-31b9a9a4d675 | -11.77713 | -45.56539 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 565ea746-7eec-3d38-8222-f10690917bad | -14.89552 | -39.72354 | 2026-10-08 15:39:00 | NOAA-21 | FLORESTA AZUL | BAHIA | Brasil | 2911006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| aaec016f-51ee-30e7-ba4c-ce7cf59b49ae | -14.08433 | -43.77274 | 2026-10-08 15:39:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 767eea85-b940-3d03-b863-f2b9479701c3 | -11.76208 | -45.49034 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 51aff5c2-8b7f-366b-9b42-23312c2b3739 | -16.15435 | -43.11784 | 2026-10-08 15:39:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 954c6798-1d72-3942-b2d5-0987d5a56e8f | -12.55656 | -38.29945 | 2026-10-08 15:39:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2051d2cb-52dc-3dd4-b127-7cd9fb11c80d | -14.56733 | -41.53762 | 2026-10-08 15:39:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b741f97c-7d1d-3087-a8e3-f5137d0394e0 | -18.27645 | -42.6245 | 2026-10-08 15:39:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5bd2ee5f-470e-3d7d-bed7-41c9dd5a9d15 | -11.61793 | -43.65294 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ea9b9c6d-feb0-3e73-8c96-2dafc0964c1a | -13.89965 | -43.76252 | 2026-10-08 15:39:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd7b3807-21b7-360f-a601-8a617637c73e | -14.24519 | -44.43482 | 2026-10-08 15:39:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1b6586ca-fac5-3c42-ac24-538b4962264e | -11.61541 | -43.63661 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 746d571d-e400-3e29-ae95-214d76181c31 | -14.46693 | -40.73058 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 348.8 |
| 03b0ddfa-1807-3d3e-a675-67229c3b6850 | -18.29111 | -42.23911 | 2026-10-08 15:39:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 6e6c4536-bcf7-329f-a38c-58fdd1883ee3 | -12.03493 | -43.43467 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 608ed7cb-9813-397f-a9de-2e11b2697e92 | -13.29875 | -41.52098 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 6bd32c02-7194-3a78-be21-626ea8a71535 | -13.58725 | -40.73993 | 2026-10-08 15:39:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 83e18aaa-2d74-3cda-907c-b8e82ce3523f | -14.66866 | -40.49788 | 2026-10-08 15:39:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0089b0ff-724c-3f50-a033-4c73f3575385 | -11.77222 | -45.585 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 74521cff-ae5b-3a45-9844-b20938597a57 | -14.26224 | -42.44104 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 148.2 |
| 70da330c-8ba3-300a-9c87-93e4c34443dd | -12.23961 | -44.73857 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 98c1b665-857e-3c89-bd89-ecb832a34b0e | -11.85419 | -43.54399 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| a62232cb-60bc-3896-8335-828c2172b6ae | -16.4558 | -41.26115 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 92b04d82-661c-375f-81bd-72377b32d870 | -12.13336 | -43.32032 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f839659f-210f-3d00-a638-f4756f484225 | -12.15894 | -44.72031 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| a7773ded-34d1-3020-8819-6b42117e5e8d | -16.05125 | -40.64803 | 2026-10-08 15:39:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| d141c374-2283-3f02-b765-a289e4f37edd | -11.64163 | -43.7017 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 96175b1f-64d8-3f01-bafb-da812fcc466b | -15.53993 | -43.17521 | 2026-10-08 15:39:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 52dabced-f9c6-3e45-a1c1-9ccaf7384188 | -17.33802 | -41.3896 | 2026-10-08 15:39:00 | NOAA-21 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8289ba77-6bb3-34fd-992a-a7ffa1ad41a0 | -14.31974 | -40.26294 | 2026-10-08 15:39:00 | NOAA-21 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 947b8f26-c0df-345f-a802-ddfa9c262602 | -13.33777 | -40.2754 | 2026-10-08 15:39:00 | NOAA-21 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3827afee-77bd-38c8-a28a-5227b99078e9 | -13.29792 | -41.51696 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 72d12f8c-7f43-34c0-bae8-afc8d405dff6 | -11.62351 | -43.69964 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| dffa55ea-af82-3333-87d6-6c5f5e4049c3 | -13.29794 | -41.51382 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| e00e6eed-9a27-37cd-a119-2cc19a218869 | -12.1615 | -42.04219 | 2026-10-08 15:39:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 49ba14c0-2d22-3f45-8c4f-90b16c80ceda | -13.67787 | -41.01492 | 2026-10-08 15:39:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4f11933f-72a6-3977-87eb-79cf5b5ac8f3 | -14.73525 | -40.29456 | 2026-10-08 15:39:00 | NOAA-21 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 7bb2f0cf-e9b0-37d2-b842-75afba80f0cf | -11.44974 | -43.39186 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 9b789971-4120-3803-a365-0b7d4cbd843f | -14.73451 | -40.28842 | 2026-10-08 15:39:00 | NOAA-21 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 79f8bee4-202d-3a4d-99b9-543187df8937 | -12.19125 | -44.82568 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| cb35f692-e158-3a5b-a017-c3cbb10bd2fd | -16.7824 | -40.92886 | 2026-10-08 15:39:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 4276ef5a-4d5e-32d0-bec5-dd3e7bc2e566 | -17.69135 | -39.16909 | 2026-10-08 15:39:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 1f3729bc-cfbf-36d8-8ec6-7827de267792 | -11.78477 | -43.53652 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 107c3d67-61d5-35e6-acda-d6b8faf3fd21 | -12.2841 | -38.96188 | 2026-10-08 15:39:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3770a53e-ee7f-3226-8c7b-ed8e3b1b365f | -17.16685 | -41.56102 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| bd21013a-3110-314c-bdd6-3d0be2e59bee | -11.6119 | -43.66124 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b4fdd332-c8bb-3454-8778-23630ca90ff0 | -11.46136 | -43.38588 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 25dc1d63-2230-3326-8b46-45c409bd3cfa | -12.18548 | -44.65868 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 4fae33b4-fb98-3e70-a365-5865a553e12a | -16.45872 | -41.25656 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 8cb45363-2dad-32b5-a2c2-4bb8339997ff | -11.64351 | -43.70866 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 7e16eb9a-4afc-3f98-bc00-b5456e3f7051 | -13.29754 | -41.51031 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 6e2d4f74-f4e6-3b29-be3d-aa285ff1cc3f | -15.88079 | -40.78093 | 2026-10-08 15:39:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9506f0dc-7b4c-30e3-adf9-fa8edf16be1f | -11.83405 | -43.5305 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f026974e-6ba3-350d-8989-0cd53fc268a4 | -11.62957 | -43.59333 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 61b93f27-13f9-3fdf-9342-daaa0732b846 | -12.0906 | -38.75725 | 2026-10-08 15:39:00 | NOAA-21 | IRARÁ | BAHIA | Brasil | 2914505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 0e5c0ce5-6ac4-34ce-b4c8-94ae59fd970d | -11.60922 | -43.63728 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 4d5cd931-e53f-3f4f-9284-636c8ce0efaa | -13.96374 | -44.8454 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 42a49d54-6479-3d8e-9110-a1ae2b6a08c1 | -11.62506 | -43.61104 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| aa28170a-4e5c-3486-8b9a-25b656eb92ca | -12.04084 | -43.43427 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 22839a2f-b979-3209-9e4f-3d30d8f297ca | -17.10468 | -41.35072 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 0b2bc615-a08f-33c2-b315-50fa923dabcd | -14.05685 | -43.81907 | 2026-10-08 15:39:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 3c23571f-549b-3e06-b750-1d52508ebf2f | -14.26543 | -40.70086 | 2026-10-08 15:39:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 985f630f-1540-3501-88e9-2b96fd7504ed | -14.68694 | -41.85358 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0fbd574d-71a4-3ae2-9ec3-2f6d0c06f8e9 | -15.70366 | -40.59479 | 2026-10-08 15:39:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d45057cb-7dfd-332f-ba18-44ddd3a9aafc | -12.18791 | -44.82218 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| f3ccc830-5cfc-3ac4-86dc-e5185e02e087 | -11.76638 | -44.94412 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a46d68a6-f047-3089-9343-aa801fdeca92 | -15.56887 | -44.52342 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 8ee3dc80-14c9-309b-ac88-5ede5e9bfdce | -12.27126 | -38.93447 | 2026-10-08 15:39:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7403f51a-4099-3e2f-9b80-a898c9bfd3e2 | -12.23296 | -44.73943 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 896a28b8-f313-3ff3-bc2d-cb825b3d1fa7 | -12.15033 | -44.76336 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| da4f4c65-044d-341e-97fe-7b829cc7f922 | -14.41563 | -41.29284 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 46.2 |
| 50785489-b9b2-3fc3-93b9-dd8d2181f711 | -12.24562 | -44.73201 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| a6f37c9f-a322-36a5-8b43-ded987840238 | -14.4713 | -40.72204 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a5c07051-cc56-33bd-987a-2c308ce2f336 | -16.19617 | -44.57631 | 2026-10-08 15:39:00 | NOAA-21 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 37.4 |
| d08fb282-a6ea-35c3-846b-a66b079dd946 | -11.76379 | -45.57235 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 228f207c-b8eb-314c-97d5-fb46634c73ef | -11.76308 | -45.56575 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| cd2eabde-63f4-3358-a9bd-43d3275e5be1 | -11.92062 | -39.47519 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7afc07bf-c678-3b35-8a20-50f04fffbc0d | -15.11231 | -43.62957 | 2026-10-08 15:39:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 27.6 |
| c68c1ba2-24d1-3039-8e40-a4cd86cb6907 | -11.62106 | -43.68685 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 77ee825c-1ab2-374f-8043-bcdf8abc374a | -14.40924 | -41.28597 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 231.0 |
| f6a5b8c5-469f-37f6-a942-050da4cd9c53 | -17.06748 | -40.02137 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| b178dd4b-ca60-3787-b1a0-68b18ebd7793 | -11.71238 | -43.66032 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 78279843-511b-344a-bc83-0efca96287b9 | -17.11037 | -41.34975 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 795522b1-882a-35d3-9e64-309d446961f2 | -14.03458 | -40.55383 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 88a0ac67-ab5c-3a13-8119-5fad480b0d2e | -11.44919 | -43.38725 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| e05fb7b6-5c19-3037-b041-2fae2c6b0090 | -11.6257 | -43.61308 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 56d31ec0-928c-3644-9dfe-8201a8314c1c | -14.05743 | -43.82449 | 2026-10-08 15:39:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4dcbd54b-a2a8-3c2a-81a0-d47d303edc2e | -11.74171 | -43.64262 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 65b71001-25b3-3bc0-91f2-967704d7eb89 | -11.63577 | -43.59275 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| ab92c795-5e63-3a75-873a-959b1849b83c | -13.34692 | -43.96537 | 2026-10-08 15:39:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f5d29d51-7110-3ac1-91a8-f1bd114bf64b | -14.5714 | -41.67193 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 3f5b90fd-8065-3454-871f-9de6930c4329 | -11.35641 | -43.14468 | 2026-10-08 15:39:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| ed2497b5-a650-311d-a6f4-e2c2123f0873 | -16.1132 | -40.79321 | 2026-10-08 15:39:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README232.md)
