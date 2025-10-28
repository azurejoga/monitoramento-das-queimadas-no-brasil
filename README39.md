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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57727368-0c93-335f-b9d8-3a92ddd99899 | -15.159 | -46.58771 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bfb19eb8-c882-399a-97b2-678e75e3675e | -14.3188 | -44.69275 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 214dd76a-2561-3951-addb-bbd38e1f4658 | -14.55814 | -47.98209 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 825e37db-9172-39a3-b99a-5f24526fb452 | -13.88784 | -48.49829 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f66514d-ac1a-39cd-84fc-80ab002d19e5 | -13.94305 | -43.80086 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 364977fc-9843-33c9-86b7-76a1ad39846d | -13.78863 | -44.34123 | 2025-10-28 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| baf4e0cc-103d-34d4-b040-f76fe4a4e964 | -13.67236 | -46.51737 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65d10783-b5ee-3294-bc4f-d05e239f9029 | -13.78149 | -44.36543 | 2025-10-28 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 315ff9e4-a332-3a23-9123-bd2c82423311 | -13.90852 | -43.89421 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79d76320-1243-31cb-a500-87c398e63354 | -13.18512 | -48.44548 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eb6b841-c444-3681-b5d4-cbe36af019ae | -14.62782 | -48.43631 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdf363a7-97ad-3f91-a707-18ab3c1e67e1 | -13.56014 | -49.58657 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ab1047d-6593-36a2-8f8f-e1a874b7f68c | -15.3128 | -48.05415 | 2025-10-28 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32443d73-d7cc-3946-bda3-4db783fac438 | -14.06626 | -44.08436 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc25295f-04b7-3d0b-8750-ef637b09c331 | -13.79789 | -48.66219 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e77d377b-6530-316c-b296-6a8e2dcdc2fc | -14.5402 | -48.00109 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8b967c0-38a1-3483-ad8f-9945845b0b4e | -13.13776 | -48.24416 | 2025-10-28 04:17:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c7e9855-5e35-3ec2-817f-497f98050e6b | -16.8233 | -43.11042 | 2025-10-28 04:17:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7079851f-08a7-334c-9e5e-a318100ab45d | -14.62991 | -48.44595 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7d2e639b-373b-3a1b-a493-2e86fce8c34a | -14.42719 | -47.85174 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bba17107-5c3c-3a69-8605-41f905c17bf4 | -17.62539 | -43.99558 | 2025-10-28 04:17:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d930bed-054f-3965-8dc4-71896aa5aafa | -13.62602 | -47.03463 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3eafce60-7cb7-3b7f-b037-80999ca17db0 | -17.27048 | -45.2847 | 2025-10-28 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 555c854e-b9e3-3b82-b1ee-6d16d4fa7e7a | -14.64487 | -48.40306 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8060ba5d-3148-3d84-a4b7-48a0b551352e | -13.91129 | -43.89832 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2242747f-2d07-3815-84ee-5d6a4cd5d667 | -13.62762 | -46.47087 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be7dff76-ee69-3ff2-bd88-458e85fefd41 | -13.30787 | -47.0776 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69b24187-f070-398a-86b8-657b7e2e3c1f | -13.90302 | -46.6537 | 2025-10-28 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ed1fae5-28a2-3809-a490-7acf492611a7 | -13.53841 | -47.17415 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e5dfce8-ae4f-3b36-9b81-885746c5c8d2 | -14.02582 | -48.7382 | 2025-10-28 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a239d008-f6d1-3eb0-8878-a07c11418834 | -13.73673 | -48.4324 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9f401f1-5143-30a9-ad38-b94c10095735 | -16.09302 | -46.74824 | 2025-10-28 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8926f072-633b-3460-8e27-1712df2139c8 | -13.62649 | -46.79547 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22cbf6f7-7fb3-3de0-bc70-87b7fded1b18 | -15.62024 | -43.67032 | 2025-10-28 04:17:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f04582ee-60cc-37df-9068-8f94b5fd51fe | -15.22998 | -47.94115 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f14128d4-32a7-39b6-b215-b96405f603cf | -16.70942 | -42.87798 | 2025-10-28 04:17:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff83fbba-b74c-343e-bd10-63f6c7aceed3 | -17.98289 | -42.53119 | 2025-10-28 04:17:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2849f4d8-4015-3d14-adc8-6ef542d4368b | -13.62731 | -47.02678 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 56.5 |
| e3f1b535-e31f-3d8a-96ea-b46ff66a500f | -13.36359 | -47.39222 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44b64324-9670-34b2-8c08-e8f8fd37c059 | -13.72309 | -51.45916 | 2025-10-28 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 01c7ac2d-eabc-3199-b27a-e25ba31849e7 | -15.31419 | -48.02414 | 2025-10-28 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 632f6c8c-4a7d-3961-9a59-6f7354eb5c71 | -15.14979 | -46.60151 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 950537d5-f0f5-3537-8003-fedc737f7cb1 | -13.73865 | -48.42983 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f3f0100-bae8-3422-87bc-b5d6a97ec0f9 | -13.26263 | -47.73248 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36202f38-7418-3e26-af18-5613e35a06fe | -15.17042 | -47.21808 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89065444-4b42-3f86-8e60-11f729d2aa47 | -14.48247 | -47.9296 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f69c8b84-f11e-3df6-84b9-04c0e41f3cde | -13.487 | -47.45734 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fca96d06-ebaf-398e-9f70-02b2c609e1b9 | -17.1656 | -42.33685 | 2025-10-28 04:17:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98f28dc5-2329-38a5-8156-072c701a50de | -18.74984 | -43.70133 | 2025-10-28 04:17:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01d0949b-8415-3905-8d90-cd8ab43611ca | -13.36362 | -47.6714 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f40e1ca5-81c5-3cd1-99d9-83a668a73e0e | -13.23319 | -47.73182 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec71e3cd-9f13-3a94-b4bc-c608c07eb29b | -13.63016 | -47.03111 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a24dbb07-bf55-30df-8c4f-2c14b533c5bf | -14.54024 | -47.97906 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89220138-2022-3061-8232-e0e2b75fa48b | -14.68069 | -46.35037 | 2025-10-28 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 663d3622-945f-36a5-a0ea-d8208bfa38e4 | -15.31347 | -48.02841 | 2025-10-28 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04756857-d437-3407-9ba7-32b825c8b705 | -13.67298 | -46.5136 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cb2d3a0-ab7f-3c10-9e89-bbaee424f5cd | -15.23212 | -47.95016 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75fdede6-0387-361d-84b8-ee93823b3bdb | -19.02991 | -42.02696 | 2025-10-28 04:17:00 | NOAA-21 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| bd3d667c-2ff9-3363-ab05-ee2e8b3146bf | -13.21799 | -47.09167 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1021852b-4ceb-3eb5-ac44-cf544bdb5c29 | -13.5581 | -49.5751 | 2025-10-28 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 451d4c01-b3b8-3270-9c73-0b2d44befb8a | -14.45575 | -44.48985 | 2025-10-28 04:17:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb6c3b84-439b-3f53-bcc7-6e0296d9acfd | -13.56209 | -47.16135 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41473a90-2dbb-3ffc-9337-fbd92e254911 | -13.86898 | -48.51905 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a3d46eb-e14c-33ba-955b-69c1f20317b2 | -15.20674 | -47.21245 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 164c0192-fb8b-352f-81f7-36d7f7225fb1 | -13.88204 | -48.48774 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d0c53ea-c6fd-37dc-a359-6c03f602d26f | -13.63648 | -47.03601 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| fc42aa8e-ac5d-3c90-8d31-70b123effa01 | -13.73395 | -43.99094 | 2025-10-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22ac0e12-123b-3f40-b623-c969e4db2712 | -14.58533 | -46.26639 | 2025-10-28 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1664cd1b-e717-3559-820b-fa404cd06932 | -13.31463 | -47.6862 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da901474-fc58-32e4-904b-b28742d14b25 | -14.1539 | -44.24413 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 318c19a3-3e26-3966-9f28-0f563e14bce1 | -19.02185 | -42.03041 | 2025-10-28 04:17:00 | NOAA-21 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7112966-a641-3309-a160-90cff89c95bc | -14.53086 | -47.99094 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30da3822-7a9c-3365-bf93-89d7de8cc38e | -14.31588 | -46.51752 | 2025-10-28 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aa638f6e-9c5e-32ab-9062-6967b2ba5ca0 | -14.15059 | -44.2436 | 2025-10-28 04:17:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1a6cc1e9-24f0-3455-9707-7fca9b9f69fc | -14.62067 | -48.4125 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06504ec5-034f-31de-a65d-8e73a6ec3530 | -14.67611 | -46.35723 | 2025-10-28 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51577b55-e6cc-3061-a64f-16f78be0bae1 | -15.22644 | -47.94048 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64f96177-b39a-3c1e-a945-51955f840c58 | -14.53593 | -47.98276 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1461836a-f2a4-32e1-aad8-d61a3b0b0767 | -14.76103 | -44.95482 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b9976d2-93ac-3741-9a95-35813ea3441a | -17.26992 | -45.28829 | 2025-10-28 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efb947f8-080a-3743-aa31-32ad6b04499d | -15.20949 | -47.21716 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63b97052-036d-3873-ad0f-c0c81973091a | -13.84396 | -49.06091 | 2025-10-28 04:17:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95083d43-340a-3f15-8cd6-db9777cae4f6 | -13.73009 | -43.99397 | 2025-10-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 603c902d-7ea4-3fc4-afab-b4316b01cc5e | -20.65708 | -42.56498 | 2025-10-28 04:17:00 | NOAA-21 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1adf7261-c0a1-3e1a-b08c-28bb8dc28a8b | -14.73857 | -48.16095 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56b7bc3f-0ce9-3eb6-a3f6-be145bac3d79 | -15.71126 | -43.94839 | 2025-10-28 04:17:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a86a10d-0412-3bb9-97cc-d4b5e100aa4a | -15.31635 | -48.05479 | 2025-10-28 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba6ed2ed-37c8-3425-a9c6-6a02c35f960d | -15.9916 | -45.65066 | 2025-10-28 04:17:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 240bf8d6-b07f-3d66-80bd-3c04dfcaebcf | -14.62278 | -48.422 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 406548fe-511d-3010-89c2-5904eb11caa6 | -14.81301 | -46.70273 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fda740e8-011b-3502-8ee6-5b7052064685 | -14.77256 | -44.96763 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1401bbbb-5106-3107-8e22-be1c0a4d119e | -14.42783 | -47.84797 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8ad43d0-535d-3276-9e09-747cc31f6c46 | -13.3679 | -47.66788 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0c60ce5-4294-31b0-b7a8-2733773bc8d2 | -14.76378 | -44.95891 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d26b6369-674f-382f-ba24-ea789529d7d1 | -13.53712 | -47.13939 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b1cd7339-6e2a-3622-ad1f-eca9528461e5 | -13.3888 | -47.35061 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7099f1a-84c8-3327-abde-964761620fe9 | -15.22929 | -47.94524 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffaed0e2-f887-3399-8af5-411a2a058c72 | -13.79726 | -48.65875 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 619a7816-3f0e-3d2c-adcd-8a904101a21d | -13.319 | -48.34721 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ac75c02-e13a-3b91-9e94-3a08e2d1474b | -18.24827 | -44.18976 | 2025-10-28 04:17:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
