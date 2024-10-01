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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94e222f3-d387-3fc3-850c-a10f12b5c92a | -7.59658 | -43.86601 | 2024-10-01 04:12:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c2d39c1-a418-30e0-9b7e-fe06419699e1 | -7.56357 | -43.86082 | 2024-10-01 04:12:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4630ad03-3295-33b5-a5a9-f8e7c3dd957a | -7.50053 | -43.91518 | 2024-10-01 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df89a6d6-7a18-3b3a-bf41-54749db5e189 | -7.48395 | -43.86964 | 2024-10-01 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8547e74b-bf2e-3508-b109-aa5cef744afa | -7.47346 | -43.85008 | 2024-10-01 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2caf4800-b3ac-30ef-b4d2-87afbec5d784 | -7.4729 | -43.85357 | 2024-10-01 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba0cf5f6-c5b0-3a90-9f74-8aa4a65ba9ea | -7.40824 | -44.04733 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 024e36eb-232d-323d-8427-045cbb9e486a | -7.32169 | -43.822 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c8ecd9f-eeb9-369c-b980-bcbc4d94f4b8 | -7.31782 | -43.82497 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c546cde-da26-3b13-833b-f7421911dd87 | -7.31451 | -43.82444 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4efff0d-8109-3061-8b89-fbc2b8320dde | -7.3051 | -43.84085 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0a88548-5c65-311b-9553-4c26dc87b21c | -7.29957 | -43.78992 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f76633d8-378f-3563-8169-3760fe444c0e | -7.29902 | -43.7934 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0860b8ce-1dcf-38f0-a8f8-5a1fee1ecb82 | -7.29847 | -43.79688 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd5230b2-1687-3233-83c0-32cc9451dcbe | -7.29515 | -43.79636 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9af23527-e033-3c20-afe7-cf9c3c072b25 | -7.28574 | -43.85564 | 2024-10-01 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88551d92-56cc-3564-9c22-141bb03e05b1 | -7.13384 | -44.10491 | 2024-10-01 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b644a6e0-ecff-3875-a7a8-98ec68a6501b | -7.12994 | -44.10792 | 2024-10-01 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b055970-1f28-3b8d-a958-3aaa81e160a4 | -7.04305 | -43.95008 | 2024-10-01 04:12:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e726ca39-c473-34e4-8700-e2c3da58f6d2 | -7.03973 | -43.94955 | 2024-10-01 04:12:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f04b384-e35a-3382-8d17-1708805c8915 | -7.79241 | -44.17326 | 2024-10-01 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e8d2de0-a9a3-3aaa-bfcb-2ff4e8017411 | -7.78964 | -44.16922 | 2024-10-01 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2235b6e6-0abd-3e09-ba9a-338c38e35bc3 | -7.78631 | -44.1687 | 2024-10-01 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79dfbadc-da82-369a-aec5-cedcff4769db | -8.76145 | -45.12877 | 2024-10-01 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63fe38f3-fc31-36a8-ba29-dd72d50f4939 | -8.75748 | -45.13187 | 2024-10-01 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c9331f1-074a-3b03-9ed6-9b3480db8889 | -8.75689 | -45.13554 | 2024-10-01 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd5ea8fd-e7fd-3352-a519-8056ffd9ebca | -8.75292 | -45.13865 | 2024-10-01 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa4f8de-2482-3a96-a1df-1e3c109c9f0c | -8.74054 | -45.21569 | 2024-10-01 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6d8f465-5a10-39ca-8e36-3af60f679668 | -8.53409 | -44.71781 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c747b927-7512-3a6e-aac9-bc85669af68a | -8.53351 | -44.72139 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d66361ab-2cf0-343f-9b37-f9fdb9d860f9 | -8.53247 | -44.70652 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d35de1c1-502c-3f3c-850b-41bfdd316c0f | -8.5319 | -44.7101 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c54a7d29-a009-3227-8773-4d5136acbbb9 | -8.53074 | -44.71727 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9878f17a-fc5d-364b-bd4b-a0d8303110c1 | -8.53016 | -44.72085 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b917f838-e10a-31c6-a15b-98d33665be51 | -8.52912 | -44.70598 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| caab3a39-9ca2-3aed-ac01-da68965095aa | -8.52854 | -44.70956 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b84735e-69f6-3637-960f-c4178d07154b | -8.52707 | -44.70587 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2ccd757-5d9a-3e05-ae7d-a959ff4b9918 | -8.52651 | -44.70946 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2fed728-0acf-39e1-8a2a-ac578d1cdb6b | -8.52623 | -44.7239 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 985acc06-3828-3573-a9c4-f24f4ecd72f9 | -8.37128 | -44.80619 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 680e6b0b-9123-34ea-bdeb-65ba7d92cedc | -8.3707 | -44.8098 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c94109f-eeb2-3979-a519-111083a107af | -8.32321 | -45.34668 | 2024-10-01 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3fdffe4-8726-3567-9cb5-60c3afa1164e | -8.32104 | -45.3385 | 2024-10-01 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebd304ba-d94c-37e2-a735-a8685116c709 | -7.96629 | -44.9946 | 2024-10-01 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c420cd85-b009-3177-b946-560b0c4cc4a1 | -8.64367 | -44.05505 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0278837-52ee-35fb-9e5b-edb877e9d10f | -8.64311 | -44.05854 | 2024-10-01 04:12:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ced7eb0-17d4-3927-a360-cb45905e4980 | -9.87208 | -45.66019 | 2024-10-01 04:12:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2a80808-c411-35f4-aac3-8734c9f52cfd | -5.98377 | -45.36963 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| fc7c9705-2dbc-392e-aeb3-3728ddd1d94d | -5.98314 | -45.37352 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d9e8e3ec-65b8-395e-9dc0-6932267dcca0 | -5.98028 | -45.36908 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c78e9227-bd42-3b7f-a939-ce4b5adf57c5 | -5.97965 | -45.37296 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 80369061-b703-37bf-9bf5-49a6a3f47f18 | -5.97902 | -45.37685 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4a72aee2-b4ab-3021-8d20-c1e3a2bd1ea4 | -5.97615 | -45.37243 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6902de76-6c42-358d-b327-bed19be4306a | -5.97552 | -45.37631 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a30da6c1-4010-3792-8aff-94eeed63692d | -5.9749 | -45.3802 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 66bfb3b8-666b-3299-adb9-8323eb984fa9 | -5.97265 | -45.37188 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6e0403b-2dec-3274-838d-3ebc0c827383 | -5.97203 | -45.37577 | 2024-10-01 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ebce694-5951-3608-bf40-f74d06f194e5 | -5.84747 | -46.23553 | 2024-10-01 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 215204c5-15af-3234-9ccb-edac6d13acbd | -5.77326 | -45.5517 | 2024-10-01 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3dcaa87b-3311-3437-a820-7531e878d6ab | -5.77262 | -45.55569 | 2024-10-01 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfb711e6-a388-3c0e-9631-28378466f817 | -5.76973 | -45.55113 | 2024-10-01 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99d78cf8-6307-3f1f-9d7c-b458fd4cd0de | -5.7691 | -45.55512 | 2024-10-01 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a72c67c0-7116-3db2-8261-d9d30d75ca00 | -5.76557 | -45.55454 | 2024-10-01 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4bed9db-9e4b-33d7-9092-41d1b70650bd | -7.70342 | -45.42599 | 2024-10-01 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5b2367d-71ba-35bb-a3b0-ecd2ae833680 | -7.70282 | -45.42973 | 2024-10-01 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a584e7e5-08be-3b20-af05-42d1cfb3cf90 | -7.69997 | -45.42549 | 2024-10-01 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43185590-a962-3fef-adb2-91811bb273d2 | -7.60144 | -45.40565 | 2024-10-01 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41446042-7875-3910-8072-757796dc4c0f | -7.25703 | -46.07433 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fca7d19-b5fa-384a-8758-12e8c5f2d4ff | -7.25635 | -46.07841 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d18e19e8-b69c-389a-8507-5ac26f43c7d0 | -6.9353 | -45.60143 | 2024-10-01 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50a67fb3-6fe4-374a-8c97-04721cf2f762 | -6.93181 | -45.60086 | 2024-10-01 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 730ed018-eff4-3c87-9210-f71ee6b9f5ed | -6.93119 | -45.60472 | 2024-10-01 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dca38cf0-dc91-3781-8fc9-df198081a140 | -9.22439 | -45.7184 | 2024-10-01 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0a9851e-7311-3378-bda6-5b96c18d98b9 | -8.93518 | -45.65998 | 2024-10-01 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1149b67a-ff8c-3ecc-9805-d7452c95b786 | -8.93174 | -45.65942 | 2024-10-01 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f74c4884-4a4d-3fe7-925a-8bf8f383be8d | -8.92892 | -45.65512 | 2024-10-01 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02b2f760-de0d-30e4-a61f-e7c3bd84e0f5 | -8.9261 | -45.65078 | 2024-10-01 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adb0d550-7d8c-325f-84a4-8d5ac8d674cf | -8.92328 | -45.64647 | 2024-10-01 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 452161e8-f98a-3ac9-a9f8-8dbbe37a1dad | -8.91984 | -45.64592 | 2024-10-01 04:12:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6c3f50f-6d06-3265-a86e-a1e2938acb15 | -8.07487 | -45.47353 | 2024-10-01 04:12:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ffd8dd0-e2c3-31bc-8a6f-fa9ffba93dc7 | -8.81423 | -46.81516 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dbeb938c-fbc1-3276-a77f-0dd8222e576f | -8.77951 | -46.82244 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d911371-8d32-398e-ad53-aa5ff779408b | -8.77588 | -46.82189 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d76190dc-7b9c-3da7-9ea8-445054886ddf | -8.77224 | -46.82135 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c866205f-8c0c-3183-b804-b356b540d878 | -8.76861 | -46.82078 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bf23707-7dbe-34d4-b688-82567a73337f | -8.75128 | -47.12919 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 922e4eff-dae5-3aca-80fb-6669a678d184 | -8.74686 | -47.13299 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 506b84c8-ea36-39b4-8abc-0af04063dea9 | -8.74613 | -47.1374 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94175ae1-7eb8-353b-ad44-cbfa4a925636 | -8.74317 | -47.13238 | 2024-10-01 04:12:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fd1139d-5a07-3876-b686-aef9b46f9896 | -8.61903 | -46.5446 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 626dd977-8772-3227-a79d-234beab4b423 | -8.4787 | -46.89539 | 2024-10-01 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e84a4423-ff36-38c5-a733-791fda0062bb | -8.47784 | -46.85479 | 2024-10-01 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfb29eeb-b408-3f97-b59e-451203af85cb | -8.47711 | -46.8593 | 2024-10-01 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6adab68a-45c2-383e-8021-0674b3f397f0 | -8.46253 | -46.85681 | 2024-10-01 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0c9296b-502b-3011-9eee-c607eb3c9a1d | -8.4548 | -46.44409 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dea9924b-66fc-3caa-b1cf-022cd9f635e3 | -8.4545 | -46.86 | 2024-10-01 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c451066-c38b-34db-94de-aa75d2369f4a | -8.4538 | -46.86426 | 2024-10-01 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f558192-4d17-35a7-aae0-c58669a20884 | -8.45057 | -46.44755 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eee579b-d3d1-39b8-a88c-816834ec57ff | -8.44991 | -46.45161 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 601a953b-4371-3051-aec3-9e7c205ed902 | -8.44633 | -46.45102 | 2024-10-01 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README70.md)
