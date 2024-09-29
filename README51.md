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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e062ba0-84da-3239-851d-9b1fe77e0125 | -9.64016 | -53.58236 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2d4cbcf-defe-3fc8-a2c8-2283ec7be180 | -9.63961 | -53.58586 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44657a3b-fb37-3bbb-9444-2619cd894b28 | -9.63906 | -53.58935 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dbb369b-f732-3aa0-a5b5-946e69c0314d | -9.63685 | -53.58183 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f67d7a22-03bc-3e07-befc-1bdeba727b2d | -9.6363 | -53.58532 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43c5f29a-3c28-3446-8e97-db4ae532cbff | -9.6352 | -53.6138 | 2024-09-29 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d235dcf3-2364-3b90-a28e-c58deb316bcf | -9.63465 | -53.61729 | 2024-09-29 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f6c82b2-593e-3e44-a6e1-a721086f1bfb | -9.63354 | -53.5813 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7020d59-5770-3adc-bdba-feb23b5cc61b | -9.63299 | -53.58479 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c71300a0-5100-3e7c-9fbb-a8e15b5f2957 | -9.63189 | -53.61327 | 2024-09-29 04:49:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d4560f2-e23d-3e78-9269-20d40a445fb8 | -9.62968 | -53.58426 | 2024-09-29 04:49:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1c012ee-147a-3320-a3df-f64519047f5e | -9.58762 | -53.85025 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ec66b45-b07b-32a1-94e2-9a52435988e3 | -10.93921 | -54.2608 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f91ac337-dcff-33b4-a10b-65df5e9c8838 | -10.93757 | -54.24966 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c650b983-067b-3091-a256-aaeb8e757e7b | -10.93701 | -54.25319 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbe66eeb-ff0c-3088-89d0-df27b60ee588 | -10.93589 | -54.26026 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38ca2066-4146-3d3a-ab50-a4571075895d | -10.93369 | -54.25265 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c768663b-746c-3e55-99b1-a4e0faaacb4e | -11.18318 | -53.89994 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a1e33d1-c358-310e-9bf7-bcf001a92396 | -11.18263 | -53.90344 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8dd3b14-c648-3057-95cb-7be907d3411f | -11.18043 | -53.89589 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fb70066-81ac-32fb-9ea8-2efb297b5dab | -11.18041 | -53.91746 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3adcf47a-3192-34ae-aba6-f3a15e479176 | -11.17987 | -53.89939 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8695e4f-c542-3ab4-a657-1ca603677c6a | -11.17932 | -53.9029 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44f37a90-c37a-33bf-9469-5d80653387a1 | -11.17877 | -53.9064 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54b70fbc-7aa0-3ab4-a7ef-73bf06e7bf39 | -11.17767 | -53.89184 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46bbab03-965e-3f95-9e3c-8d11dc521f4d | -11.17712 | -53.89535 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdccdaac-5991-3b59-bd35-394236a37f91 | -11.1771 | -53.91692 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78b4e77a-c7c4-38f5-ad1e-13050b6206b7 | -11.17656 | -53.89886 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02595d6c-599c-31f4-90ca-9fb23f62175f | -11.17601 | -53.90236 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ba6661b-aac3-3853-ad86-379357ad5841 | -11.17546 | -53.90587 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a6e01a9-189f-32c8-929a-c8a0354e8152 | -11.1749 | -53.90937 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72f2eeb6-8ce0-3ab8-8f25-976f10b24253 | -11.17436 | -53.8913 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a93e26bd-aaf9-3872-819e-3af453063e0b | -11.17381 | -53.89481 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a0c3f540-3ed1-3d69-b8b3-66ccaf96f1e7 | -11.17325 | -53.89832 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6aa08de6-6b0a-3b27-b889-557039b42106 | -11.1727 | -53.90182 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fc32b90d-e91f-3665-b36b-25e5369afa0f | -11.17214 | -53.90533 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92df3852-cd3a-3ad0-b9fa-6e989f22d6b1 | -11.17159 | -53.90884 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df60f459-73f0-37ec-87f6-98f9ddb5b306 | -11.17105 | -53.89076 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75518cc7-0861-32fa-bc69-1c86574b5408 | -11.1705 | -53.89427 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| d63ca5f1-fb7f-3e0b-b9b7-c97bfbd62326 | -11.16994 | -53.89778 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| cec175a2-b48e-355f-a4c9-1dff472781fc | -11.16939 | -53.90128 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e1a127d5-63f3-3a4d-a02a-938a83430fb7 | -11.16883 | -53.90479 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 939890a9-f89d-311c-a5bc-43c39d02a2a4 | -11.16774 | -53.89022 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d3a96c2-607c-37f8-8bf2-bbfdc2cf621e | -11.16719 | -53.89373 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b444cb1-ad1b-3640-9110-ad17827b47de | -11.16663 | -53.89724 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acb4c9cf-5def-3099-a7ad-c10d8fa0ee7b | -11.16608 | -53.90075 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 236c741c-e0a0-3766-85c4-17b2d7a3c35a | -11.16388 | -53.89319 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a1f4d18-5e1f-39ad-af75-2f6696e3f707 | -11.16332 | -53.89669 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e87924b5-6b8a-391a-976f-0533a889e935 | -11.20858 | -53.86808 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea312504-d1ef-3280-bc9e-1a5b9e1b301d | -11.20803 | -53.87159 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3eb2b2a3-ca48-3e76-9dad-16aa46c53288 | -11.20748 | -53.8751 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a291f7f4-5b3a-39ca-a701-063c9939acc5 | -11.20692 | -53.8786 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3c19524-2a98-3890-9bf3-8305c4a43aaf | -11.20637 | -53.88211 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d9af20f-a34b-36d9-a950-2b974408a849 | -11.20527 | -53.86754 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1739a2f-d9e6-3b47-9f3b-d434fc09c3a5 | -11.20472 | -53.87105 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e19d76b-25fb-3a50-9b36-5a53a476fe9a | -11.20417 | -53.87456 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5476f1b9-cb53-364a-8150-c7dc2cb66d33 | -11.20361 | -53.87807 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3f32ae9-9ed4-3de0-941e-7b6b9fbb1133 | -11.20306 | -53.88158 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 949934dd-69ea-37a7-8b15-39bbe630dc35 | -11.20141 | -53.87051 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8df61522-93b6-3af2-b1d4-2165a0b832c1 | -11.20086 | -53.87402 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d93157e3-4841-3d07-9e5c-8f0b4115b4ec | -11.2003 | -53.87753 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ae5cc66-41bf-38a7-93af-b5ec37377272 | -11.19975 | -53.88104 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 006cf4af-f668-36a7-9347-ac2b41f0f5ca | -11.19921 | -53.86296 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87e94bad-ed21-310a-bed7-178d5f1e01c7 | -11.1981 | -53.86998 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b5d89a0-1a4b-32de-ac10-b5db41e38e0b | -11.19755 | -53.87349 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9df0362-550f-341e-97e2-d5b593eba507 | -11.19699 | -53.877 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 855467b1-7cce-3c2d-8f2f-7f3fb548733d | -11.19644 | -53.8805 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e47b0e8-6b92-35cc-a1f9-d15cb049843a | -11.1959 | -53.86243 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a0a7798-1372-3ed6-b288-6b54a7208139 | -11.19534 | -53.86593 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f25ab05-729d-3050-8335-d6a742598965 | -11.19479 | -53.86944 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd65fbc0-5d9f-3941-9013-98660863ab06 | -11.19424 | -53.87295 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac285a66-4db2-361d-acff-9eb15eba52ea | -11.19368 | -53.87646 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46aefad0-8867-3ebb-8fb9-b6063479ca1f | -11.19313 | -53.87997 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b53d233-eb38-3759-9f32-94e3d2029679 | -11.19259 | -53.86189 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 712a00d9-f01f-3491-96e4-f310fba43458 | -11.19203 | -53.86539 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f8d0c46-05ca-31ab-bcfb-0f0d3f7b3eaf | -11.19148 | -53.8689 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a60ab41-08c7-3b3a-8ab7-875edbfe5386 | -11.19093 | -53.87241 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c2c8df8-6347-38e7-b583-f5486dd0e2f4 | -11.19037 | -53.87592 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bd0b3f7-1050-3a2a-941b-3b4b6524a160 | -11.18982 | -53.87943 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bf5acb9-9a5d-3a3d-b92d-74584051f7fa | -11.18873 | -53.86486 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72faba80-648c-3ede-9f6b-54dce46bc9a5 | -11.18817 | -53.86837 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48986c63-90f0-38df-8938-6812becc97df | -11.18762 | -53.87188 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d9a0b8a-509e-3382-b55f-347b9101e2ef | -11.18706 | -53.87538 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97be70b2-bee3-3b7f-a7e2-a3926195a3ae | -11.18542 | -53.86432 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79a1e951-ad61-31dc-80ff-6b4505467f08 | -11.18486 | -53.86783 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd43ef85-6cef-34d8-a618-80f02f2c42d1 | -11.18431 | -53.87134 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8014305e-5a54-3d75-9b89-f392e5714d4c | -11.18375 | -53.87484 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c88e6791-f57e-39f6-873f-aa328a744a85 | -11.23129 | -53.87468 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c04d090-6df3-3ead-a1ac-20754ce68dfd | -11.23073 | -53.87819 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9877b260-363d-37d1-bb2b-d5ab9581af6a | -11.22798 | -53.87414 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9f65b7e-4f7c-3526-b941-bcad95407f4c | -11.22742 | -53.87765 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b834ec42-162c-300d-9d52-c10a5c8fe52c | -11.22513 | -53.87077 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99a37027-4187-3422-8a8e-d41b5e66791a | -11.22458 | -53.87428 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c35e680-373a-36bf-9de5-099abc5281b0 | -11.22403 | -53.87779 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea93a9c4-efde-3b15-b1d4-33d2cb2c6503 | -11.22347 | -53.8813 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bf6acda-efa9-3dfd-8177-12c905bf38df | -11.22182 | -53.87024 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1f3ef1c-a593-31d5-bd45-707741e08c0d | -11.22127 | -53.87374 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4497cb42-8a22-3913-8bdb-b38e321b9ca2 | -11.22072 | -53.87725 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d93dacf0-d31e-3755-a8e5-1844e2942cfe | -11.22016 | -53.88076 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d9afb05-6900-39bc-bea8-d4ff30bd4a23 | -11.21851 | -53.86969 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README52.md)
