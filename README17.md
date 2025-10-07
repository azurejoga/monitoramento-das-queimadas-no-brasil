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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 592aca2b-7f34-34a4-b525-2b281909a046 | -14.62349 | -43.8945 | 2025-10-07 03:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9adfef1-9498-3c8c-8f8a-bd6cff3bf76d | -14.62484 | -43.8884 | 2025-10-07 03:17:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3cab35cf-00b0-3c1b-804f-02209b4c9bd3 | -13.66334 | -44.31011 | 2025-10-07 03:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c6f4808b-2667-318b-9884-e9ba9d60d142 | -11.6064 | -43.1143 | 2025-10-07 03:17:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca73ad07-ab77-30ef-9e1e-27ee6a216c40 | -15.60133 | -42.37827 | 2025-10-07 03:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb13185e-e9e2-3663-816a-851d7a3d00b3 | -13.50039 | -43.67442 | 2025-10-07 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 980a3a0c-c97c-3a34-9d22-1135f6acba06 | -15.59228 | -42.36182 | 2025-10-07 03:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e08404a3-875b-3197-83ba-0be31e1a7bba | -15.05515 | -42.34118 | 2025-10-07 03:17:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 04c4586f-c610-31ad-9db0-24a04865b557 | -11.60509 | -43.12046 | 2025-10-07 03:17:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c10af34b-1bb7-305b-a009-8e2ba3b18361 | -14.99003 | -42.02235 | 2025-10-07 03:17:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a4b16c74-e91a-34e1-b660-df53dbb7a8c1 | -13.80696 | -41.83109 | 2025-10-07 03:17:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a717de63-98b0-3640-ab8d-31a54896e581 | -13.80791 | -41.82642 | 2025-10-07 03:17:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53b16cc7-bdf7-3b8d-a567-ba33c7096da8 | -13.66386 | -44.31527 | 2025-10-07 03:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ab4912f-f4e6-3e2c-b1d1-eea216e7f59b | -14.81008 | -44.90432 | 2025-10-07 03:17:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72221c8e-1a55-3c71-b6de-2fc271de56fb | -15.60234 | -42.37355 | 2025-10-07 03:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 765012f6-9254-3536-8b3e-d2140986c644 | -14.98785 | -42.02065 | 2025-10-07 03:17:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 179d959f-98a9-3e51-95bf-0a207b5faee4 | -11.45947 | -43.50333 | 2025-10-07 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b393588f-2b30-3202-b76c-581f455ac9d1 | -13.85524 | -43.99058 | 2025-10-07 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aed8b663-a121-3bdb-b91b-3c887bbd3202 | -15.59126 | -42.36653 | 2025-10-07 03:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb1d2b2d-19a1-3f7c-bcae-4a41aa5b56d3 | -13.86132 | -44.42065 | 2025-10-07 03:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9e3a4d0-050c-38df-852c-855a85513b2b | -14.80838 | -44.8981 | 2025-10-07 03:17:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 440ac062-d9e4-3613-8b94-845a314c6ff6 | -14.99698 | -42.01895 | 2025-10-07 03:17:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 143b8780-9d39-3459-9e0c-f6d9f07cde9f | -13.85385 | -43.99695 | 2025-10-07 03:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d4bdb62c-d1bb-36a4-a941-21f3da922086 | -13.50172 | -43.66827 | 2025-10-07 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 7d7ee4f7-cc8e-39e8-934e-a08c56605022 | -13.49907 | -43.68058 | 2025-10-07 03:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| cb57f4b6-42fa-3a45-b1e0-12975c842eb3 | -14.99476 | -42.01728 | 2025-10-07 03:17:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 84d917e9-4985-38f8-bebe-e9efe0609382 | -15.59632 | -42.3723 | 2025-10-07 03:17:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d08bb018-5977-308d-930e-a09bf427336f | -11.45813 | -43.50969 | 2025-10-07 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c08aea48-e182-35da-aaeb-18d33b3c7f9b | -15.05404 | -42.34637 | 2025-10-07 03:17:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 6c9f4837-4e9a-3928-b42a-0a0cea5164c4 | -11.74587 | -43.29783 | 2025-10-07 03:17:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0574e871-2d1f-31e6-a8ba-c48424f0b160 | -13.53687 | -43.00013 | 2025-10-07 03:17:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f365dc87-4ce1-3915-88a7-602b8afdcc66 | -13.8543 | -44.4194 | 2025-10-07 03:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91b622dd-ea50-35e3-8e91-14b0a84d1293 | -11.73911 | -43.2963 | 2025-10-07 03:17:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 874c58e8-c1b5-3511-8977-eca58cb50f95 | -11.38202 | -43.49786 | 2025-10-07 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc2d9079-16cb-3c67-9f39-37255714f984 | -14.80305 | -44.90271 | 2025-10-07 03:17:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a93ba7cb-f33f-3bbf-baae-0438108729af | -13.66518 | -44.30911 | 2025-10-07 03:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1dc142dc-113c-383d-bc3d-24602b411160 | -13.66197 | -44.31633 | 2025-10-07 03:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 571ed979-6b3b-34a5-81b0-bb8fc372c639 | -19.10669 | -43.16391 | 2025-10-07 03:19:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 83234649-bf05-3f26-92ab-e254d08493db | -20.2058 | -43.92725 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ef90544b-8aae-3697-bc89-f8f07f4f1d8d | -21.60705 | -44.00201 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3f6a0cd1-e4f9-3de1-8499-75f291d5f660 | -21.51482 | -45.59952 | 2025-10-07 03:19:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 81c8d9e9-26fd-39b7-8505-3a20ac39a2b3 | -18.77916 | -44.61889 | 2025-10-07 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c38b429d-e41d-3c3b-814f-ea1ad00811b7 | -20.20204 | -43.91581 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 57ec244e-99e2-3f7d-855f-734cc04ff2ec | -23.202 | -47.25204 | 2025-10-07 03:19:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c6d0e293-8efd-3c8b-923b-f810ade0d40d | -20.19981 | -43.9256 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 11c357a3-57c0-326f-a69b-73607260620a | -21.54784 | -44.27864 | 2025-10-07 03:19:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74432e67-ba78-378a-a2db-3577ee4c4c44 | -21.90191 | -44.89566 | 2025-10-07 03:19:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| dd176b73-dc7e-394c-91a0-0569bc86d679 | -18.56721 | -44.1859 | 2025-10-07 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e973e324-ce0d-3948-9e1d-62b046784e10 | -22.87933 | -43.72423 | 2025-10-07 03:19:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67bcc953-3ff8-353c-841d-bf1c42c2a8c3 | -19.78807 | -45.84491 | 2025-10-07 03:19:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f52a6cd-adf5-335a-83a0-56280d9eed83 | -21.61112 | -43.99799 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb5fe0b3-78c2-39be-a734-d06dd3257789 | -23.22444 | -46.56517 | 2025-10-07 03:19:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 64f0beb1-637f-39da-b9a2-a7302af1b1fe | -20.1133 | -44.41853 | 2025-10-07 03:19:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 0c1dbc12-9292-35a9-8491-2087523e6b46 | -20.25502 | -41.94408 | 2025-10-07 03:19:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c8d6f948-f1ef-3174-b0c1-9b8545ae2394 | -23.20395 | -47.24443 | 2025-10-07 03:19:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f794d71c-8006-37a1-ab06-0fa99967851e | -20.1006 | -44.19038 | 2025-10-07 03:19:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e1a49f0c-a212-3641-9068-57108524a0c9 | -18.6715 | -44.04747 | 2025-10-07 03:19:00 | NOAA-20 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d18ddda4-810d-376a-9b33-e5c03754403d | -21.54894 | -44.27404 | 2025-10-07 03:19:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| abfeca35-2b0e-3f84-a60c-744aa8c15b9c | -23.20207 | -47.25161 | 2025-10-07 03:19:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3551fd2e-5f74-3c2d-8d90-358bb7576a40 | -21.07448 | -46.91304 | 2025-10-07 03:19:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| caab448d-3314-3a17-80e0-faef4341f3f9 | -21.61518 | -43.99393 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4a23d832-0acb-3cef-9072-ee18d170b743 | -21.74501 | -44.42129 | 2025-10-07 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d31b9b21-52d1-30bf-bbd6-b174244fc448 | -21.74631 | -44.41584 | 2025-10-07 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c434d293-cede-327a-b728-39b65ca782dd | -20.11461 | -44.41283 | 2025-10-07 03:19:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ebe4bb3f-b0d0-3ecc-963e-332ba53b2925 | -21.07643 | -46.90527 | 2025-10-07 03:19:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b29690e3-99a3-3a3a-a0fa-f304a2bffd56 | -18.04141 | -43.15099 | 2025-10-07 03:19:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 79fbeffc-c34c-3b08-bfc4-6501893bf379 | -22.88494 | -43.72581 | 2025-10-07 03:19:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 02b07c83-596e-311a-bb15-bb4c0c66b2f0 | -21.09472 | -44.18418 | 2025-10-07 03:19:00 | NOAA-20 | TIRADENTES | MINAS GERAIS | Brasil | 3168804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 85375c3e-6f4c-3e54-888f-c33b1db5efd6 | -22.12972 | -42.91761 | 2025-10-07 03:19:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9c2f478-e935-3ef3-bc1f-2b39e9e7aaa4 | -18.04647 | -43.15669 | 2025-10-07 03:19:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 70bb8eff-d10e-3f11-96d6-00b08476abdc | -18.27488 | -45.46877 | 2025-10-07 03:19:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 39734dc4-ca04-3bba-acfb-aae410671b81 | -21.61793 | -43.99542 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 55a135c3-4cc4-3145-b378-fb5b8020b46f | -21.7438 | -44.42638 | 2025-10-07 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 67e63fcc-716b-3d21-9c90-128f2c66d45c | -20.7491 | -43.47589 | 2025-10-07 03:19:00 | NOAA-20 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 610a7a8b-c7cb-3b23-aa44-65e5f8f2d016 | -21.7388 | -44.41768 | 2025-10-07 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1ae8bbeb-352e-315a-9b38-5688bdc232b9 | -20.20801 | -43.92111 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6f050f4d-9bc8-3ca6-a8ba-70da7d658c06 | -20.82347 | -42.49107 | 2025-10-07 03:19:00 | NOAA-20 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5c93fb97-0c38-31fa-8d91-306ad6e1aa0e | -21.73903 | -44.41965 | 2025-10-07 03:19:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3ea0c7fc-e85b-3abf-ba28-6dad8bd477b1 | -21.08854 | -44.18344 | 2025-10-07 03:19:00 | NOAA-20 | TIRADENTES | MINAS GERAIS | Brasil | 3168804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 71c73f6e-78c5-342c-997a-9177008490af | -20.11772 | -44.41617 | 2025-10-07 03:19:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cbca7628-5390-3fa0-a2fa-2e89ea98281d | -19.7071 | -44.12311 | 2025-10-07 03:19:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 539e055c-8a76-3795-b0cc-491927d2b0d4 | -21.73759 | -44.4229 | 2025-10-07 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3608c568-1f92-3da1-8b2f-eb4fb3038744 | -22.88013 | -43.72831 | 2025-10-07 03:19:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 38c31ea3-7770-3024-861a-05ac6bd44e2b | -19.78875 | -45.84711 | 2025-10-07 03:19:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8aca8d64-b9ca-3833-9bd8-d6f8430fffd2 | -21.89983 | -44.87698 | 2025-10-07 03:19:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fae760fb-e415-3908-9312-92e0ee71f51b | -20.32418 | -45.12061 | 2025-10-07 03:19:00 | NOAA-20 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f3215e38-af9a-34c6-b01d-bb1411e10f3d | -21.61412 | -43.99844 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ef2ad1da-3d0a-377f-b4f7-6f38820d5b29 | -21.90594 | -44.8787 | 2025-10-07 03:19:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7bc8b51b-11d5-3532-9c1f-deeff50007e3 | -18.27673 | -45.46095 | 2025-10-07 03:19:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2eacfa2c-639c-3a54-a64b-825089867d89 | -19.78641 | -45.85192 | 2025-10-07 03:19:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ba0e99a7-dc1c-3b35-a1a0-c45c9848cedf | -17.95948 | -44.41161 | 2025-10-07 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e24115d7-506c-3e1f-858b-9b7d1fa08937 | -20.09475 | -44.18765 | 2025-10-07 03:19:00 | NOAA-20 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01490a46-0320-3061-a94c-8d95440c6d1a | -23.20385 | -47.2448 | 2025-10-07 03:19:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 50563b48-d4f5-36f2-ae07-dd03e6145c9c | -20.31644 | -45.12453 | 2025-10-07 03:19:00 | NOAA-20 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b9a07faa-be87-3d10-8e28-98770d15a553 | -21.74477 | -44.41938 | 2025-10-07 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1b0fd32a-c41f-3e29-8568-64c2c29a13ba | -17.95301 | -44.41008 | 2025-10-07 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3917f4e2-2fd6-344e-a8f0-67187c6c0650 | -21.6082 | -43.99715 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fb6aa869-8749-3e1b-b1db-f93df9bd0b31 | -22.58079 | -44.44896 | 2025-10-07 03:19:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 06b39af7-5998-3574-95b0-7ba5e555edf6 | -21.49189 | -46.0251 | 2025-10-07 03:19:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 55891535-60e3-38ee-a7e8-4d18d5d504a8 | -18.77781 | -44.62466 | 2025-10-07 03:19:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README18.md)
