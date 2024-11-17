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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2176d927-26a0-3787-a25b-99311850752c | -3.18565 | -53.25307 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6799234-7b55-3d88-8e44-ae178c43f241 | -2.67042 | -46.20432 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c464d0ee-6723-3eb9-b6d1-39c9d701530a | -2.13543 | -46.49649 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee154337-2380-3d6d-9140-3375a1e97ccb | -4.93139 | -40.8402 | 2024-11-17 04:06:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 87a78428-4186-3502-8ffd-6780a69272cf | -3.35045 | -46.42888 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 271bf434-2843-3bf6-86cb-238211b89452 | -4.09402 | -47.81451 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d5a04b6-61b6-3a74-ad6a-b30d0ea4268f | -4.09722 | -48.18341 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ced95149-cb75-3b23-9d0c-1cce233aff24 | -0.89969 | -51.74118 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dc6cfb1-035b-3cfc-9692-d5d4395851bb | -11.65833 | -39.83908 | 2024-11-17 04:08:00 | NPP-375D | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1f272a9-22a0-3328-9f88-713dd395ab71 | -8.43549 | -44.20993 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab8aee43-2590-3756-ab9b-eae423a68e19 | -11.7208 | -44.08395 | 2024-11-17 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 038be09a-1e4a-34ff-bc4f-536d42fd7b13 | -12.44206 | -43.79545 | 2024-11-17 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c5430ce-2c17-3efa-93a1-c2b7609fb1d6 | -8.44374 | -44.20333 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 796fa068-a97e-357e-bd9e-ab6721bb0e64 | -11.85453 | -46.93737 | 2024-11-17 04:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca8bf854-17c0-353c-8269-5a13e11822c9 | -11.18121 | -44.62299 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30771b8a-7650-3d4a-b1a2-b5724c9e411c | -8.45198 | -44.19681 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e12fad8e-852f-36f2-86d9-3fa68f3879e4 | -8.44786 | -44.20006 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2e5c0fd-5c5d-35ae-82e5-dd4cf0560523 | -10.66325 | -44.4989 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| da68d1c1-e744-3188-98de-4b2d2fee2730 | -10.66388 | -44.49508 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dbf1340e-1d05-343b-a1d1-0d67dfb824e1 | -9.86833 | -47.53194 | 2024-11-17 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e394477b-15ca-31ea-bf20-ee2fc5c7af3c | -13.59105 | -43.18717 | 2024-11-17 04:08:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7733f2cc-087e-3d01-af34-54655453ec0d | -11.10073 | -45.34645 | 2024-11-17 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57c09dc9-82b0-3b0b-bb0b-e7b0dcb49c5b | -10.69475 | -38.27794 | 2024-11-17 04:08:00 | NPP-375D | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a294ba02-365e-3a9a-b65a-c963ff0c2938 | -10.69589 | -37.04984 | 2024-11-17 04:08:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 038f863b-f901-3ea3-b981-1a8ee95e7d67 | -11.56923 | -46.00375 | 2024-11-17 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb4cac83-3138-33c3-9c18-7dc58839e388 | -8.4485 | -44.1962 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c112f8e2-9c34-3a96-be6c-592151959695 | -9.86485 | -47.52748 | 2024-11-17 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0723e475-5ef6-33c9-a00f-7d5e2e347d93 | -10.69241 | -44.9122 | 2024-11-17 04:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d60437fb-6b99-3bf7-a412-00af93ad4bda | -10.81955 | -44.92834 | 2024-11-17 04:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d156b080-5645-3acc-b387-0cc554b79730 | -8.44153 | -44.195 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cb78327b-3d63-3e29-909a-a34b36b777cf | -12.43871 | -43.79489 | 2024-11-17 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 676d2b54-bb64-3d39-9d52-37362a70e648 | -10.69856 | -38.27849 | 2024-11-17 04:08:00 | NPP-375D | HELIÓPOLIS | BAHIA | Brasil | 2911857 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0525d08e-78fa-3818-a59a-7675c6dafcb3 | -10.68274 | -44.01999 | 2024-11-17 04:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 436a8b64-07be-30fc-ab47-d24cf2d0a682 | -11.16227 | -45.1069 | 2024-11-17 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1ec30ff-5c9b-3362-b399-aa3c9b868105 | -8.44026 | -44.20274 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 355e23bb-b020-3f08-b70c-924085d22472 | -12.26984 | -44.98322 | 2024-11-17 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6116901e-623b-3301-a8b2-81b9972448b0 | -11.1594 | -45.1023 | 2024-11-17 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6efcfac4-2a2b-39c4-888b-dd587c95dbb8 | -10.72943 | -40.52243 | 2024-11-17 04:08:00 | NPP-375D | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 35128840-7bf6-3016-881f-79e0c6a8a3c5 | -10.66734 | -44.49566 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cffcabb3-1a31-3b07-88ce-8560bf5c55eb | -11.1239 | -44.5707 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d863e1d9-eddd-3368-bdde-192dd2aaa025 | -9.86896 | -47.52824 | 2024-11-17 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb542c36-21dd-36e6-a6e2-e19d8abe56f3 | -11.18185 | -44.61916 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0b00fbf-17de-37cd-9196-3efe30716b24 | -8.43962 | -44.20662 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7a309ffb-5d73-381d-8697-f02f29aeb659 | -10.38348 | -44.87878 | 2024-11-17 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfbd763a-8478-3484-a0ac-088eedc167e2 | -11.12453 | -44.56689 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4b67e95-865f-31eb-ab38-1cc575e2094d | -8.44247 | -44.21111 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 98a56992-3c72-397b-adc0-ed311aa5253a | -10.54039 | -44.67418 | 2024-11-17 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a354d62-9550-3110-8c62-f688a88c4354 | -10.83473 | -42.73075 | 2024-11-17 04:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 18d9b44f-f178-372a-91f7-f1ba4a46ee1f | -10.81603 | -44.92775 | 2024-11-17 04:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be6a8e7c-2886-3018-a740-3f3d31045e7c | -11.18467 | -44.62356 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fab6e83-20b4-34d2-9ea2-cf7af38a0b4c | -8.44977 | -44.18842 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8e5d1ce-6717-3e5f-855e-9c5d009486e3 | -8.43898 | -44.21052 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2847da96-9058-3e33-ac96-863d5d76ef47 | -8.44501 | -44.19559 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 06b73174-5a1f-3d4c-9ba2-771b510b8b40 | -10.37996 | -44.87819 | 2024-11-17 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b8a0364-b9f0-3d8a-a1b2-8372ab9215c4 | -8.44659 | -44.20782 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20027842-7d7c-3e35-9a0f-1e3218649018 | -13.04928 | -42.58992 | 2024-11-17 04:08:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63a3c5ae-5c36-3739-9d20-798cf09a98ee | -11.85185 | -46.9392 | 2024-11-17 04:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 46a63691-dc53-388f-98f2-1236a0fa8e8c | -13.46059 | -43.05267 | 2024-11-17 04:08:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dbc4d79f-d29e-3bb8-9b23-d8e0f3a3f9a8 | -8.44565 | -44.19171 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c79b3c6a-4f05-3c39-9057-4d87f348f89d | -8.44438 | -44.19946 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb55c4fd-9c6b-3481-9b71-b674111a6557 | -10.54388 | -44.67476 | 2024-11-17 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4979cbc5-1ee9-3c60-a3de-9394a62864f9 | -11.85068 | -46.93671 | 2024-11-17 04:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 35424527-928a-3866-9c86-c4378c0428d0 | -10.42151 | -44.71492 | 2024-11-17 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55718872-f3fa-3c06-83e6-d53bf7d7cf84 | -8.44311 | -44.20721 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc953d54-c88b-3c60-b624-217a34867b29 | -11.95203 | -43.15082 | 2024-11-17 04:08:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 66f211ca-3d3b-391c-9d95-a9466c254199 | -8.5022 | -43.91118 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b6689cc1-5454-3a01-8d7b-4496146a0451 | -11.09706 | -44.71251 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d600e50-4585-3044-aa89-1f5e73db12f2 | -10.66451 | -44.49126 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 440c962b-fee9-3087-aeb3-26344d4bee3a | -14.95887 | -42.2629 | 2024-11-17 04:08:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 390a95bc-014c-3761-8b85-4be8d3fa074f | -12.27201 | -44.99175 | 2024-11-17 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 386d8e63-04e5-3d71-8a85-464fc5ef88e4 | -10.99564 | -49.35853 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36872637-d9c5-3bb1-847a-811642ad35e3 | -10.41323 | -44.96181 | 2024-11-17 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db96e14a-6d6f-38e5-bda0-9bd4488a04c1 | -8.4409 | -44.19887 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fb5c2767-1254-3657-acf4-e77fc78a32b9 | -10.77308 | -44.42696 | 2024-11-17 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4faf99ce-164f-3778-b3b1-492b7c0e7ca0 | -12.26637 | -44.9826 | 2024-11-17 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f27218bf-dac0-35e5-852f-6e79933f90f2 | -13.47067 | -40.06448 | 2024-11-17 04:08:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b77ca86b-af59-35c8-84dd-3819953fb166 | -9.36951 | -40.34062 | 2024-11-17 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eef3f7b9-c29e-3df3-a844-0894290b7986 | -11.15874 | -45.10629 | 2024-11-17 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05fb261e-173b-38d5-88dd-ac78ed5d3d5f | -12.27266 | -44.9878 | 2024-11-17 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdeb141b-6294-312b-a920-f5bff1722a24 | -9.9334 | -49.09779 | 2024-11-17 04:08:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea2d35f3-6e06-38e9-bcca-605d59a39cc8 | -11.56959 | -46.00562 | 2024-11-17 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1464ff28-122e-3f93-80ba-8c8fb25d63c8 | -8.45134 | -44.20068 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1786f0b2-e18e-3731-91e3-ea7fd06b7e5c | -9.86075 | -47.52673 | 2024-11-17 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff789263-5ec1-3a76-b122-b526bfb97af3 | -9.86422 | -47.53118 | 2024-11-17 04:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99d7381b-3c41-3335-bc53-76bda04e346a | -10.131 | -49.14882 | 2024-11-17 04:08:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0515f92-1f89-3043-802b-a33a049b8dd0 | -9.53166 | -43.05245 | 2024-11-17 04:08:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4683d675-6746-3d12-9c23-cfda762952fd | -8.43613 | -44.20603 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59e322fd-7b24-3a1a-9740-5ce68874a063 | -8.44217 | -44.19112 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 17a82959-1903-3e59-a257-167811a0aa4d | -8.51537 | -44.94749 | 2024-11-17 04:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9003915f-063c-3332-a47d-bbcc471cf7fc | -8.44629 | -44.18783 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38028ab9-d92f-3feb-b2a1-4ae3a5e94fe8 | -8.43834 | -44.21442 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdb1ce6c-11ce-3d4c-9658-f04e8afa1f03 | -12.38986 | -44.60936 | 2024-11-17 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 209aade7-5404-35c9-8a15-da081bae5212 | -9.43016 | -43.59793 | 2024-11-17 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 734053cf-3402-32c1-a924-631f0f0aa663 | -12.2692 | -44.98711 | 2024-11-17 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1ba9534-ce87-3d17-8647-8744b8e3e58f | -12.17914 | -38.81108 | 2024-11-17 04:08:00 | NPP-375D | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21c54727-6d6d-3433-855b-634907efdc28 | -8.4428 | -44.18724 | 2024-11-17 04:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c2b77f8-1b2d-352e-b580-5e6303adb5e5 | -2.6322 | -48.5634 | 2024-11-17 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c5b1764e-92e3-3b82-be31-a8daf0df5fb4 | -3.5124 | -50.2553 | 2024-11-17 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| cd0f9aee-7bbd-30a9-b67b-9341ceb978ce | -4.5616 | -47.9925 | 2024-11-17 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cf4e9e51-6e84-3550-adee-9d4127eaaf65 | -4.5614 | -48.0141 | 2024-11-17 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |


[Clique aqui para ver as próximas entradas](README36.md)
