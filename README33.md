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
| 6c1bf392-3e88-3d58-9b78-6144d4b78102 | -6.98252 | -47.08379 | 2024-11-20 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43691880-0692-3906-9742-ed343e47f2e3 | -11.04141 | -44.57145 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 1f878e98-68d5-3a69-8ff6-92f06417e564 | -6.63848 | -47.34656 | 2024-11-20 04:27:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 737bc71e-6950-3e28-b803-d5bfffcf6dab | -2.90843 | -48.31567 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 647cc92d-4d9a-3fb7-9271-34241fdd1c45 | -5.20204 | -44.23082 | 2024-11-20 04:27:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51024c35-a2b4-3444-925a-831a0a052d93 | -2.86881 | -54.48032 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 736ae068-4b18-322d-a98e-d1b98f215e92 | -3.36265 | -46.23909 | 2024-11-20 04:27:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c1b5b6c-841b-3a85-8772-b225c86c0ebb | -2.91857 | -53.05682 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c6acbaf-fa68-3d51-a93e-8877da0267dd | -3.91405 | -46.52053 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53d3a883-12d9-369d-9692-277594b6ecfc | -2.61783 | -51.8064 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 494dc6c0-b101-30da-a9b3-9dc56dd3f187 | -4.6991 | -44.46766 | 2024-11-20 04:27:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8921fee6-5e2c-3973-9ae4-d3f6888ce861 | -5.69304 | -45.84325 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36821bcc-bc6f-3e10-acba-e6c8a6d79582 | -3.73013 | -47.37006 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64a4565c-6c21-3390-a29d-f948fa497ef9 | -3.56889 | -47.37438 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1c1132b-5610-3cbe-8dab-9ff9101ea3f2 | -3.81866 | -51.35776 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9160c82a-d65b-396f-ba62-5acd578f014a | -10.42807 | -44.88796 | 2024-11-20 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 615dfa7c-1d1a-3dd3-a42a-3612cba11f78 | -3.18239 | -54.317 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858f4497-8237-3698-aa28-2dd234ffdc02 | -4.09595 | -47.81418 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eff3808-538a-330d-bdf6-3730f558e57a | -5.4524 | -44.82251 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28b1b813-6f51-359d-9f0b-06d5ebd9397e | -3.77909 | -44.06374 | 2024-11-20 04:27:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50d5b1dd-b1b2-33fd-9945-4291e9375ed6 | -2.75676 | -54.06807 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e92ecf8c-2ecc-352b-89d3-35721fea458a | -2.59033 | -51.71742 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a92ca3d-1435-39b3-9a90-580c31c1f08f | -3.88362 | -52.24093 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b6719ddf-829c-3f32-9464-ba193cce0eb2 | -2.84871 | -54.00584 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea51ba00-1a55-3c7a-b050-abab87c7e55c | -3.04886 | -54.40715 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3577994d-af7a-3765-8d3e-17e57f164325 | -3.5814 | -53.71936 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9156e7a8-02b0-30d5-92d6-1f5144d52bf2 | -4.55408 | -48.00544 | 2024-11-20 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75f4b74e-1f5c-338c-b8f7-4cb0187915d0 | -5.87513 | -40.17582 | 2024-11-20 04:27:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d85cc0d-4839-336c-9eba-72f42f82e32f | -2.34915 | -54.78796 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 450d7faf-f583-359b-89ae-4a0a92c64f4f | -3.87923 | -52.24027 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf724f26-c38b-36d5-8ffa-77cdba3bdf90 | -3.85195 | -49.44121 | 2024-11-20 04:27:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b63b380-44b1-3039-8167-c0941a527820 | -2.60683 | -51.79192 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c0f3fd5-8a4c-3fe8-8be9-6c05eae2aa7f | -4.77103 | -46.41476 | 2024-11-20 04:27:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96054d33-4556-3ad6-98e2-08e44adf635f | -3.77949 | -47.48508 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642fed30-5cdc-3834-8b3a-20a0adb02e93 | -3.78591 | -44.06479 | 2024-11-20 04:27:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 138a7f01-6f81-3e27-9ef6-cd947cebddfe | -10.76988 | -44.82383 | 2024-11-20 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac88b4cc-6490-3d28-ad24-4d63ee47437c | -5.59688 | -46.17838 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 676d6b49-6633-399c-8faf-401a0f29daef | -6.53388 | -44.18378 | 2024-11-20 04:27:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2dd787b-aff8-332b-841b-aa1797882974 | -10.21954 | -42.1935 | 2024-11-20 04:27:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 24b05d8c-46e5-358a-867c-ba819ad6950c | -3.88085 | -47.08043 | 2024-11-20 04:27:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b319950-9a13-31d6-9454-b2a447ff79cb | -2.53465 | -54.01138 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f937ebd-f3f4-3112-a739-e092687d0963 | -4.16715 | -45.50897 | 2024-11-20 04:27:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec72401b-6019-3e74-bccf-608fed10df40 | -4.65699 | -49.02232 | 2024-11-20 04:27:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6ecde80-1d46-3e1b-8d77-221e08b0fdcc | -3.84858 | -46.63458 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52c7d301-b87d-34c0-bc12-e52209c4213d | -3.8933 | -46.60952 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dbc88fd-8510-3feb-941c-4a2d5223b19e | -6.57315 | -46.56893 | 2024-11-20 04:27:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ab7aaae-ee43-39ac-b873-be0d4ee9fca7 | -2.58104 | -51.72018 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc880ca9-093c-3091-a16a-bb714624939d | -2.92766 | -53.07075 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 228f756d-aa67-38b4-a3fb-4c76696f02f5 | -5.3802 | -45.44921 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72492b82-f092-3b4e-aa27-e715c69ec8d3 | -5.59795 | -46.17148 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a50bbca5-8555-3438-84b5-be3f0f5a74f8 | -3.72901 | -47.37723 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fac2358-b539-3933-9030-a281c241b4d9 | -4.08134 | -50.03562 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d010754-e26b-3d6a-8b0c-3116cec3aa5a | -3.18661 | -48.57578 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5518b20f-e599-36b3-b641-cd07a7abe40c | -4.9759 | -49.63691 | 2024-11-20 04:27:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb3fa670-e128-3f10-91b4-7b03b9b07edc | -4.15051 | -43.97485 | 2024-11-20 04:27:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 428e614c-5a9f-389c-b24a-17ecaf74e39d | -4.66054 | -45.61822 | 2024-11-20 04:27:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 037e1fc7-08e3-3c18-b702-cea954d15b6e | -4.46835 | -46.58621 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5174465f-1e5a-302c-a80a-60dc15fe43a5 | -4.55514 | -48.02082 | 2024-11-20 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b211a5-9c52-3310-9fb7-48e366a04cee | -2.92864 | -48.32999 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a232c79d-19f7-32ca-894f-6c94feedc9f3 | -7.99976 | -44.37971 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36727251-dede-3ea1-83d4-71f7bd3f3c09 | -5.96272 | -48.06859 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 63b82158-f297-3195-80dc-d2ed7f918906 | -2.9199 | -53.05927 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f373799e-5af5-3f17-af93-65adaceb10a8 | -2.90641 | -51.7736 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0866b7dc-e207-3984-9b3e-e7f633f7b245 | -4.38722 | -47.7729 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1fe3138-9449-382b-987b-ea45236ccb21 | -5.30002 | -43.06907 | 2024-11-20 04:27:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 973630a2-b6b3-3e1b-baf6-8478ac74e5e6 | -4.0778 | -46.73434 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54e69edc-ac97-3c67-a455-37ef69ec3c96 | -5.25099 | -42.64413 | 2024-11-20 04:27:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44bb6758-e537-3192-aff5-8e6dd43f900e | -4.99305 | -46.92859 | 2024-11-20 04:27:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef5eb5c6-6e0b-34e9-91aa-7a4e14773989 | -3.81004 | -47.80368 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 830063bb-52b7-3239-8a1c-399a4bae04c8 | -4.39003 | -47.77708 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc0c4099-a1c7-33e5-9f11-421ab45b41ec | -3.7647 | -52.14032 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75334c3b-e265-3ee5-9fdd-c45e5817888e | -2.91233 | -53.06559 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 34d188ea-9f78-303d-8f62-7ccbcc22c3f0 | -6.53331 | -44.18759 | 2024-11-20 04:27:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 84dc4e8e-b680-30ff-8f63-ca6457d119ba | -3.81345 | -47.80421 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 746b9929-b14b-3559-8142-077e2e6c328c | -3.36313 | -54.09854 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e901d3-5660-3c59-b254-b6834b68f379 | -4.13601 | -53.61002 | 2024-11-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4252c9e2-ffc2-3f54-ad02-e202c4e3d889 | -3.08642 | -54.66534 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72cf1241-e0da-339c-a0bb-5f656af58460 | -6.48179 | -47.49815 | 2024-11-20 04:27:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b5a33839-e53c-39a0-8a03-e9fe15e962ef | -3.88294 | -52.24513 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c810ada-2220-389b-a787-856b58a5caad | -3.36359 | -54.09577 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8201711-83fb-3e7e-8ae5-a7cfe621e6af | -2.6635 | -51.71626 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7faa5c8c-bf51-3136-976a-92886bb34bc1 | -2.93917 | -48.33164 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 211aab24-f688-35f7-8e3c-cddcdae8bdc1 | -3.05971 | -54.40561 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec361b21-81a8-3f05-9bd1-4a4e135e1008 | -2.92625 | -52.68414 | 2024-11-20 04:27:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a0c14dc-2621-3601-9b23-9002f1af6627 | -3.84749 | -46.6415 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57949603-ecc6-3ea3-94cb-ede288593533 | -3.80663 | -47.80315 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 71d54263-152b-33b9-91b0-d9d98b5748c6 | -3.94348 | -49.95112 | 2024-11-20 04:27:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9227542-14ee-3206-a969-a305ad58bcd2 | -3.84851 | -50.69863 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57b02880-1826-3023-8001-cf5024f17171 | -6.24709 | -46.04361 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 577c5c9b-72ec-3b73-98c5-c30091a4ffa8 | -5.10912 | -40.33061 | 2024-11-20 04:27:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6c0d8c8-7b60-3bce-bee0-75875c13a8e1 | -3.82436 | -51.21809 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02ba3c52-6db7-30b5-8277-cc305a085b8d | -6.94524 | -45.0822 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bd3dc19-9ab5-3c5e-a8dc-96b331bfd875 | -3.11309 | -53.70763 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ccf9fb7-dbc2-3d29-8461-352fbce021de | -4.44849 | -46.5831 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 35.3 |
| c89df997-8ea2-3bc1-8440-f8f4fcd57cb0 | -2.91195 | -53.07783 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2674a812-e649-3271-85a5-eca9ee05b2d2 | -2.91194 | -48.31621 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efadb86f-96aa-306a-938e-aac69890690b | -3.23256 | -46.44184 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deb19445-0dc8-3e22-940e-935a64aebd4a | -3.23533 | -46.44582 | 2024-11-20 04:27:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 896d3c98-e69f-3d5e-89be-7fb48e7dd83a | -3.2684 | -51.62269 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2806753-2401-35f8-8551-8c630ad74c2b | -5.37688 | -44.96463 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
