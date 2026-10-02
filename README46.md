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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a546e0db-c47e-3c52-95fa-b86ee707f75b | -11.75947 | -43.5784 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ea2c226b-dcc5-3145-ab57-7f91c3ecbe9b | -14.20474 | -43.62757 | 2026-10-02 04:17:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 572d30e9-f164-339f-b91c-66c955cff7ac | -11.30468 | -50.93542 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af394fde-0c27-3d83-a7ff-c4bf2405caec | -11.13374 | -44.593 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66228989-5694-3738-9110-ba111a644d09 | -11.66041 | -43.60241 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 0661a96e-50b3-3170-8a0e-1131e56936ec | -11.52467 | -43.51807 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae36fbc-ec20-3111-9c24-845e44dbe5c8 | -11.4404 | -43.40639 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08bb0c7d-42a0-395b-b377-cf98fe2888f6 | -13.00447 | -51.31336 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24c7f733-afcb-36ad-880c-4488f4e3483f | -11.69956 | -43.50727 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71093500-5e88-3db8-9eec-3ed120340ee2 | -14.00687 | -43.82374 | 2026-10-02 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 458fad6a-0d3f-3398-9c9d-81b69dc8af51 | -11.25886 | -44.25804 | 2026-10-02 04:17:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76aa13af-053b-3821-bbbd-214ce5771a76 | -12.72692 | -41.80814 | 2026-10-02 04:17:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 941ccb6d-a041-386b-adb2-65c98ef78766 | -13.34481 | -43.86277 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 195460bf-4f83-3894-8ec6-ae911abb2e38 | -11.43493 | -43.52499 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28794f85-7941-3f22-96e4-f4e56a307213 | -11.59905 | -43.54156 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daa79649-9dcd-3450-8fb1-51e9df87b278 | -13.80121 | -45.2529 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7071e5ce-f95c-3ccc-ac1c-a3d6c92d6a98 | -15.30851 | -42.77855 | 2026-10-02 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ef4014f-21c9-3498-96f0-3a216c7a7fd1 | -11.47074 | -43.42949 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7673a4b-ceb8-3030-b454-cbdf1b9f013e | -11.80046 | -43.57789 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b8ac3e1d-dab5-3c54-bdf9-a3252eaadf6a | -12.8266 | -51.43989 | 2026-10-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ddb483f0-a08a-3c4e-a703-0320e8536e95 | -11.38386 | -43.35741 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aea73c51-9a36-3718-98e5-bd4fab1c176b | -11.15491 | -44.61553 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 2eb38f2b-e820-316b-a295-76146d2264d8 | -11.13817 | -44.58978 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a780a0f-b988-37f2-bc5a-e9d9f19a3b25 | -10.81561 | -51.09737 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b14fbd62-4db9-32a5-b47c-068f7b77c384 | -11.70369 | -43.58777 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2468bc0b-eefe-3d55-8abf-b31eba93d6b4 | -11.65984 | -43.60594 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 0e757713-71db-3d51-af13-9e519a030cf3 | -10.60418 | -50.04761 | 2026-10-02 04:17:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a26bed9-d409-3d8a-9f9b-860b7cb74f06 | -13.39036 | -46.81596 | 2026-10-02 04:17:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62bd18e5-9f86-35a1-a885-21fa690c8eb4 | -11.76888 | -43.58353 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| aae2908c-f719-3a28-960a-673b603009b7 | -12.32407 | -46.38017 | 2026-10-02 04:17:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a903e38c-66a4-3c29-a3be-b74719ab1d09 | -11.77066 | -43.55128 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f287c7c-19e3-36da-b05d-b2ee535cc3ef | -13.79718 | -45.25608 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ab98ce6-164a-3bb0-8e27-97dd1b7eeced | -11.23951 | -45.18933 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54dd589c-a09e-328b-b551-f3b9f9489d06 | -11.2432 | -44.24791 | 2026-10-02 04:17:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26b1087d-c410-3f9f-bb26-065073fc8bf4 | -9.33909 | -50.99931 | 2026-10-02 04:17:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e3334f5-9aec-3c3f-8e30-fe7af2bd12ee | -13.86226 | -44.44946 | 2026-10-02 04:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b47b2e4-e5b9-3630-8a7d-89a636814f4a | -13.33989 | -43.85099 | 2026-10-02 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebb02734-c0dc-3f87-9a02-15f06b518cd0 | -11.23147 | -44.29845 | 2026-10-02 04:17:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee8aa8b0-a634-348a-9d72-2d8ea1db0de4 | -11.20774 | -45.14399 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2e5671d-3b02-3dad-8e71-dc8b3424f1df | -10.30168 | -44.63864 | 2026-10-02 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01824e7a-f2a4-322a-8d07-aa41695c9e9b | -10.71799 | -43.71703 | 2026-10-02 04:17:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83da9d9a-e3e9-3944-ac38-d9fed5c56c0c | -16.85652 | -40.57706 | 2026-10-02 04:17:00 | NOAA-20 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e2b1d592-71ea-3aa1-aeac-79cb0e665426 | -11.76556 | -43.58298 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09b21f8e-f0cc-3508-b1c1-43bd4befb338 | -11.68643 | -43.61027 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1552d102-5aad-30c5-a17c-47f2858a21f7 | -13.49127 | -42.50586 | 2026-10-02 04:17:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 65be5432-bc46-3083-803f-6795d3db347c | -11.47009 | -43.45473 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6b759e0-fe25-3e82-942a-559b7e3f53bf | -11.23943 | -45.23318 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb215d47-2b5d-3f07-8e5e-424f38260454 | -11.13384 | -44.61586 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 969ead95-4e71-3187-bfff-f9b09b975189 | -13.3811 | -44.01873 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7f4e743-a967-3cdd-9246-7eee1591b906 | -11.76001 | -43.44806 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0793346c-9e63-33ac-8a2d-c8b17ad8610d | -11.1335 | -44.61599 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43557fc4-3594-3a8e-ad62-987269e4b745 | -11.644 | -43.55612 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a91984a5-0a99-3874-a27a-42ea0fa2dc98 | -13.79377 | -45.25549 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 409724c2-b869-3638-a314-3088047cc824 | -10.52464 | -43.50313 | 2026-10-02 04:17:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7925fe88-fd4f-3d20-b81c-1927b52d245f | -11.44371 | -43.40694 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1229e84-060e-3933-a3ad-7923a31ff6ef | -17.21517 | -41.21083 | 2026-10-02 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 86b4333e-5f03-36b7-9ae8-52bb6d26c375 | -11.63538 | -42.93038 | 2026-10-02 04:17:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc7dde4f-015b-31c4-9267-3ab4c4068163 | -11.84577 | -44.74567 | 2026-10-02 04:17:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab78d129-1f8d-3c81-81c3-a0db44fd64b2 | -11.68975 | -43.61083 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 343abc5f-f560-35b2-8bfd-11580c023efa | -11.15552 | -44.61181 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| efb37ea1-ed01-3788-8ef6-c61e94e37bd4 | -11.73825 | -43.52091 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 834a9325-7d5a-3607-887e-9b8761d9a744 | -10.89731 | -51.18514 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 09b1e044-0111-3d12-b820-a26d0fb7bfb0 | -11.2521 | -45.2307 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6efca2ed-f15b-3ddd-bf97-0b19f9e21cae | -11.79496 | -43.56966 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63ee576b-4d27-35b0-a866-46cafcf2a622 | -11.13714 | -44.59359 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef815544-abec-32a2-a482-a8bc20b75b3a | -11.68699 | -43.60676 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61399c41-4e14-315e-acad-9cf15fad8053 | -11.46135 | -43.42432 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d737fc2-18bf-3686-8c8a-4ec8176117dd | -12.92261 | -42.45096 | 2026-10-02 04:17:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 178db1d6-c9a9-304e-a300-7dd5740699a0 | -11.67759 | -43.6016 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40330272-06ea-3ad5-b374-d04a01a2fabf | -11.24234 | -45.19381 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5aa8c9c-2ffc-392d-a011-9b784353a7f0 | -11.2071 | -45.14781 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87e56054-5457-3caa-b256-78f0f7370502 | -10.90177 | -51.18907 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9783f26-f9d8-3428-941f-8f91f5f45f39 | -11.14468 | -44.61383 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34c615d2-9726-31db-b2b4-2bd8a590630c | -11.75672 | -43.57436 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 7edb9403-d952-372a-a492-9c8955037207 | -11.74675 | -43.57272 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bba392aa-abdb-37c2-be41-0eb7207c8d96 | -13.40276 | -44.01138 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d7e627f-9910-320c-a47f-036d0b9f5d81 | -11.7247 | -43.43534 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffc56588-4dd6-3f64-be91-923eb3c2a16c | -11.79051 | -43.57619 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b129a8c-6fd3-3854-8520-d7f66105d6d4 | -12.27915 | -47.23359 | 2026-10-02 04:17:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88fc367a-306c-3987-95f7-9c16d31dd5a7 | -11.15088 | -44.61869 | 2026-10-02 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d9e1acb2-cabf-3518-a2e7-82e381fa3033 | -11.74524 | -43.53982 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d33d41a4-78b5-39e1-9744-6a0be1fb2dfc | -15.77528 | -46.02773 | 2026-10-02 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 200c573a-22e0-3945-b7c6-351f725addab | -11.71947 | -43.51056 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 078d6be8-690b-3402-95dd-3fac462ac539 | -11.46572 | -43.43952 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3fbafb36-115a-3086-9bd1-c3e116b152fe | -12.5702 | -43.07542 | 2026-10-02 04:17:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c76acfc8-5395-3e78-9849-9c1d53f2cee7 | -10.8962 | -51.19104 | 2026-10-02 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09ed0e05-8652-3558-8868-9b659fc44fca | -15.77354 | -40.77775 | 2026-10-02 04:17:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 86378b07-a027-3668-9a54-98051fef080f | -11.46847 | -43.44359 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 051e7274-415b-3d9c-8111-98c6ae8161a0 | -12.39301 | -49.83237 | 2026-10-02 04:17:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6247b2d-4ada-377f-9fa8-f0a447198f5c | -11.44432 | -43.53017 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6ed8cf5-9d9d-3c44-99d0-16a5f870fee2 | -11.43736 | -43.40601 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d3e1db9-6683-304e-badd-2c1fedb14f4f | -10.70287 | -45.32359 | 2026-10-02 04:17:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c98b070-04c6-3169-a81c-b8fcc0b76ad6 | -11.25276 | -45.22681 | 2026-10-02 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c89edb9-8ff9-3494-934b-492042f16b45 | -10.2627 | -49.66267 | 2026-10-02 04:17:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| aea353e3-304d-3da9-8de7-dea189c3ec71 | -15.74651 | -43.64969 | 2026-10-02 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d0c70669-7a0f-36f8-8e59-2801997df470 | -15.24909 | -41.01467 | 2026-10-02 04:17:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b2e34ff7-39b2-3704-ad2e-3b3518e1cac5 | -13.79036 | -45.25491 | 2026-10-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fef63f69-db93-3962-ae47-44bde82724ea | -13.40172 | -43.99656 | 2026-10-02 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38be1524-2f72-326f-9fad-8c3499a62865 | -15.77341 | -43.65028 | 2026-10-02 04:17:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a540115e-d18e-36ef-a0d5-17740629c1ed | -11.26931 | -43.56298 | 2026-10-02 04:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README47.md)
