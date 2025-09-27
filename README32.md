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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52027e87-4e74-3df6-b6ad-56ac890bd17c | -12.64778 | -51.6828 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb6ddd30-ebc9-3ade-831e-868cf75aecd2 | -13.87822 | -44.24355 | 2025-09-27 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2f195d8-f3d7-3bda-8d27-29807e8cc3d1 | -8.47615 | -47.83099 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a25d086-cc49-341e-b9ba-c208d6399c19 | -11.4332 | -44.92662 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adef5b2e-fec0-3ebc-b601-2b9df3714b60 | -8.13112 | -44.12701 | 2025-09-27 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a11f0fa-344b-3407-ae10-28b876dd32c4 | -7.80909 | -46.89565 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d34e6a5f-0e4f-3368-b556-1f7de447f8d0 | -11.34934 | -45.01274 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccb91da6-a91c-3e61-8cc9-92e04fd6856e | -8.66888 | -43.98966 | 2025-09-27 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af16f43-2aae-3ce8-9a3b-7ba76ba81430 | -13.32838 | -47.30981 | 2025-09-27 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5086ac4-5c74-3460-9a81-a51eb291a7c0 | -8.65125 | -44.00949 | 2025-09-27 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ae36e64-86a6-3119-8425-c4070c690e71 | -11.9636 | -47.89495 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15c80206-aefb-30f0-975a-705df821bb29 | -10.93822 | -44.30895 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86bf814b-1ceb-31bd-87b6-04a798449e9c | -9.69515 | -48.94638 | 2025-09-27 04:23:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d385eb26-1008-3246-9c47-e1ed25d8b0c6 | -7.86394 | -45.2907 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddf7dc67-2fec-3612-b1ad-fd4d36640a28 | -10.03809 | -52.08754 | 2025-09-27 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0b94308-cc87-3aa9-9a0e-8f070233b3b0 | -10.80997 | -45.37732 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7c1e400-4165-3b7e-857c-6d2d9d960ef2 | -10.92574 | -48.82888 | 2025-09-27 04:23:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e985d80-378f-3447-80ed-4c1736a65562 | -11.98731 | -46.61001 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5b65de97-5292-3660-9730-a5f43c2af04f | -11.43273 | -44.97431 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e63ad4b-b2c6-3379-bc30-9a9f00466217 | -8.81915 | -46.26271 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14ce564e-90c0-31d9-893a-94db8a89fae5 | -8.83314 | -46.26135 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a0ea643-78c0-34da-b951-c1cc03eb5f68 | -10.90846 | -43.63042 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d05923dd-11c9-341b-ad26-66ba7b29c98c | -11.37774 | -44.94017 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 903dfecd-f697-31ec-8e65-e815e2eb076e | -12.62713 | -44.19854 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4c25aae9-b35d-3233-a5ae-b9cec56e038d | -10.1079 | -45.34406 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f23f1b81-aac3-334d-a725-5d74fa5ab0f0 | -11.61052 | -45.42132 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86975a62-07b5-349c-84ab-4a2681bfd520 | -7.78684 | -46.94562 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dafbff8-6d86-3dc4-a305-cbf347a2bbfe | -9.562 | -47.69737 | 2025-09-27 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dedf8afd-c50a-39cb-b20a-a13c99729680 | -7.72016 | -47.30929 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ced130c6-44c5-3aeb-b31d-0cf0975e11cc | -8.47605 | -47.82573 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 836da142-70eb-3354-b723-989e0ddaf14d | -12.54393 | -45.85053 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6109d383-9674-33c7-b9d1-f333696b7c53 | -12.07001 | -45.04862 | 2025-09-27 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11d5acb6-ebea-3c5a-9bb6-092959a6ee20 | -8.49593 | -47.83731 | 2025-09-27 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1717269-9a7c-3681-bbf7-e282e114dc16 | -9.6959 | -48.942 | 2025-09-27 04:23:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2278ad96-47e5-327c-9727-1e2c2042304e | -11.77692 | -44.86642 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14eb8d0a-0f7d-3e38-9e71-a5ad597ccfdc | -9.11504 | -45.87138 | 2025-09-27 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39f1b82e-6b5d-3bb3-bd43-eca504f70db1 | -11.78475 | -43.75981 | 2025-09-27 04:23:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb63c966-bc75-32d0-9bef-270f285fb59a | -7.7208 | -47.30543 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85532a42-f8a5-31c4-b1ae-dc8aa0f50b29 | -12.29839 | -47.21692 | 2025-09-27 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b0e756e-9e67-35ec-9d94-cd5f04277f14 | -9.75464 | -46.14094 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a67819b0-ce5d-32bb-a71b-a1a0ecdadabf | -11.69026 | -44.40471 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8fe6ca8-935b-300b-9c24-d48866ce6bfe | -12.55226 | -45.84099 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 876ff416-ecf2-3aba-aa0c-bf4ae3e91019 | -7.80626 | -46.95644 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb2c4dba-09de-3c24-9dae-ca6777c49e71 | -13.17988 | -47.40083 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1eb3b2ec-8f53-3fbe-b612-72984eae7fd8 | -13.32898 | -47.30614 | 2025-09-27 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b27fd17-f695-362f-a553-d1235c0a5ddc | -12.54449 | -45.84699 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01b04bab-de49-3e6f-9227-e9e3e4e777cc | -10.78793 | -49.15798 | 2025-09-27 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce5da07d-9533-39d9-97a4-cfb715ce510e | -12.27537 | -44.0648 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78d889ff-f7a0-3f28-83ed-62f90413eb10 | -10.87739 | -49.40291 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37d885fb-5659-3adb-80c2-08795557b326 | -8.81415 | -46.25091 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9209405-7037-37ca-95e5-c4fb798a9e50 | -11.43721 | -44.98982 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 522a8bbd-dc2d-3b0f-82d5-4e226eadf1f2 | -11.68972 | -44.45365 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1fcba1e-88af-3003-ba92-82a6826ecc57 | -9.18318 | -46.64896 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d42f70bf-36a6-3b54-b223-aa47f6b423ea | -12.00735 | -47.88647 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a865e9eb-8a28-3fbc-915e-e3bbe13bdc33 | -8.82529 | -46.26737 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cb77a8d-0cd1-3b75-b041-4ad9b30c21ba | -7.81027 | -44.57771 | 2025-09-27 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9cdf8d4-4146-356a-9de6-25866f12142a | -12.30769 | -44.35509 | 2025-09-27 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 942e1102-55a4-3534-9963-64b1f3eeca6b | -7.71795 | -47.30098 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43fffaec-a0c5-39b1-b274-48d421d18d84 | -12.96967 | -46.91405 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a2e39ca-97ab-334f-b9af-43d237fa6fa5 | -12.98256 | -49.43386 | 2025-09-27 04:23:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4edac24-71a5-3671-8ce8-e63dd277f062 | -11.44552 | -44.93586 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d9e2d66-080e-3f96-a266-b7c25a9cd52e | -7.7834 | -46.94506 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c7f7b42-db54-3996-a8d1-29a90f30d249 | -8.36578 | -41.40102 | 2025-09-27 04:23:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eeb8fae2-6ab1-3d14-9620-b38577ead319 | -12.03673 | -47.06297 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a88035c-1cfe-3dbb-b264-9ac849f70c8e | -9.89257 | -49.12573 | 2025-09-27 04:23:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0eee5a75-c0cf-3bf2-8111-6aae4cb7d476 | -11.82611 | -52.39283 | 2025-09-27 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 628bddf5-76c5-3849-9a4e-bddb1385144d | -11.37776 | -44.96223 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd85a363-0670-3826-82d0-27547f3c6a32 | -9.96541 | -43.60345 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c6cce47-e164-37a4-b110-1d49bccd573e | -12.27307 | -44.05664 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09df9d06-5fcc-3cd4-b92c-2dc2d940d028 | -7.86128 | -44.53555 | 2025-09-27 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78d675c2-87ae-3f19-9076-e4c76eb92ed6 | -13.14962 | -43.3139 | 2025-09-27 04:23:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| da61a576-ca7a-3830-8daa-6c7a450caee3 | -7.85616 | -49.63939 | 2025-09-27 04:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa8b3447-2842-3341-b2f0-4575cae9ad34 | -13.15263 | -44.93894 | 2025-09-27 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea5b6811-e193-3e21-a2d0-972044faa967 | -10.47401 | -46.53014 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e97f6171-a164-3f27-ab36-0190817e2f4c | -12.87725 | -47.09424 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9658c9b6-586c-3978-85ea-f9a7e497d2c4 | -10.80386 | -45.37275 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ff6e1fe-f288-3c95-84a6-ade6d966b1f8 | -7.23535 | -48.34393 | 2025-09-27 04:23:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1e48d3a-0126-34ad-a74b-37cf63f8ba4a | -8.81579 | -46.26215 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32632fbe-0b82-3840-80e5-bf5c192c9d94 | -11.71292 | -44.41582 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed69aa2f-d973-3fe1-8d3f-358151d0043b | -11.14163 | -43.37129 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a2ce6261-5647-36f7-863c-079fc9de2cfd | -11.6481 | -52.87594 | 2025-09-27 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c2aef76-e1ba-306b-ad1a-015776fbe636 | -10.12565 | -45.33971 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9ae64ef5-b406-3449-86a3-b6a7fc2eafe0 | -10.28474 | -45.21001 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d013a07-2095-3139-a690-ac133a4d9633 | -8.77379 | -43.03564 | 2025-09-27 04:23:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4167e9d7-390c-37fd-bd23-83e7bd70476f | -11.65994 | -45.3457 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef82487e-f95c-3acb-9e55-0cb5d785b122 | -12.3015 | -47.17652 | 2025-09-27 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8f910c8-687d-35e8-b8d9-b6ddd5ee6b0c | -9.99654 | -44.17187 | 2025-09-27 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d53ca0f-76e2-390e-b5bc-bc67980a6714 | -11.47593 | -47.24644 | 2025-09-27 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de4c3eae-0db3-33c3-9989-4a733659e112 | -10.11068 | -45.3481 | 2025-09-27 04:23:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a849987-382d-3cb5-9691-10e83ba8d24c | -9.97229 | -43.60453 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a43aad92-3cca-3992-884b-b776d56e10d4 | -9.43476 | -45.58116 | 2025-09-27 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea138ec0-27d4-3aa3-a5d7-d7ef13984368 | -9.16117 | -46.65644 | 2025-09-27 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3049ea7-fd5b-33fd-883b-7bac9a9d7995 | -12.64636 | -51.66673 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 410fbc2c-882a-32cc-8218-50e29ba82206 | -11.35548 | -45.01737 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab6672a0-efa4-337b-a427-35878ace8a37 | -7.88054 | -44.02597 | 2025-09-27 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 273a1ca8-47bc-367d-8659-cc5194f711b5 | -10.28807 | -45.21055 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6dd54d5-d58f-3760-8928-35935341e35c | -11.71349 | -44.41214 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ebb47ec-0aa4-3cd3-b414-14ad1532dc80 | -11.43048 | -44.96661 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 378c8ca1-87ee-392b-b8cb-e3cfe00e6979 | -12.64703 | -51.66297 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b05206b-6a8e-3121-b272-99ac4d71611c | -12.83594 | -44.68712 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README33.md)
