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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26a90743-b375-3111-8064-d780b67c6a17 | -13.24919 | -48.58159 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2fb89f02-cbf5-3fe2-8f60-e4f0fb0e1ad1 | -13.24859 | -48.58468 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fa5d0df-70a1-3724-974e-67e679199aa7 | -13.248 | -48.58778 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ff30af5-950b-3b25-af3e-d394acb59962 | -13.24346 | -48.58386 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da08c393-d1f0-3b7a-b117-f1eb5dd9f2fa | -13.24226 | -48.59008 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 555bd54c-648f-38b2-abe0-9ec65d278734 | -13.24165 | -48.59324 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a2f3c27-140b-3e44-99b6-8e7638f763d5 | -13.23954 | -48.57678 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0afc2c6e-299f-379d-a606-637d13bcf1d4 | -13.23893 | -48.57992 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 203aa1e7-75f9-3e8d-a675-590b4dd0017a | -13.23506 | -48.57262 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 844f48e8-7f67-3bea-b875-a150c7fea5ce | -13.23444 | -48.5758 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cedef6d-6b95-32fc-b8a5-616ff7a76317 | -13.22994 | -48.57173 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bcfe2c1-5dd3-3674-8c30-622e5cbe783e | -13.22933 | -48.57487 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ddbdbff-8fb0-38d1-97c9-cae0c053b549 | -13.22488 | -48.57056 | 2024-10-02 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b61325cc-1544-3de6-a358-e12530620368 | -14.81318 | -49.04486 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58c6fe74-1dac-3f77-8632-d8f8567b7365 | -14.81258 | -49.04795 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbf5e7bf-6998-36ee-ba80-d4ff2f4b2a4e | -14.81138 | -49.05409 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c41d40dc-bb82-30cf-87d9-efa2544dfb87 | -14.81077 | -49.05724 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a3a9de6-97ff-3a9f-a2bb-af97dbe3b69a | -14.81015 | -49.0604 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3a0b3ec-a7dd-3efc-b07f-b2fb3fce4462 | -14.80688 | -49.04996 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e172432-1bad-3b4c-8fa0-d602ea1819e6 | -14.80505 | -49.05931 | 2024-10-02 03:55:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2628d90a-880f-3e3e-893f-a37185e6a209 | -14.80959 | -48.76917 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d6bfead-5471-37fd-83ac-c3c4700bdfe5 | -14.80851 | -48.77461 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5efe2de1-eb55-3043-b137-a23cc70d1e48 | -14.80798 | -48.77732 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9e21f6c-2568-3b3b-bdd6-bddeced2da26 | -14.80746 | -48.77993 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0b341ed-9f41-309f-8b41-93d7400a37ca | -14.80679 | -48.75704 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35d3ced2-c8db-3d78-8341-ae956499aa0b | -14.80623 | -48.75983 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5688b4a0-1d3a-39b8-bf0a-d6a550b6e2f4 | -14.80569 | -48.76259 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fcfe72a-1e4e-3471-a52d-73f01157de15 | -14.80515 | -48.76528 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16901a46-6c39-3974-aa44-edd8153c901c | -14.80462 | -48.76793 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aac09ab0-0985-3c30-8400-141c24fa468c | -14.80356 | -48.7733 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6e4e75b-d393-3364-a65f-7256fb89d88c | -14.80302 | -48.776 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5707118f-7944-39f3-a1d3-cbc0798de73f | -14.80249 | -48.77866 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14b3a6d0-2e96-379e-b406-5085a02629b6 | -14.80197 | -48.78127 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14969208-4247-39d7-8a02-8abebd8eefb6 | -14.80094 | -48.7865 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccdc0a53-e6ac-39b2-b5f0-32b691a01d9c | -14.80037 | -48.76782 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d7edbee-0d64-3051-baf2-b82a45131847 | -14.79985 | -48.77049 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e17dd837-e2b4-3e94-a39d-b66bd4246489 | -14.79961 | -48.76696 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4231083b-d4cf-36aa-92d6-102312cacac4 | -14.79907 | -48.76963 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c64890e5-9ce9-3e05-97cd-94ba1990274f | -14.79885 | -48.77572 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2932764f-2a9a-361f-bf48-a51a8a2d6bb3 | -14.79835 | -48.7783 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5acc80b-f24a-3695-97e2-a55d07df2d45 | -14.79804 | -48.77484 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79be43de-4fdc-3265-8864-b53f97c2e868 | -14.79785 | -48.78091 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7b4a222-077c-32b5-94dd-917d1eb00e24 | -14.79753 | -48.77738 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac812c82-4679-3219-a03f-36779e73b7d1 | -14.79733 | -48.7836 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a8cd716-ccf5-334a-8113-acf2fd3a8d2b | -14.79678 | -48.75498 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 814641cc-006c-331f-8251-53856711ce6e | -14.79648 | -48.78265 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6bf87e4-938c-321f-9f3d-c2d629a4ee7c | -14.79623 | -48.75775 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ac5e57f-b8d9-37ec-865c-62be99c78316 | -14.79621 | -48.78948 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 763b1274-4730-3b85-9992-ad30f4c6484f | -14.79594 | -48.78538 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b4650a3-8c92-33a6-9cc0-ffbc5ff50b1f | -14.79536 | -48.7883 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7bba328-d7eb-375f-9df5-89975169fe5f | -14.79466 | -48.79178 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1ab811d-473d-310f-ae1e-ba9c2b51bede | -14.79385 | -48.77462 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 555a2547-b7e6-35da-9d5d-66a902724dc1 | -14.79286 | -48.77977 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91b27faa-7cb2-3629-adac-d6ad0b2a6a8d | -14.79201 | -48.77889 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5437da3c-97fe-300b-9423-f29ea75e887c | -14.7873 | -48.78157 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32ea0e3b-6d77-3e06-b903-18467ee9b7eb | -14.78644 | -48.78065 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b355de29-17bc-3eab-bc2e-3f830d4e20d3 | -14.78614 | -48.78762 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e358f003-cfd7-3fd6-ba42-5ed2756790cb | -14.78523 | -48.7867 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3d41b0f-d055-30e1-8134-c7d6f7b7831e | -14.78279 | -48.77789 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cc818bd-9de9-37b3-a37e-04e42aa7ef67 | -14.78224 | -48.78074 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b5ac95e-a09a-3d81-a44e-468c584d440d | -14.78163 | -48.78395 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cf5cfbc-a664-38fd-8e16-e0939ee7f493 | -14.78098 | -48.78733 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9411675f-cda3-3435-ad33-58c50d8534e0 | -14.77778 | -48.77685 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36827253-1143-34ab-a01a-170aea3c62ba | -14.77596 | -48.7863 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e3c423e-2f04-350b-87ab-eb446c5595c7 | -14.7753 | -48.78977 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a432bdf-6244-30f7-b543-075c62b6fa82 | -14.76968 | -48.79182 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3bae2381-ed32-3299-8f95-6233c72b2774 | -14.76901 | -48.79532 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac22cd07-8164-3f21-beba-91145fc82aaf | -14.75819 | -48.79725 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6218610-16d3-34bd-8bc7-8a7cc9318664 | -14.75751 | -48.80078 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39a9e59e-da2b-36e9-9b80-95161bdf2a51 | -14.75686 | -48.80416 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14faa2e5-270c-3a88-989f-88312e77db2b | -14.7531 | -48.79658 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19a9784a-63bf-36c6-b5e0-ead4ba3b6746 | -14.75245 | -48.79992 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 113eb414-3dfc-3847-8e89-cb99668d1323 | -14.74806 | -48.79564 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c0b8c6a-bcb9-331b-906e-07250304b553 | -14.7451 | -48.78399 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f72f238e-c0d1-3c10-89ec-734f3d65e43b | -14.73929 | -48.78701 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a1933bd-5d61-3cf6-9176-6d59e8448a1f | -14.71909 | -48.75692 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 955c5fa7-4905-3552-a1cc-86a3935b4ab5 | -14.71861 | -48.75934 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb5c96b8-ac8b-3324-b07c-660cb34b45d6 | -14.71811 | -48.76186 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1587fae7-50c7-3a51-a9b8-e77b2a5ccb1a | -14.71361 | -48.75824 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b673e79e-73de-383c-bc08-33269e59622b | -14.71314 | -48.76063 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 224deb33-86aa-3028-9049-95c3b48d41f9 | -14.71263 | -48.76321 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece14d9b-e138-3831-904e-8a68a5e056b7 | -14.71201 | -48.76635 | 2024-10-02 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24c02cb3-672a-3db1-b10d-afdcdabf8180 | -16.20084 | -49.19523 | 2024-10-02 03:55:00 | NOAA-20 | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de0c2818-e470-3d08-9820-b0f10fd12ac0 | -16.20019 | -49.19856 | 2024-10-02 03:55:00 | NOAA-20 | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d30bb28-4600-3dc1-a671-9597cd6a5972 | -16.10476 | -50.30121 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b50842c-4145-3c3b-a8f2-bbb631d5a0f4 | -16.10405 | -50.30474 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b586bfba-b201-3ee7-8b55-d48521fc106d | -16.10335 | -50.3082 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef012795-311b-37c4-9983-522dcea7dd23 | -16.09883 | -50.30273 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 741a28f7-66c8-3b68-8d9f-2da14a9d14f7 | -16.09813 | -50.30616 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3037a259-1f71-35e8-8ebf-8b650af60a50 | -16.09743 | -50.30962 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 498a3fba-a74e-3856-853d-308470893c13 | -16.08789 | -50.30106 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 746c027c-055e-32d2-91cf-dc1b4d388a2c | -16.08717 | -50.3046 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 517bab76-a1c8-3092-a9ec-152ceba2d490 | -15.91873 | -50.14747 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3a643f9-6a85-3022-9731-58b373e3ea0d | -15.91799 | -50.15118 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63088a68-e4f7-36f5-a02c-79348c4386b8 | -15.91724 | -50.15487 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aada1172-21ba-3fdd-82d6-b144f4149876 | -15.91218 | -50.15219 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65316781-ca14-35c5-8aa3-a34221a39a90 | -15.91138 | -50.15622 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58ee8515-60ff-36f6-b9af-2daf82eed6b8 | -15.90758 | -50.1473 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2a8f5f9-357f-338d-b8ea-4fbea6461d26 | -15.90679 | -50.1512 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3df95931-1d60-3960-82eb-12d8ce921fb6 | -15.90596 | -50.15534 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README74.md)
