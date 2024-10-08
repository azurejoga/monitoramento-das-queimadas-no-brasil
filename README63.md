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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28f3ee88-99dd-3d75-acce-e5f808a1bb40 | -19.55145 | -49.48949 | 2024-10-08 04:36:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca96c128-41c4-39b6-b2d2-7607293b4533 | -19.55089 | -49.49327 | 2024-10-08 04:36:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7ab9539-169f-3200-bbdb-15af76739467 | -16.41212 | -49.93171 | 2024-10-08 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e278c54-aa5d-3009-8093-5b99b58e7a8b | -16.40937 | -49.92759 | 2024-10-08 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30d1f3a9-7c63-3989-900d-face2611f0bf | -13.93011 | -49.20532 | 2024-10-08 04:36:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40d3dd84-97ae-3cc2-bc9c-1ab1e3db0124 | -13.80358 | -49.29669 | 2024-10-08 04:36:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce5b2aaa-6d87-395d-90dc-52f574bc2576 | -16.41267 | -49.92814 | 2024-10-08 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a78c4fac-b6df-315a-a468-cafc5de5c6e8 | -16.40881 | -49.93116 | 2024-10-08 04:36:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 533126a4-3640-3871-8679-4bd336a98136 | -16.35653 | -49.56563 | 2024-10-08 04:36:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e9a5bb5-6a0d-353e-84ab-dcfd046485cb | -16.35267 | -49.56867 | 2024-10-08 04:36:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a868fe5-f52c-3928-8158-7231bfa44648 | -16.10778 | -50.22509 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9ca4cf1a-b5c2-3204-8003-1623d7efb8b5 | -16.10722 | -50.22865 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b0ce0836-121a-3390-a953-a73ae3554e30 | -16.10448 | -50.22453 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 99ef6f36-d490-3eb4-8a01-53adaedcf106 | -16.0991 | -50.1909 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8d4886a1-e23f-3fe4-8c2f-626e61207084 | -16.09854 | -50.19447 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9fe78ad9-7ea3-31aa-8758-5f3c5e5bdfb1 | -16.09791 | -50.22002 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9900f41b-2862-3e89-aac2-f9f60baf8249 | -16.09742 | -50.2016 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66286daf-717e-30b5-a0c1-21e47cab1791 | -16.0958 | -50.19035 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 147aff7d-5788-3ebe-b538-096520f497a5 | -16.09517 | -50.21589 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 560ff794-b850-3cba-8758-88c72a01aada | -16.09468 | -50.19747 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ccf5c3c-5f9b-343a-b62e-73e7a9947fe3 | -16.09461 | -50.21946 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 53454638-ac9e-3b50-8be8-2bef0e164ee9 | -16.09411 | -50.20104 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6d6e3bb-b9b5-39bc-aa41-9ffbda6a62d9 | -16.09356 | -50.20461 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1f77b578-6ad9-384d-adb7-b78ff0394cbf | -16.0925 | -50.18979 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c018f33-07a4-3494-866a-abbbb063874e | -16.09243 | -50.21175 | 2024-10-08 04:36:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bff36bd6-2dd5-331d-8c40-98daf6fe7002 | -17.01007 | -49.78025 | 2024-10-08 04:36:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b5efb1a-92f8-3d9c-8f85-892480cc0b0f | -19.00358 | -50.23481 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eca334c-70e0-3989-ad8f-858bee9e3ba2 | -19.00302 | -50.23846 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 560624ef-b875-3b9d-a16d-df29ff8be9da | -19.00245 | -50.24211 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ab0269b-51e9-3ac5-814e-0411257f453c | -19.00189 | -50.24575 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e593cdc-a68c-365a-954c-295a943b1d71 | -19.00026 | -50.23426 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faeb46fb-060a-34ae-abef-5d77be81eff4 | -18.9997 | -50.2379 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b8a3002-ebef-3ceb-b158-43700350b59e | -18.99914 | -50.24155 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f52c38b4-7d9f-35d6-a68a-cd8024c9d34c | -18.99858 | -50.24519 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73624b03-d603-3e88-9a32-25bb9906ad31 | -18.98594 | -50.21685 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e457d6d6-7077-320b-9b0c-b0fef74f7d2c | -18.98487 | -50.20169 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc98c89e-ba49-3e61-bf29-c371253299b9 | -18.98431 | -50.20534 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaa2465b-e36a-3e73-b7a8-f90643e4505a | -18.98156 | -50.20114 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ea11e6d-a499-3f6b-b67f-c305e7800e7a | -18.981 | -50.20479 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9031731c-3747-3280-8ea7-ffe4c6c28580 | -18.98044 | -50.20844 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7126a6e6-ce91-3141-aa89-f857a3ea5d34 | -18.97712 | -50.20788 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fde23d90-f43b-3119-b48d-ce399d1c4e2b | -18.97309 | -50.2783 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ebc7d03-367e-3519-b30d-297fd6f5169d | -18.95546 | -50.26034 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cea52b7c-f684-3afe-82ea-dd15642abe4d | -18.92336 | -50.22544 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f18526cb-ead0-38e6-a696-8da2d2c91ad3 | -18.92224 | -50.23273 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be0f5b68-b96c-3fc3-a695-7127e50ea696 | -18.92168 | -50.23637 | 2024-10-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0b5a065-7051-33e9-86a0-768479e4e6b5 | -18.28929 | -50.5428 | 2024-10-08 04:36:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6c4f7c4-d8cc-3f32-a63f-4be5254e6af0 | -18.28655 | -50.53862 | 2024-10-08 04:36:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e52003ef-b324-3b05-88d2-c5b67664e3eb | -18.28599 | -50.54224 | 2024-10-08 04:36:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fea310b1-0405-3dc4-ae42-dd8010bb594c | -17.66622 | -53.02346 | 2024-10-08 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 00e06f41-f060-3edf-ad10-ca0bd594a905 | -16.20688 | -50.92705 | 2024-10-08 04:36:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cc8c460-3535-3bc3-ab0a-49aef119e3ce | -14.16606 | -50.2356 | 2024-10-08 04:36:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bcadde4-dde2-3f97-8166-b5f8efb0b5d8 | -16.8108 | -51.25497 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 571a6a23-060d-38cf-a969-df6344b86929 | -13.89044 | -51.28225 | 2024-10-08 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01adc86a-8446-3076-a930-6f3285a7ed40 | -13.88982 | -51.28596 | 2024-10-08 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 568bfbcd-7b10-3f55-93b4-6d008da79065 | -13.88644 | -51.2854 | 2024-10-08 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43df33db-9496-3e04-a517-967a17eb8c3b | -16.64663 | -50.60295 | 2024-10-08 04:36:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e4963b1-02e8-34da-af76-3a3905e87539 | -16.45892 | -51.8063 | 2024-10-08 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb05ee84-b73a-306e-ab3b-7b1a8d783dca | -16.41362 | -51.89102 | 2024-10-08 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 760ca649-ff26-32ce-bf01-b847da5603ca | -16.41088 | -51.88659 | 2024-10-08 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c9c041a-acc0-3c97-b91a-74747b544623 | -16.40749 | -51.88603 | 2024-10-08 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17217e91-a0ce-341f-b2f3-c0f0cd8f88ef | -16.30546 | -51.45427 | 2024-10-08 04:36:00 | NOAA-21 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de453be6-c3fe-3622-9b74-6c0d48d706c8 | -16.30486 | -51.45798 | 2024-10-08 04:36:00 | NOAA-21 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8392294-b3c0-33af-b78e-7590c7ab2b5d | -16.30271 | -51.44999 | 2024-10-08 04:36:00 | NOAA-21 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dcb6d0eb-6cb7-3531-9608-06856683c0a4 | -16.30091 | -51.46108 | 2024-10-08 04:36:00 | NOAA-21 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa8b10d7-f354-3392-a042-22decf5f0147 | -16.06625 | -50.44212 | 2024-10-08 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0b6dfb1-2ca9-3c3b-bc35-4cf1953c1e30 | -16.06294 | -50.44156 | 2024-10-08 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b3b7091-6ffb-32ae-b180-d8d57047f1e6 | -17.36287 | -52.00162 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6cf0d0f6-6d05-399e-b5d5-51df81883f79 | -17.36225 | -52.00538 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0e535823-276e-3ba1-ad9c-95aaa2e5073c | -17.35888 | -52.00477 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82b65d76-1d31-3449-9433-aeb2cbae01cb | -17.24858 | -50.71312 | 2024-10-08 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 634c85ba-6c46-3830-98a0-a2de3abe865a | -17.248 | -50.71672 | 2024-10-08 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a286d0a-4300-39ae-ae07-0b241824db27 | -17.2447 | -50.71615 | 2024-10-08 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9362025a-0ebe-39ca-9a1a-672f2f913fe1 | -17.24413 | -50.71975 | 2024-10-08 04:36:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17b14bf3-eadd-33c8-9819-50d29fce92b7 | -17.16514 | -51.69819 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f3047545-2fbc-3a77-8dd1-6292f93005f1 | -17.16118 | -51.70131 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c039120b-1bf1-3625-88df-5ebbb92ea30c | -17.16027 | -51.68573 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7754921-7381-32a1-9f25-5a31cb385811 | -17.15966 | -51.68949 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb25a2a4-2beb-3b6f-8f4c-f02373e3a75b | -17.15905 | -51.69325 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d8bb3a3-5572-3e8e-ae73-7f45950447d3 | -17.15844 | -51.697 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3d2ab84-e4b4-30f1-94bd-24b73bd0de51 | -17.15783 | -51.70072 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a63fa61-52e0-331e-9f64-98d767d1b546 | -17.11814 | -51.98603 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16692f34-6157-3942-a5a9-1e1da01fe834 | -17.09635 | -51.15415 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fc7f46d-375c-36ce-82f0-ec8fa88df7cc | -16.81413 | -51.25554 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6f31d15-6828-3fd9-a8a0-36c365bf5a1a | -16.80798 | -51.25422 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 304b37cf-b543-3651-b10a-8fae986cd2e4 | -16.80523 | -51.25 | 2024-10-08 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a546faa-388d-3d62-ac28-9905430c1c40 | -17.99163 | -51.61812 | 2024-10-08 04:36:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d27f3e5-aa90-3f91-b5c8-a4dbee0e3664 | -17.9877 | -51.62122 | 2024-10-08 04:36:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 850aebf5-3368-3f39-bfb5-e3d46fc30682 | -17.98437 | -51.62062 | 2024-10-08 04:36:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d6e0df2-d4c9-3bda-84b9-ce7dd595948e | -13.13588 | -51.65828 | 2024-10-08 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4f41871-234c-3325-a11d-7cd877dd98fd | -13.13496 | -51.64231 | 2024-10-08 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77d65051-f77c-37c7-a32f-ee41858186ed | -13.13025 | -51.64941 | 2024-10-08 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ebddc7f-6b91-3688-bc4d-ffa72fa08edc | -13.12743 | -51.64496 | 2024-10-08 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb09da2e-855f-37b3-8e02-2ad9f25e642f | -15.92556 | -52.2437 | 2024-10-08 04:36:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e82bbca-d08d-3298-b514-ee6c17c09303 | -15.92278 | -52.23918 | 2024-10-08 04:36:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5c8a259-feaa-3876-99e5-43abbcba5099 | -17.84326 | -53.76844 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ab04973-1f0c-3e4e-8865-cbcf05c69fcd | -17.83894 | -53.77197 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00f48454-8113-3c2f-922f-c2b2b435b4f7 | -17.83611 | -53.76696 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b297373-b0ab-31e3-8c01-af1b8062ea06 | -17.83536 | -53.77125 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e1ddc43-58a5-3d3f-b053-5706d89f43fd | -17.81466 | -53.76257 | 2024-10-08 04:36:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README64.md)
