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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50c17c8f-e934-3705-82c7-09131064a55c | -3.46986 | -50.08865 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a54f390-413e-3a0b-8c1b-3cd81e598b03 | -5.99636 | -53.51833 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31547f58-e74c-35d6-83c7-c54669f5bf57 | -6.00469 | -53.51206 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 23623b0f-bdfa-37db-a449-85b6ffdf1d53 | -4.287 | -48.57032 | 2026-10-05 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5ce9594-5cd9-3b7b-a5c3-7804bab54a74 | -3.46865 | -50.1027 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a79ef85-2c89-3798-87bb-c15edf84fd68 | -3.84811 | -50.31708 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 00bc448b-8218-3289-9ae8-5eb81784a0de | -7.18297 | -42.00099 | 2026-10-05 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e6f962c-a405-30ae-aa9c-4ca18d00029f | -4.17595 | -46.44691 | 2026-10-05 04:02:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1afc12-d9f6-3ba4-bebb-93608e722b22 | -4.30191 | -50.78282 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c0b2db3c-f64c-31cb-8c9a-44dd2e651be3 | -8.32119 | -45.47911 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21f4ea67-5e09-3f93-8c8a-357e88891748 | -10.96783 | -45.41748 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1a9f0d5-2010-312d-a066-c42b7cf893a2 | -3.94009 | -47.97743 | 2026-10-05 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8406f765-10e6-3efb-b08a-2bff5cd00386 | -6.62024 | -41.78806 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f53a3ffa-2882-3d64-9478-0a8500216f29 | -5.95268 | -41.3435 | 2026-10-05 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 830b6db4-2586-3275-9973-ba5b1416e57f | -3.27886 | -50.01898 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4eacff1-e0ad-395a-a074-354f06157819 | -6.92622 | -43.67957 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c5e7a150-ec3c-3568-9960-3fa5c9eee397 | -9.81604 | -44.7976 | 2026-10-05 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c20a3ab9-46b8-3283-b30f-c1eeaafb16ec | -6.18022 | -52.93791 | 2026-10-05 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 128779fd-1fbc-3e51-bde3-d695c9d81722 | -11.8618 | -44.74306 | 2026-10-05 04:04:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1151e44-b581-3527-acbf-ae46269ed94f | -15.29298 | -43.8043 | 2026-10-05 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68d49e23-e17b-3fcf-b365-58a9c9d9f4a1 | -16.31044 | -43.96316 | 2026-10-05 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d439d2c5-44d2-354d-814e-9a488a51637f | -11.77171 | -44.9229 | 2026-10-05 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aef5d665-13a2-3d1c-8743-654c0e5a4318 | -12.63704 | -42.86259 | 2026-10-05 04:04:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2b97c509-73a6-3257-a1b1-8779c04fe932 | -17.04985 | -40.23037 | 2026-10-05 04:04:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d8005d8-e8f3-38b1-b8ff-391c3452f0e3 | -12.05465 | -43.43562 | 2026-10-05 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 205422fa-91ec-3a7d-8a84-48bbc3d89866 | -13.39317 | -41.32833 | 2026-10-05 04:04:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2337a5d9-354c-381d-afb4-2bee514c5a64 | -11.82761 | -43.53518 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f6707df-7baf-3393-bd0d-66810ac2d267 | -16.30707 | -43.96259 | 2026-10-05 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f76f4c13-ddc7-3aa6-94f0-91beb934e000 | -13.46515 | -41.34711 | 2026-10-05 04:04:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25dcabbf-e8c4-3ee9-97e3-4345eb7480dd | -11.68717 | -43.64176 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7ce9bf22-61a7-392f-90fa-3eaae7735d2f | -15.57245 | -43.76809 | 2026-10-05 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af1ff86a-7d52-35f7-987d-279ae8a05e65 | -16.67597 | -41.84624 | 2026-10-05 04:04:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 51d404de-3dc9-3a32-8414-9d1231d74669 | -15.879 | -44.23725 | 2026-10-05 04:04:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8d942b0-71ff-34f8-9e2f-fca994085e52 | -13.63603 | -44.42422 | 2026-10-05 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| dcde6b88-80ea-30d0-a091-0d02900417b2 | -13.58171 | -43.70852 | 2026-10-05 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f73863a-8dc7-3c07-a2d7-1cbf5edb08b0 | -16.67874 | -41.85039 | 2026-10-05 04:04:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 3d1600d2-9e15-3746-9266-75addb960f45 | -11.64193 | -43.61464 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afeda941-0fcf-3a0a-a8fa-1bd684c9abf3 | -16.0254 | -45.13185 | 2026-10-05 04:04:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d96dd300-be2c-3153-9b16-4a5db78da8a8 | -16.02892 | -45.13248 | 2026-10-05 04:04:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76900751-a691-36fd-aeb8-48f76a13f211 | -12.86184 | -39.92345 | 2026-10-05 04:04:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d9b3040-0971-36cc-a147-77cb58a51abb | -11.71322 | -43.63435 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e22d19a-9afa-31e7-b0d2-4f1de7a0bff7 | -11.63911 | -43.61023 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e99426e7-b60f-3296-aaeb-6dda2247d0b5 | -16.67542 | -41.84984 | 2026-10-05 04:04:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8e3479a3-6f46-35c8-8a22-f54f5d62ae3c | -15.57184 | -43.77181 | 2026-10-05 04:04:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 692cc8f8-bf99-3820-b405-bd51e56a3bbd | -15.4978 | -44.41474 | 2026-10-05 04:04:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 40638a27-f0a7-39df-8269-a6dd2d6d87c6 | -16.67929 | -41.8468 | 2026-10-05 04:04:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 1b444e20-3dfb-3603-a0d7-f0124fbbc485 | -11.68433 | -43.63739 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8bd95556-194b-3858-a5f1-69ad9ed5b727 | -15.6385 | -43.16977 | 2026-10-05 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d116409-2b47-341f-8bc9-c5b4e756bf43 | -11.68087 | -43.63685 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 70135d14-2dbd-3c5c-846f-ebb4786fd510 | -11.6837 | -43.64124 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85998ce0-6eaa-3896-8714-7c1200fc41f5 | -11.71258 | -43.63826 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17031c6d-55bf-3ac6-aac9-58be8e707477 | -17.05331 | -40.23086 | 2026-10-05 04:04:00 | NOAA-21 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 19ff0e92-5806-3d20-b8e2-4972a35c2fde | -16.02961 | -45.12839 | 2026-10-05 04:04:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bda08a2-2cce-3c93-a84f-1e3c2b45ab9d | -11.68654 | -43.64561 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 679b6671-8388-3cfa-bcb0-d4adb836dfe7 | -12.05404 | -43.4394 | 2026-10-05 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 994ae46e-3a81-3a72-8e1c-1a14c588a841 | -11.68023 | -43.64072 | 2026-10-05 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e74c002a-12f3-3ed0-b002-c912c48aadf3 | -11.76801 | -44.92249 | 2026-10-05 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a632f44-d144-3174-b43a-2f6f5adf694a | -12.19011 | -39.76857 | 2026-10-05 04:04:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46ec2ec6-ad62-3d0b-8015-dc10e35a1f6d | -12.86129 | -39.92715 | 2026-10-05 04:04:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2c9f2d0-3813-3674-8a13-5777baec5849 | -3.8448 | -50.3063 | 2026-10-05 04:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2278ce12-1f29-38b3-a8d9-b5a9f3fa906e | -3.0917 | -54.1666 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 0b3a3db0-c886-3929-a80d-f535f297aee6 | -3.0917 | -54.1867 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 15ebe96d-fdc2-3544-afd1-20978763b437 | -2.9817 | -54.089 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| acc5d44a-f9ac-3084-aab2-a9a8c2ca3d13 | -3.0734 | -54.147 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| ab79eca6-69ef-36b8-8f00-35ebbe67c0ab | -2.9817 | -54.1091 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d7ca4452-0f4b-3916-9234-7561c9975728 | -3.8447 | -50.3273 | 2026-10-05 04:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 70d0fa9e-12b8-3e15-8440-cb51c9a6a5df | -3.055 | -54.1675 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| df34cbf9-da6c-34d1-8ede-142c2072b978 | -2.9632 | -54.1497 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2002d67a-a378-3150-8130-46d23b1ebb35 | -3.0734 | -54.167 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 390.2 |
| 34181192-cc10-3262-b6e2-80f225fcb989 | -3.0733 | -54.1871 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 218.5 |
| df2521d0-1453-3ef1-a2b3-facf729e3c54 | -7.4442 | -63.5589 | 2026-10-05 04:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 23862816-5e6f-3b03-9586-2c2b6346ba1d | -2.9449 | -54.13 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0e0cfa73-7674-3755-9207-dcb6f61def02 | -6.0075 | -53.5122 | 2026-10-05 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 99331dd7-c47d-3947-9c3f-d10d599cf791 | -2.9448 | -54.1501 | 2026-10-05 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e86f8ed1-de4a-3d48-8cfe-ad0388b275c8 | -3.11 | -53.75 | 2026-10-05 04:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de5fa8b2-34c8-3975-9207-2edde4016a00 | -3.4762 | -54.5772 | 2026-10-05 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ffb0b014-5874-34d0-b856-b897d613d2bb | 1.8583 | -55.8018 | 2026-10-05 04:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 83922153-af34-3b17-b96a-7a82369d1fb4 | -3.4578 | -54.5777 | 2026-10-05 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| c44669a4-2f7c-32f7-adff-6ab152d30faf | -7.4442 | -63.5589 | 2026-10-05 04:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| da8f246a-a748-3c50-9754-a888a544e707 | -3.8448 | -50.3063 | 2026-10-05 04:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 9cff9579-c906-3f72-8f37-f56a3209c3a4 | -2.9817 | -54.089 | 2026-10-05 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c6b332d0-52db-3e6a-8c53-0bbe0f08e9d6 | -2.9449 | -54.13 | 2026-10-05 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| d5f452ab-e516-3551-b84a-3f63cb4bbda9 | -3.4761 | -54.5972 | 2026-10-05 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 9f74fc8c-863b-39c7-8c0d-4b0bec5b79d6 | -2.9632 | -54.1296 | 2026-10-05 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 88b5a861-560a-3274-a03f-d922f3ef3b6b | -3.4577 | -54.5977 | 2026-10-05 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b2ef9972-4cdf-36a6-9914-6bb4a8fceefb | -8.6736 | -54.5481 | 2026-10-05 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b6f9cd16-d103-30e5-98ef-a41f5d2da818 | -3.0734 | -54.167 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 258.2 |
| 56afcce8-6dfc-3c7e-89f8-9950fba2efa9 | -3.0734 | -54.147 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 45362dd1-6d3e-3865-a1df-233688ab8c2e | -3.0733 | -54.1871 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| d4c06694-42f6-35e5-a6ea-49343293bdca | -2.9817 | -54.1091 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 61aa8749-dae5-321c-9a0e-d5efb60d13c8 | -3.4577 | -54.5977 | 2026-10-05 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 6da1897d-b292-33e5-9c9e-f52e6b98b4f5 | -3.055 | -54.1675 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 99e74d5b-fa69-35f7-bd7d-804096e76644 | -7.4442 | -63.5589 | 2026-10-05 04:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 21becdc1-6031-3fd9-8caa-063c9bca744c | -3.0917 | -54.1867 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 4f718750-071c-3143-bbf9-24b85152966b | -3.8448 | -50.3063 | 2026-10-05 04:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| dc33c565-1dee-32ae-903f-e0bc28488e81 | -2.9448 | -54.1501 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 7cc2384f-ee90-3a4b-9266-e36232f34e98 | 1.8583 | -55.8216 | 2026-10-05 04:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 82761acb-5836-3c48-a1f8-7ed54f58c1eb | -3.0548 | -54.2277 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fc4465d1-f7ec-3d84-a797-1f219bb2232d | -2.9632 | -54.1497 | 2026-10-05 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| f6b45934-ec7b-3c6d-9020-b30d444e609e | -3.4761 | -54.5972 | 2026-10-05 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |


[Clique aqui para ver as próximas entradas](README16.md)
