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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a522bbb-5410-3653-bf61-956f1ed24daa | -12.15506 | -50.07143 | 2024-10-02 01:26:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| ecf169a5-46c5-3af9-a698-3eab3e99adee | -12.15257 | -50.05596 | 2024-10-02 01:26:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2b1a4c09-ad7d-3fa6-80ff-a2dcafc13bfc | -12.13869 | -50.04239 | 2024-10-02 01:26:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a9790958-c3f9-3468-98cd-724a9b696267 | -11.34831 | -50.79649 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 737a5f9e-6396-39fa-b0c5-8ff6dad36450 | -11.10384 | -49.61039 | 2024-10-02 01:26:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 78b29b51-f6fa-31db-94c1-e58a13413dc1 | -11.08903 | -49.59495 | 2024-10-02 01:26:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ab485047-7642-38fd-a3ba-865544ac40c1 | -10.92012 | -50.12212 | 2024-10-02 01:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2bdc4eb7-8f05-3d3f-b8f7-d564e597fb33 | -10.91105 | -50.14008 | 2024-10-02 01:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cb9e564c-9aed-3cf7-a5a4-5031713ee017 | -10.90853 | -50.12406 | 2024-10-02 01:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 106b3c33-6c39-3952-826e-451772c09775 | -10.89948 | -50.14202 | 2024-10-02 01:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 73037c0d-1fb2-30ca-a6ea-5a1d73154d17 | -13.59533 | -51.14205 | 2024-10-02 01:26:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 4729f092-b319-3ff0-aa57-4d4ddb93c76f | -13.59337 | -51.12967 | 2024-10-02 01:26:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6d917541-98f7-3b0a-ba3e-14655929b55d | -13.5882 | -51.14962 | 2024-10-02 01:26:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 31872a22-6274-3996-9be6-34cd0d2a77ff | -13.58632 | -51.13723 | 2024-10-02 01:26:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 4c98cedb-c8ac-31d3-ac8e-36d4421e4af7 | -13.5809 | -51.23908 | 2024-10-02 01:26:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4467d465-d7ac-3ac8-91b1-8ae75e15ba2f | -13.56697 | -51.2163 | 2024-10-02 01:26:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0f75be95-36a1-3c31-a489-c81574412e06 | -13.56508 | -51.20404 | 2024-10-02 01:26:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0ecbb9ba-d218-3034-bc6d-bd13a1d32fd0 | -13.20787 | -51.21177 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| d08a686c-baf8-33e3-b5f7-7e3357fb2cf1 | -13.20597 | -51.19935 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f55b0ac5-54a4-3007-8df0-814774143de6 | -13.00035 | -51.13002 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2bc67b6f-6c89-36a5-8a88-c6e3104c4a95 | -12.9939 | -51.15697 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 08428504-9a13-39fa-a57d-975ae0735aa0 | -16.10707 | -50.41577 | 2024-10-02 01:26:00 | TERRA_M-M | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 37c609b8-6550-3a5a-ad55-4cfce0e32bbb | -16.10329 | -50.3245 | 2024-10-02 01:26:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ad2fada0-3d4b-3317-bdae-2559d0ecce42 | -16.10127 | -50.31166 | 2024-10-02 01:26:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 41.0 |
| e1a5f85c-8da9-3120-8ed0-bf817c782029 | -16.06993 | -50.38272 | 2024-10-02 01:26:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2d9512f3-9d92-3a8e-8eed-171dd71d61f2 | -17.28761 | -50.61863 | 2024-10-02 01:26:00 | TERRA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 919ee7da-2ecd-3bf0-9c2b-0beecee6adac | -17.28653 | -50.61301 | 2024-10-02 01:26:00 | TERRA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 59b01895-7171-3346-9d39-5431beaccaf3 | -10.43859 | -50.80208 | 2024-10-02 01:26:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c5fad481-c678-37c0-b800-8a94ae112a78 | -13.19762 | -51.21346 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 13b48072-dca9-3e3d-a56a-dffd439f10c4 | -13.16048 | -51.245 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cfb616f9-067f-3e2a-a9be-de19d82258ed | -13.13937 | -51.22902 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 710374ab-c964-3d9d-92b2-519644bb5773 | -13.11728 | -51.35864 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d8d1d85f-7883-3b2a-b563-be119f5dd396 | -13.10072 | -51.38626 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ed05d925-a69f-346e-9ab8-8f548320b63f | -13.0981 | -51.43623 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| ca0ae2bd-476b-3d96-9a6e-6c4c3958b586 | -13.09622 | -51.42419 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| de5940d7-51f9-3289-b334-1737c47dd457 | -13.08987 | -51.4499 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 283535f7-e1e9-3403-8674-49b47a95d466 | -13.08799 | -51.43788 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 392.3 |
| 401ed65e-04d8-3325-9228-14302b36ddf0 | -13.0861 | -51.42585 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 1e665320-33d4-3d43-8131-923a5a8616d3 | -13.08422 | -51.41378 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 7c5b1368-3e88-3dc7-916d-3eee9fb30c0f | -13.08233 | -51.4017 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cf5847b2-078f-332b-b82b-7eb1e92ffaa7 | -13.07979 | -51.44553 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1f8b252d-c04d-3450-b4cd-e283940c587c | -13.07798 | -51.43348 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 343.4 |
| 54561ea5-35e1-33f4-8f33-4ee0e1e84790 | -13.07788 | -51.43954 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 457ee19c-e307-3851-8e51-d2a95ceb5a14 | -13.07616 | -51.42141 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 2f25d981-d872-33cf-acda-0dd522471767 | -13.07598 | -51.4275 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 9d65cc52-7094-34f5-a3be-1b70c0beb5cf | -13.07069 | -51.38507 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 725fac61-86b5-3388-a0da-50b48d0eb5b6 | -13.07029 | -51.39126 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| e7bc7d2e-10c7-317e-afc8-6a5a0bf8d0c4 | -13.06886 | -51.37291 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 067e95da-581a-32de-83ba-899ace064846 | -13.06838 | -51.37914 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3ec7d21b-39aa-3922-baef-911ac67170a4 | -13.06647 | -51.36699 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5ed24463-07f4-3ceb-a680-b802842778ed | -13.06604 | -51.42308 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| afee7ac4-1804-39fe-8238-a39ff94975d2 | -13.06054 | -51.38674 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 21fed721-a4e9-3886-9bab-6d7e26d163f5 | -13.05407 | -51.41266 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 19e29843-1583-3476-8f56-a44816effb31 | -13.05315 | -51.33798 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5cbdc80a-e675-3303-bf3f-8c73b66a4bcb | -13.05223 | -51.40055 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3d77a6f8-8f3f-38bf-9441-4fde7c91d893 | -13.00639 | -51.50675 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7fb82fad-84f7-39b4-a93d-1655821dcce6 | -12.9815 | -51.54119 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 88bcf000-57db-394d-ae17-d76dba38d409 | -12.96963 | -51.53093 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| db2906af-06b3-3184-a5e3-6151e8cc9a18 | -12.95956 | -51.5326 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 327e9d37-1a13-3007-a8c3-f2981bd711c8 | -12.95773 | -51.52064 | 2024-10-02 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 9effae51-ec0e-3ad6-a308-bd6611ed0f93 | -10.90109 | -52.42328 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 14d7b4fa-319b-3e0b-b60e-cef9e516d359 | -10.89944 | -52.41214 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 572558bd-adaf-3038-9460-3ca7830b06fe | -11.08133 | -52.52967 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a21ff921-89c8-3deb-9877-99cb861327b8 | -11.07971 | -52.51876 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0cc6baa7-56bb-33d0-bdc0-7e8b6f6e7f83 | -11.07 | -52.52032 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 554be096-d967-3677-b94b-8719112c2cc5 | -11.05698 | -52.49989 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bade9282-9f34-36c7-9d83-da2d668aa536 | -11.04725 | -52.50139 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 810c0f81-9c6b-3645-9e61-429938425f3f | -11.04559 | -52.49042 | 2024-10-02 01:26:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c16228fd-1134-3464-9ca4-1612fc55990f | -12.91223 | -53.88816 | 2024-10-02 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b3c920d8-1383-3b8b-a16f-30fa7d1874be | -12.91089 | -53.87888 | 2024-10-02 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 22907d04-1977-356d-abd4-80a11e212779 | -12.87466 | -54.01404 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c39a8fd5-a61a-3c18-a11e-7aa869ef5d32 | -12.73794 | -54.02186 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 970bf61a-0fad-3559-9a1e-5a0aaf77d2c3 | -12.68204 | -54.08387 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f9ef77d-af61-30e8-b3d8-8e1820bbcc7e | -12.67178 | -54.07603 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| ffb53d48-7927-392e-8258-642d8b27e4ba | -12.66914 | -54.05758 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f5e9b087-530b-38d7-baa3-8ee46d4e1f0d | -12.66284 | -54.07738 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ee27b60a-50f0-3916-88af-678a8cdddbe4 | -12.66152 | -54.06817 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| abad4014-69e2-3e6d-93cc-4ff1ea5b2509 | -12.60719 | -53.50057 | 2024-10-02 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c3de600a-6526-3db4-89a4-a3c342b61e41 | -12.6058 | -53.491 | 2024-10-02 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| da518cb7-ca2f-336e-ac60-a5dc3afc0033 | -12.33459 | -54.10443 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| abb4902e-6b07-3392-8cb7-bcf7dca71aae | -12.33327 | -54.0952 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 31e1e5b4-bd71-3051-8b86-0b58cb02078f | -12.32563 | -54.10579 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2a6a80d0-ee69-3369-ad19-b7a978d3a8d2 | -12.32431 | -54.09655 | 2024-10-02 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d58ab00b-a985-3189-aecc-46d88f4c4c66 | -12.26618 | -54.01078 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a7c38e17-777b-3ac8-b6c7-28cce2e76421 | -12.26484 | -54.00151 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 29c0d02b-352c-3345-8dad-e3a7f692cc43 | -12.26349 | -53.99221 | 2024-10-02 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dac75a5f-d36f-3301-bbaa-e038591c1802 | -12.59309 | -53.14479 | 2024-10-02 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a10c1c68-b602-3e5b-9946-b408d6e3a143 | -12.58386 | -53.14625 | 2024-10-02 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a2d70784-42d9-3bc3-87fc-f625a96c5b1a | -12.50851 | -53.14787 | 2024-10-02 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e69b5ba7-abf2-3ecc-9342-e867432b03f1 | -14.80297 | -53.90085 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c797c90d-b627-365a-b342-ad589ad762d3 | -15.38105 | -53.7501 | 2024-10-02 01:26:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4fc404e5-a231-3d61-8189-bdef51671205 | -18.69769 | -57.3127 | 2024-10-02 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 59fae5bd-1bcf-371f-858e-2c9ddb5030a8 | -10.62346 | -54.06425 | 2024-10-02 01:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 258e3a32-e9da-3dbd-9d16-246bcc42ddd9 | -11.43326 | -54.31128 | 2024-10-02 01:26:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 66ea669d-91bf-3c3f-8c7a-140436425908 | -11.43195 | -54.3021 | 2024-10-02 01:26:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c424523d-4135-32c3-8815-a02346b03814 | -11.42118 | -55.06871 | 2024-10-02 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 11b82551-4e75-3c01-a08e-6b81412db124 | -11.41992 | -55.05972 | 2024-10-02 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b0b6e66b-672d-37af-ad66-019aff403ccb | -11.38101 | -55.11762 | 2024-10-02 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fe377b0d-eecd-38ca-a4e1-aa258b463c1f | -11.36577 | -55.20228 | 2024-10-02 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 819dab97-d5c8-361f-851b-51aa604d5073 | -11.36452 | -55.19331 | 2024-10-02 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |


[Clique aqui para ver as próximas entradas](README34.md)
