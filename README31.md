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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 039c51ff-598d-357b-897c-9669145fddeb | -11.38276 | -50.97212 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89b7755f-c6ef-3059-8ae5-7bdc1a4a152f | -11.8474 | -50.96001 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a5e723c-594b-3d90-bcbb-e61730174cc3 | -10.72124 | -44.42738 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d86cddc-cb5a-354a-943b-bc40fd41feed | -14.94033 | -49.75042 | 2026-09-30 04:34:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d763b9c-6d9f-3a8f-aa63-29fac752c97e | -11.38958 | -43.37534 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 008b24ac-a3ac-331c-9886-944510aaaf51 | -11.45536 | -43.46177 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a872414c-4d8f-32fb-beaf-d15ed0eba177 | -16.67898 | -41.85122 | 2026-09-30 04:34:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9ec00f3b-dc00-3d96-ab35-deb62428f9e3 | -12.77979 | -54.01999 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07d8da1f-a077-3597-8d8d-0d2656ebf459 | -11.84275 | -50.96284 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b37fb345-20c2-3575-940b-38756c1a14b2 | -10.51641 | -45.37435 | 2026-09-30 04:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3e1d2bc-3250-3e2e-9bd9-7b5fbf176986 | -11.63621 | -43.52832 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df9bad85-8a3d-39b7-951f-27023d37d2b7 | -11.93927 | -44.80598 | 2026-09-30 04:34:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cbedda7-af50-33ae-a0ce-e0992630642d | -9.80634 | -44.83503 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa28aa44-0794-3d4b-aa2e-546ba3a3c2b3 | -10.28689 | -44.61653 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82820399-4326-337e-a746-92b2d0b35ee9 | -11.36313 | -43.35629 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26f4604e-4319-3dde-a302-3568ce08262b | -14.85287 | -48.18092 | 2026-09-30 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ee01368-58a2-3f1e-ba9d-fd7871febacf | -12.19385 | -47.11193 | 2026-09-30 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d87c060-f67f-3a29-a2d4-49c3defa106e | -10.71116 | -50.8356 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35cc6804-fdf1-304d-9206-c56a8b48dcc1 | -14.09958 | -46.27541 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58551164-a37f-3cad-b8c6-6dd43270000e | -11.3497 | -43.35019 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72fe6e88-7a71-3d8c-8bef-c762f68462b2 | -13.70015 | -44.23037 | 2026-09-30 04:34:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| add90db3-3e3a-3f0d-af8c-e67a5ac23dd0 | -11.83469 | -50.96135 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ced5b50-384c-3f6d-8cd4-3429e4b05172 | -10.71505 | -44.42273 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e921ccb-e299-3ebc-b366-cee4aaabb88c | -11.83594 | -50.95417 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b529db49-cc9a-39e0-8373-7e4699f11c88 | -11.42676 | -43.48537 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9f381d6-9890-3fd2-bc1f-43a89feacc69 | -11.71262 | -43.45061 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab833abb-d715-3f0a-996a-7f4122c64051 | -9.77517 | -44.81559 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89f6c8a6-8e86-3bc4-bfca-baa761dcd61b | -11.38257 | -43.37427 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f39c03f-5f4d-339f-a277-b6acc2bdcd12 | -13.19338 | -48.55193 | 2026-09-30 04:34:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ed207c5-b6c2-3e12-be7a-90d2ac4948eb | -15.63177 | -43.22889 | 2026-09-30 04:34:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 979c5872-1494-3caa-a3e5-50a3851c061c | -16.35467 | -42.58133 | 2026-09-30 04:34:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f580ce9-f1d0-3361-a0bb-3585828e8192 | -10.90372 | -43.85306 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 998f110e-f720-3c3b-9007-c084235e455d | -11.22477 | -41.62529 | 2026-09-30 04:34:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b777b38-9a16-34ea-b868-1c11b17095b6 | -9.78825 | -48.22567 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ffb70f2-1b90-3648-87cb-b566f195d766 | -9.70533 | -46.71382 | 2026-09-30 04:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af97face-d096-338e-8b74-495fc62ca277 | -13.06887 | -43.27886 | 2026-09-30 04:34:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 89ccd010-cda0-3153-9529-92dc414e97a8 | -11.36026 | -51.02821 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c25c1f31-9811-3a8a-ae44-8a7b5acf058d | -12.79149 | -54.01115 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a75e70f5-ecd8-3597-87f8-5d9dbfbedbbb | -15.30091 | -42.76732 | 2026-09-30 04:34:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4ac6750-da69-3377-86b6-d332a4f8959a | -11.39152 | -50.97 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a211ee28-d9a2-3ae5-93df-8b6f2dadabb0 | -16.64638 | -49.39155 | 2026-09-30 04:34:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc4b2dda-63a8-33ad-9dde-00955d4119cb | -11.18119 | -44.83779 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 25fa6eb6-551b-32af-b362-63229b0499ea | -11.63911 | -43.53276 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d96780fb-54c8-37d2-9a8d-7ed0f94e50e5 | -10.76592 | -50.48093 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 107df8a0-49fa-328f-885e-c41afd140bfc | -11.85235 | -50.97939 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7dfea1a-acbd-359f-8690-afc15c71e5e1 | -11.41464 | -43.42345 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13c1d8b4-49b6-3d30-920b-c24f7085c9bb | -10.72461 | -50.49882 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9ada056-3b4d-3d91-82a3-67d661723efb | -11.36116 | -50.97565 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afa1d32e-40a0-3eb1-9450-bba09430b553 | -15.16016 | -43.56888 | 2026-09-30 04:34:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 80272677-0c0d-38f8-86a8-386619192a3c | -11.43794 | -43.43507 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34541dbe-b131-3445-8c9c-5623c420d4de | -15.57546 | -47.88932 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ad33feef-611d-3926-888e-cf245787ad1d | -10.72068 | -44.431 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9779d2ed-a87e-3ee2-8bac-dc8474fb8236 | -11.32669 | -50.98062 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b2cf1d3-c6a6-360b-b6e5-bf16dcbbca60 | -13.37677 | -46.82068 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbd7c709-e39b-3b5f-a9d9-ef2915eada9f | -14.8162 | -42.77208 | 2026-09-30 04:34:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77cf6c7d-61d5-3213-9732-e93bfe723701 | -11.40182 | -43.41344 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 149950cb-6d1e-3b4d-b58e-6ceaacd5f09d | -11.19133 | -45.14592 | 2026-09-30 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53cf2171-78f7-350b-846d-58f7de1d2755 | -11.44375 | -43.44399 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 43d02c1a-9616-3af4-b55d-d947570ac42d | -10.72062 | -50.4981 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d57c4c83-804d-3ab1-b5d4-20110704b5ac | -12.0737 | -46.44869 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2603b52c-fa5d-3934-af1b-d2d2af32c11a | -8.93362 | -49.77415 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40e3f6c9-1b2d-377b-ac37-76d00927c758 | -11.43385 | -43.43845 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117c8e36-5f33-385c-8c8f-65addb4e021f | -10.66573 | -50.7423 | 2026-09-30 04:34:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68fd295c-1864-35bc-b743-d9ff96008a1e | -13.33745 | -43.96161 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 923d5eca-4c85-33a2-9b68-a562def1eabc | -11.39483 | -43.38824 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfecdcd3-7cea-3ae7-ae52-a64e33824406 | -17.71242 | -42.04806 | 2026-09-30 04:34:00 | NPP-375D | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 964fcf95-ea46-3e3c-8ca1-6602c3f571c3 | -14.52958 | -48.29729 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7481a37-d663-35f9-abb8-3e10e3e8b76c | -9.77183 | -44.81505 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9fab62e6-0e08-3220-9cca-b5c3a22a2648 | -12.07923 | -46.4569 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bff10a01-835e-3b6f-b275-69eec5b21c4a | -13.43148 | -43.81467 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 6e58a900-b609-3266-aa19-194b11bdd6bf | -11.40307 | -50.97587 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d1df5578-c851-3ce6-84bf-25aaccc73d54 | -11.98432 | -50.89063 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14a1b805-2660-3e2a-bf66-313f03baf382 | -11.67938 | -43.50304 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7371a1e6-cc49-3280-b528-9d53b8dc0cd5 | -10.51399 | -50.84528 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d08a3bed-5855-36a2-aee3-e3e98b9607f0 | -16.9122 | -42.10975 | 2026-09-30 04:34:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ff416a39-46f1-3d5a-829a-bda83d417cc7 | -12.77597 | -54.0136 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e53bbd1-16f6-32d5-9e32-7d577ba3695e | -11.17224 | -44.82904 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15e8171a-7696-3f80-897b-86bed83db884 | -11.70853 | -43.45401 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0187d8c2-efce-3f77-b18b-1aae0fbea327 | -8.32043 | -54.75961 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50727272-9693-360a-a323-944939566e9c | -15.97916 | -48.13293 | 2026-09-30 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e92e9cb-7fb2-3d46-8faa-8bb41c44e20c | -13.06948 | -43.27473 | 2026-09-30 04:34:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f2d9f6f-f516-3cf7-9bba-607b5b146dc0 | -11.34832 | -50.97708 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e030521d-f3d3-3b4f-b4c4-202c2573b9e8 | -11.38729 | -51.01808 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fbdf8b7-bab8-3166-b2fb-680894f602f6 | -13.52296 | -44.31302 | 2026-09-30 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0d53566-e96c-3a69-95e8-ace1486a5e32 | -11.40989 | -43.47878 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d654bfa7-4738-3117-9194-97b8fc7694b4 | -13.37953 | -46.82479 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f45c21df-01a4-31b5-846e-6334f3cc993f | -12.78283 | -54.00384 | 2026-09-30 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aeb6ab71-29e3-3308-bb8e-dedffc71d137 | -11.84894 | -50.97506 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 641e12ba-286a-3e52-8993-5ed63bea7c8b | -12.70419 | -46.96274 | 2026-09-30 04:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a9c903d-14de-3118-a5da-57ce91da78b0 | -11.83406 | -50.96493 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be892ec1-ab5d-306c-971e-f478a139e8e0 | -9.7952 | -44.81878 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95c94a2a-f99a-39ba-8127-67e08e2bde6d | -12.24846 | -50.24607 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da0acece-50aa-3741-bed4-3c4301169717 | -11.85638 | -50.98013 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72689752-1b7a-3b0d-92fb-3e182e198070 | -12.24294 | -50.25501 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2198fccb-7291-3fb4-b003-fdcf0978211d | -10.69147 | -44.44121 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 019197b5-03a2-3091-9be9-b58870ead697 | -15.25768 | -44.82208 | 2026-09-30 04:34:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e039fe6-00b0-3553-b374-7d7ee7ec0e21 | -12.8914 | -44.80595 | 2026-09-30 04:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f84ab9d1-dcbb-3429-9a4c-436574a9f863 | -15.19598 | -46.13906 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e82170aa-54e1-3316-ba60-497bd935c82c | -11.41232 | -43.41506 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9c304e9-c123-33c1-a78e-fd066abeba7e | -11.68346 | -43.52637 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
