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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4ed2f78-ac92-3c06-b364-8622499d07ac | -6.70356 | -44.09177 | 2025-08-02 05:12:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bf78b4b-6983-3f9a-b524-7f824b05d321 | -8.23116 | -49.93457 | 2025-08-02 05:12:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac2d9a50-864f-3011-8a27-8a101c2e99b4 | -4.77517 | -45.33403 | 2025-08-02 05:12:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13b871ce-edf7-389f-b2e0-122e07b6301f | -3.51648 | -47.22297 | 2025-08-02 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5bab018-e7f4-38d4-8deb-79828fbaa3f0 | -4.31684 | -48.10215 | 2025-08-02 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4605636-2179-3bcc-b410-ca2150495b5c | -9.38912 | -45.49739 | 2025-08-02 05:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa1627dd-6e65-3ea6-9b2f-b885a46d1b32 | -9.08916 | -45.89949 | 2025-08-02 05:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dfde710-77c7-388e-b5f5-6a6a80923a87 | -9.05987 | -45.05798 | 2025-08-02 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52d919c3-efcf-3855-922d-ee0c002fea4b | -9.39576 | -45.49807 | 2025-08-02 05:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c173a90b-11a9-3e11-8a4a-d8fc58d749af | -3.52612 | -52.86577 | 2025-08-02 05:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a58da73-ff58-33ac-9ce1-6a4207354191 | -7.03919 | -44.41272 | 2025-08-02 05:12:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95062f3c-7901-3af9-a4b1-6c4414326668 | -8.57178 | -51.5419 | 2025-08-02 05:12:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1fde020-2ed4-352c-9f5f-1a3eb393f87b | -7.34433 | -44.65925 | 2025-08-02 05:12:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 189550fb-6d16-3f2a-8603-ed7e65e3db95 | -11.41376 | -56.86346 | 2025-08-02 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5251461-9458-3b4e-80d4-95093a4bb5eb | -15.57054 | -58.70787 | 2025-08-02 05:14:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3beb92c5-bc01-3bfa-8d3e-9c6fcf64267a | -12.67363 | -48.09203 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 366d9fc2-2c48-3879-b196-65ba1c9ebc0a | -12.67203 | -44.50338 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 02ccbd9b-37ee-3d57-af47-c897f814fc42 | -15.11441 | -55.22206 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32ad2b62-7874-3d94-bae4-1543367371c7 | -13.99409 | -53.92837 | 2025-08-02 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f777198-dff2-3721-a72c-821d441be797 | -10.46702 | -46.96399 | 2025-08-02 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c13bccbe-e803-3a65-92e6-9cac81e5b81b | -11.41716 | -56.86399 | 2025-08-02 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bd265ad-1b8e-3525-92fd-1ef53c665f99 | -12.44881 | -47.0408 | 2025-08-02 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7393941-7692-38d9-8151-1161ea2565c1 | -11.94301 | -46.67516 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 901d72ee-6e73-330f-9167-779c8d428b82 | -10.63809 | -45.23799 | 2025-08-02 05:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fa2f530-bdcc-37e7-bbf7-90797167303b | -15.76084 | -49.94952 | 2025-08-02 05:14:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 537e9008-22b2-33f5-9164-d969b3284a34 | -12.44768 | -47.05074 | 2025-08-02 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 092efaf4-0168-394a-8277-b6ed28d66bd2 | -12.67282 | -44.496 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 34dfb59b-5400-39a4-8d78-26b0a963e30e | -12.45621 | -47.03161 | 2025-08-02 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e15601b-a2b5-3af9-b502-7b0e80a8a2e8 | -12.44143 | -47.04996 | 2025-08-02 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f201f0d-8fdb-3af2-9266-a31f9adf22b4 | -13.05983 | -47.44751 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a7ccb1d-c186-329d-95e6-473f7d0f2f43 | -11.9446 | -46.6755 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06afbd5b-8f98-32bf-aa55-b9a4b909a46a | -13.69271 | -51.95649 | 2025-08-02 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51964b9e-2c1b-3d79-93f1-2e3f92746813 | -12.66992 | -44.53827 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6affff3-a878-32d3-a329-242328d4f16d | -14.21853 | -49.05523 | 2025-08-02 05:14:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43f6eb7e-0b16-37ed-afd4-589a6baa5df3 | -12.67043 | -44.51828 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 80d16b89-3160-3ccc-a6f4-910ba8a8c26d | -15.10858 | -55.23579 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3920852-ee57-3f7e-8682-4ea9a4315299 | -12.65096 | -44.49363 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 168feaee-1a45-3b8b-afe5-a96e63a131b0 | -11.90778 | -54.7852 | 2025-08-02 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e47c10c9-c2ad-3630-91f3-8f318e28c30e | -13.21724 | -47.24877 | 2025-08-02 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f37c1b4-4009-3af4-8983-bf9cffbb72c0 | -15.12132 | -55.22012 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88f9ca6e-4d1b-361e-bcad-b7223fc19e3f | -15.1119 | -55.21246 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74708012-66e4-3493-8ff6-db49a7d798fa | -12.66632 | -44.48783 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 81d3797b-4281-35a6-8dfb-c11c42e562bc | -10.37563 | -55.31944 | 2025-08-02 05:14:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afb791e7-a7fa-32bf-aaa9-7d3b1f84561e | -12.65904 | -44.48698 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 618a7745-f29b-383d-a3d1-7f786a597e34 | -10.58521 | -45.27531 | 2025-08-02 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10ca6f5f-4e22-3d94-9735-b90843f3ac34 | -10.45823 | -46.93386 | 2025-08-02 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4651d72-570a-3325-9724-71f0ae482270 | -12.67361 | -44.48861 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 42199aad-b2fb-3334-a273-cffd25aba79c | -14.87418 | -57.51614 | 2025-08-02 05:14:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ae058ce-5ea9-3d8a-b672-23f0dfa59411 | -12.7149 | -47.79376 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37230bd0-a729-34bf-8d47-974f3f926c29 | -16.69959 | -47.57846 | 2025-08-02 05:14:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa15997e-499c-3aa0-a7cc-bfa43910e233 | -11.90932 | -55.48595 | 2025-08-02 05:14:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b8bd523f-9a91-3344-8c8c-4fdd86f872df | -10.59355 | -45.26328 | 2025-08-02 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b49818be-114f-3524-bd0a-84508f63d00a | -13.69731 | -51.95705 | 2025-08-02 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecc35b25-8313-3e99-8439-2a3d7ddb1777 | -11.94401 | -46.68066 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 369bb946-36fc-33cf-887b-f83293189dd2 | -11.91152 | -54.78575 | 2025-08-02 05:14:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98b08813-6ee5-37f3-b511-75109d842751 | -14.60364 | -57.48286 | 2025-08-02 05:14:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ad0f6f6-22b8-3498-ab25-ba20aba57b5b | -11.95156 | -46.67097 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43b39bbd-7390-3972-b713-178096b6e54f | -10.46203 | -46.95391 | 2025-08-02 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7027ccb8-30db-3df9-9953-c31786580307 | -10.64556 | -45.23825 | 2025-08-02 05:14:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebc87b7e-7da5-3238-90f0-9cb2be3438ee | -12.67691 | -44.52654 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef35aee3-6563-303d-b753-98c73dde822d | -14.90972 | -51.0579 | 2025-08-02 05:14:00 | NPP-375D | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a3b4194-f50c-3d6c-a157-38b1bd43ecea | -11.18919 | -55.02016 | 2025-08-02 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b792a6ba-cb80-35b8-a917-3c9604727b8b | -12.6728 | -48.09896 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c48a66d0-cc94-350e-abdc-c5726f614080 | -12.46293 | -57.87568 | 2025-08-02 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71228624-edbe-38e3-b39f-336c04003d0d | -15.11506 | -55.21753 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ea75bc16-50f1-3c10-a807-be7360778be2 | -14.21808 | -49.0592 | 2025-08-02 05:14:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b3e0a2b-00ee-304f-80c8-87d981f88c0a | -13.06865 | -47.42498 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e1e18fed-7583-3bed-911d-09a207ca9263 | -10.46759 | -46.9594 | 2025-08-02 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfc3ee7c-6f90-3936-805f-3b5b5a358aab | -12.67442 | -44.49371 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 651ce2d2-76bc-38d4-aab3-09dcae39af07 | -12.64939 | -44.50845 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 05d7b145-d759-32b0-bd67-58e44ea89bc5 | -11.19278 | -51.51862 | 2025-08-02 05:14:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c6dd3fd-9cfd-3d95-a0f1-8be45284f8ef | -15.11371 | -55.21908 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9e6028ab-3349-3849-a81b-525990eee665 | -13.23107 | -47.23782 | 2025-08-02 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 042172ef-acc9-3143-af0f-33bd90ccdd2a | -12.67367 | -44.50113 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e5fed143-6f76-3b0d-9fea-2567672af98e | -12.67517 | -44.48629 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2fdf1946-cdc9-3fd5-82ae-643cf96b054a | -10.46318 | -46.94443 | 2025-08-02 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a233dd9-a35d-3444-9904-205e575689d6 | -12.66713 | -44.49291 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3701dc12-db62-3085-9d1c-819142160a81 | -13.03926 | -46.75359 | 2025-08-02 05:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57c53a59-e7bb-3967-abf4-5edd9b55b84e | -12.66266 | -44.53732 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0d8d129-42e9-3331-9d7d-0be5c6313bf8 | -12.66475 | -44.50261 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d14800dd-9a17-33d9-aa55-538b4ed1535a | -16.70646 | -47.57396 | 2025-08-02 05:14:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d36a5f05-30dc-37ae-a781-202044e3db27 | -10.03492 | -44.7177 | 2025-08-02 05:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6eec0428-acd7-35a9-9f7a-1d4e494ed7f2 | -12.67532 | -44.5413 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fde45a5c-30a8-3da1-9160-f13531f26ddc | -15.11238 | -55.23637 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76121ee0-08a2-3319-ae40-c5a3ccce5955 | -12.70892 | -47.79298 | 2025-08-02 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba9ad657-3839-388f-a7c9-c4a489107a5d | -12.67066 | -44.5309 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e785ad75-426f-3588-a7cf-0eee5c12e190 | -15.11126 | -55.21699 | 2025-08-02 05:14:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 989987a7-4109-3f65-9d5c-098cf60324e2 | -12.65746 | -44.50186 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e1e47cf-cdcc-31a6-a026-a53c4484619c | -10.03569 | -44.71088 | 2025-08-02 05:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b51e12c-ed54-3cc5-a6aa-0e23487e9471 | -13.70254 | -51.95282 | 2025-08-02 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37dbbf43-6dea-35b6-a824-88da926d169c | -12.45563 | -47.03666 | 2025-08-02 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 036b9e90-11c9-3129-a5b1-8a87192df966 | -14.77938 | -59.56615 | 2025-08-02 05:14:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e7330ba5-1ac4-3aae-908a-b38d16fb2b90 | -10.0443 | -44.71648 | 2025-08-02 05:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31574036-e74b-324e-9ea0-e15704bb9400 | -12.67717 | -44.53922 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3a366faa-52ed-33c2-8215-31b16b152d1a | -11.96493 | -46.66693 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85f93ee5-cb4b-3e65-a45d-64009a3adb3b | -12.67292 | -44.5086 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c3c50084-0235-385f-9796-91febb25ebf8 | -11.94238 | -46.68035 | 2025-08-02 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e919cf5-056f-31d3-87b5-67e9b19571f8 | -12.66964 | -44.52567 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bd137fe-c995-3e0d-826b-c58592ba328b | -10.57848 | -45.27385 | 2025-08-02 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7b4c24c-5fc4-3a72-b980-c2605db12f14 | -12.66564 | -44.50776 | 2025-08-02 05:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README22.md)
