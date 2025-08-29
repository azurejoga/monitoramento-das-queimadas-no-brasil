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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 593896f1-60fd-3488-b48b-6d2ddf528b35 | -12.05941 | -46.62994 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 447ae060-c30a-3af3-9fa6-801e2e175926 | -17.13265 | -43.83103 | 2025-08-29 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5be9a8a0-2cb7-36a0-8229-3249878982cc | -10.02708 | -48.07299 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebd65d8c-bcfa-3076-8642-81426ecc0ffc | -13.38093 | -46.87831 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d579fd32-e0bf-31e9-8eeb-a08a951c5095 | -12.68426 | -48.19543 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 883a6a39-9b35-31e9-8183-d29431c6c173 | -5.53346 | -36.84991 | 2025-08-29 03:49:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b75efb1-e04c-3bba-898b-9d035dc08aa7 | -13.67037 | -44.22309 | 2025-08-29 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61d17522-880c-31bb-ad45-1442b201cc1c | -12.91255 | -48.13401 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d66f314d-1c9e-3d4a-a378-77f40dacddc8 | -6.24252 | -42.3983 | 2025-08-29 03:49:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bb3906cb-96ff-335b-a550-76b05b86693a | -11.08425 | -44.7734 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edf10127-6677-3b4f-a421-9531162d2dbf | -11.57044 | -46.37785 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ff68bfd-2497-3ca9-9988-8e87d427dcd5 | -11.03215 | -45.06843 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bafc69c0-74dd-3eae-bbf5-16aadb0f10a7 | -5.62124 | -45.00915 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1b475bfc-decb-3058-98fa-9b4dfb44f7ba | -11.5612 | -47.61678 | 2025-08-29 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c110c92-b522-3435-810c-30812bcf2e82 | -10.72299 | -47.02155 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 023110e6-3b12-3b60-bed8-428ce2606b60 | -11.90537 | -46.71419 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1adec627-4572-32a3-ad4c-4f89f5b757be | -12.91074 | -48.11417 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b230c6cc-0e70-372b-9005-f3df8dc4f0b1 | -13.66452 | -46.90819 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0063f77-fd33-398e-b6f3-bd2000e89278 | -11.03299 | -45.06367 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad94391e-4d59-333a-89d5-6b2c959354bd | -13.59986 | -46.86749 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0ec77f0-87c6-38f4-8e91-a273734f25e0 | -11.29472 | -43.54166 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68231c92-da74-3fe9-9fd2-9235d0cb9314 | -13.553 | -46.86963 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd8a903d-2ff9-3f8d-9a61-da5f60536b14 | -13.48019 | -46.84552 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f074bc08-32df-33c5-9c0f-9c0827330901 | -13.40798 | -46.84497 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9cb1c8d-d84e-3ef0-bb10-723a570f9c22 | -13.67 | -44.21928 | 2025-08-29 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed2e6826-038c-39c0-a010-b7b2ae4fa1fa | -13.365 | -46.88032 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c098d9b-485a-345a-ac09-558030b68f62 | -14.33767 | -48.65088 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83dec32b-696f-316e-8e40-fc99e9750e14 | -15.32065 | -48.22717 | 2025-08-29 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9a765931-da51-3ad5-8bc4-3469ee5e67ac | -13.48514 | -46.84663 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce371289-a5ae-3691-a937-8e79ce328a43 | -3.98477 | -47.88468 | 2025-08-29 03:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 172cdc4a-0475-3457-aa69-7abf15118362 | -9.6727 | -48.32467 | 2025-08-29 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85329e1e-d280-3a4f-816d-1c276ecd502b | -10.83541 | -47.4824 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfec707f-e09e-36ed-9eb5-e74f1c7d4260 | -17.75229 | -44.50868 | 2025-08-29 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f62b4b21-3dac-32cf-8561-569d795564c1 | -5.62175 | -45.00615 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da4c524f-3346-338e-94d5-04287c69f72a | -6.16344 | -44.17961 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 204587da-6cb8-31da-9470-1b09fbbc7f7c | -15.10338 | -47.87585 | 2025-08-29 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29611b86-e1a7-3690-b094-8831b201332b | -17.75432 | -44.49743 | 2025-08-29 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87e51ab6-76f0-3eb8-b777-978f389b662e | -11.34204 | -43.57281 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4bf2eb2-1341-35ee-a63e-6bbafa8ac5f8 | -13.66325 | -46.91482 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5a1b2c1a-189d-38f4-a01c-1d85105a3307 | -13.4535 | -46.95823 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a7c9d453-d4bf-306f-9f99-2b2bd30766c0 | -6.03636 | -44.46586 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 188424b0-949b-3f9f-9f9d-157e46097669 | -11.08674 | -44.75921 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4fc91ff-abe2-3cc7-bebb-612d260698a4 | -13.53722 | -46.87111 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a3eb9a17-425a-3f6f-a695-8c23f007fd79 | -10.84907 | -47.49951 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eee80881-7954-3e36-8277-5103838de6d2 | -12.08587 | -44.97831 | 2025-08-29 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4236636-a43d-3518-a5fc-73975f8b0415 | -4.07244 | -47.95778 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d57dc912-1f88-33d0-81a5-c25228d19c31 | -11.3004 | -43.54179 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1c052e8-6560-398c-bec1-ad8d2cbe6185 | -5.85715 | -42.94569 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 24af0d49-df19-3afe-8886-ec2c9fbb4f5b | -13.36615 | -46.8743 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d1ea730-60a0-38de-bd09-9c6f757429e4 | -6.69692 | -43.07894 | 2025-08-29 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4814696b-7cf4-3e6b-9aeb-0a1b07885c94 | -12.6906 | -48.19225 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 807c0417-fa21-3262-a189-d84059e1d862 | -10.68392 | -47.08312 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c31f6bba-b4c7-3179-951f-85fc69996d18 | -12.69713 | -48.15852 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11e9be75-c6d9-3949-850c-0de420f4e050 | -13.97571 | -46.33891 | 2025-08-29 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d950fb50-fff8-3331-b663-9fccb6d1c014 | -11.29822 | -43.54624 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70fa8217-90fd-3972-ac8c-315244aae738 | -12.80881 | -48.17035 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 50747d49-1fd8-349a-8b89-0cdc931f1ab2 | -15.07014 | -48.12484 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b21031c-f858-3e83-893d-ea226cf3d042 | -13.36561 | -46.87711 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea5e8c1a-7874-3893-9191-b2aba1b42f4c | -10.02213 | -48.06791 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5eb3b88-49eb-3f8f-8588-64216047e2a2 | -4.49151 | -47.68774 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0a31e5a-c5c0-3ec3-b741-88895591d6db | -4.11412 | -48.01583 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c018516-b286-35e6-9817-534762c40461 | -6.54048 | -43.92627 | 2025-08-29 03:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 8be8e681-50ff-3647-90e5-c863dc59fbe0 | -11.07318 | -44.7567 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3840ce14-011e-35c2-9b81-d63a40e7dd29 | -15.49456 | -41.53029 | 2025-08-29 03:49:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 155add65-11c3-3682-9f82-b9fe1a62a816 | -6.26821 | -43.81357 | 2025-08-29 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 166bcdf8-b187-3a3b-939b-28fb64da4289 | -3.42676 | -49.05019 | 2025-08-29 03:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b6c04e39-60b6-38d2-9b79-7d6bc560e250 | -11.1204 | -45.11958 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 82a28163-0b0a-314f-a132-ad404801dae1 | -17.60257 | -46.68809 | 2025-08-29 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8935d469-2d85-3ced-980d-a3b8143ea32e | -6.22107 | -43.33462 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 399f38d3-203d-3c62-bece-6ea803fefbc3 | -11.26713 | -45.49681 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 784fab9c-9e7e-395d-8091-3648a1185fe0 | -10.94842 | -46.88678 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2ad3e93b-af7c-37ac-a524-ec2a9395e6da | -12.8264 | -48.10872 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f816de10-2914-35dc-a2c6-7443fbfdbe53 | -14.33654 | -48.65479 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3892d33e-70ba-3762-930a-f7f7efab5f50 | -11.56525 | -47.62494 | 2025-08-29 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55cad032-c51b-3a8b-a6e5-e7425f299f66 | -6.40404 | -41.75856 | 2025-08-29 03:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bbdc8f58-1a94-38f6-bcd3-2b6c00c60533 | -13.52329 | -46.86333 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7ef0378-e5c1-3427-a32b-da7c86f22bc0 | -12.70773 | -48.19234 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8eae6f1e-33e8-3280-97ef-aaa0d2334901 | -13.67436 | -46.8838 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e1f5b20-2551-3c0f-ba2f-3a40274d4063 | -17.60159 | -46.69305 | 2025-08-29 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 406c9c1c-48a7-36ec-95b1-29a7fe6b4fa4 | -15.12556 | -48.11807 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef6cd632-bcfd-3851-867a-96a4129bb437 | -11.34674 | -43.54625 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 413419dc-251a-3b3b-a603-870fb2259e9e | -6.13555 | -44.43074 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a1fc696-c1d0-31f3-8982-5df166dc97ee | -6.19302 | -44.00554 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e89668e8-1fd7-3888-85e0-d58c21887847 | -11.93239 | -46.70027 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbcde69e-375a-370f-a1a0-dd4f2993cfed | -12.8319 | -48.10959 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e8e646d-57e9-33f4-9386-38075164e8fc | -6.53993 | -42.66824 | 2025-08-29 03:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a9ceac7b-627d-35c8-a4ea-1934f93e70fe | -11.29002 | -43.55175 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff0f1f6f-37cb-33d3-ac6d-43d4ff365d67 | -12.70695 | -48.19644 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c688632f-b939-353b-afa7-e83898c4fd9d | -6.04352 | -44.4748 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 637c80b0-8179-3565-86ef-5d0357eee661 | -11.32947 | -51.28751 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 355670a6-c011-3553-bb4a-05dce08ab2e4 | -13.6711 | -44.21916 | 2025-08-29 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03443594-7bb1-36d3-ad6c-b3438dfeee17 | -10.64164 | -48.6462 | 2025-08-29 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da6a8106-2a97-3cf9-93c6-f6da9e8e84ac | -9.6732 | -48.32919 | 2025-08-29 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b01a50e-a935-3eed-92c7-ad3223396a0a | -10.97776 | -46.90336 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2597f20c-4186-3e90-9343-1b87686dc011 | -16.076 | -43.62583 | 2025-08-29 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 206ee269-15d6-3f3e-b6b4-41ea49a1c6d3 | -12.79709 | -48.172 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b14d84f-5b21-3877-8131-d43b89428a46 | -10.05383 | -46.60826 | 2025-08-29 03:49:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e728f14-a38f-3709-b39c-f9f1dd289c9e | -18.01279 | -42.90829 | 2025-08-29 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 073dd926-d6e7-3bba-a77e-79437d82332a | -12.83232 | -48.16588 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ddcd2eec-bdeb-3401-b409-3ad40d5052e1 | -15.17179 | -52.3317 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README35.md)
