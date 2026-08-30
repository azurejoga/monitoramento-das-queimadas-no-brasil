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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bfc2128-50ad-3bef-9949-49646ae131b3 | -11.21471 | -45.06745 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9448aa41-ca9e-3802-8956-2da649bd2958 | -11.2713 | -45.33966 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7c712d85-bae0-3ca4-aa99-311227603bfd | -11.82109 | -51.03967 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 63a3d018-fb2b-3159-9425-c7566e4fd636 | -7.17943 | -43.71607 | 2026-08-30 04:14:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2dacee6-7892-3c1b-9f5f-014e97526329 | -10.75131 | -54.04337 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c1560b9-e887-36f4-a481-5bcc1504acc5 | -10.13954 | -45.70373 | 2026-08-30 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 92084a22-1497-3205-beb2-6078d55cff6f | -7.04812 | -42.20456 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ef8b7833-ef14-3462-b2ef-9e1b80d3c732 | -10.75255 | -54.03731 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f3027830-9de3-3813-a8fc-e501555ce68c | -9.21381 | -46.0661 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd530046-2cea-3574-95c8-07976dc35504 | -7.08136 | -42.21773 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53273984-86e0-320c-a16c-180e4070a96c | -11.27379 | -45.32553 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e0aa31c-375e-3dc2-aab8-7375a0bd5faa | -12.92362 | -45.89793 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d56ed26-5351-3016-8e97-11246d966e2b | -10.94958 | -43.03421 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8705cb28-ca72-3ed7-9d88-21bee0480eea | -12.80383 | -46.45307 | 2026-08-30 04:14:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 826c0584-8408-3457-9e4c-1eec79a83352 | -11.57065 | -44.0339 | 2026-08-30 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81470e37-5c4e-360c-88ef-69f4304f59eb | -7.60704 | -45.84359 | 2026-08-30 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83e59020-0378-35ab-a203-6ed67d84f4c8 | -12.90664 | -45.85278 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7c8c07d-9985-37ce-a39b-19c0baf34e00 | -11.21687 | -45.07735 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 782ee3dd-a21e-3f7e-bdae-1fda8d510567 | -8.01679 | -48.01352 | 2026-08-30 04:14:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 717dacaf-7ec4-3267-bd87-e3ecb2871711 | -11.21982 | -45.08268 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e9563af-3ecc-3502-8db2-e09f6efd8949 | -12.07899 | -47.19534 | 2026-08-30 04:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89a1e3a1-8065-32bf-8c82-cde5edf156b9 | -10.94802 | -43.02229 | 2026-08-30 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 05de4541-0dfd-3c82-bffb-611637d0aa2c | -11.35626 | -45.16622 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 598720fe-0b8b-3246-af66-8385ef03a183 | -8.25169 | -46.50544 | 2026-08-30 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed7aefaf-f51d-3c1c-bd6c-78dbe862cfd4 | -9.68772 | -46.54666 | 2026-08-30 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 538499a0-10e0-3492-aa50-72d7da9cba4e | -10.75351 | -50.69513 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc57de4d-89fc-3d43-a765-aee39c6b6dd9 | -11.63583 | -54.59238 | 2026-08-30 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a74322e-6f78-305a-8e3d-254e423fc645 | -8.1428 | -45.47499 | 2026-08-30 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0da03ca-a817-3a7d-bb9e-da8fde5daab1 | -9.76129 | -48.16191 | 2026-08-30 04:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b214557a-a2e6-302f-b766-ff406bd3abf9 | -12.07971 | -47.19138 | 2026-08-30 04:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c603e0b9-d01a-30a4-9b0e-c8cad53e388c | -11.79355 | -51.06422 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 17137da3-e4cf-3dc7-b27b-6f572824ac66 | -7.08764 | -42.22265 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c2f818e9-e521-3e9f-bc6d-e2f3f7b2e133 | -9.4169 | -51.68349 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b898b051-fdb7-3291-adf2-96258e09e6ef | -11.15435 | -50.5841 | 2026-08-30 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6aa92494-c240-375c-9abe-f241c5e8b71b | -10.73789 | -54.04073 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c71fa91d-e492-3720-88c5-521991b439ab | -11.26441 | -45.07158 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6ba61a4-f9b5-3c09-9e9c-0961fdda12dc | -6.90528 | -43.65187 | 2026-08-30 04:14:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43f2769c-4984-3920-824f-a2ef39d3cff8 | -8.60798 | -54.77534 | 2026-08-30 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5781b38b-f6bc-3a5f-a437-9dade3d6f16b | -6.49675 | -53.26601 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72cf2259-5816-30cf-b62c-e038123380a4 | -13.69779 | -45.04963 | 2026-08-30 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e390d43c-d179-3a01-9868-9bd0a8999558 | -10.14359 | -45.704 | 2026-08-30 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ced8510-ffad-3484-9a43-b4cd907de00b | -11.21331 | -45.05323 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46916a79-a3af-31d1-83be-9d86a9ff6abe | -11.80185 | -51.0508 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 6819b379-0fff-3d92-b865-5b1563a06fe4 | -11.24308 | -54.00095 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a0aa88fe-9637-3a1b-9037-fed245e890bf | -6.91711 | -44.95274 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d58b83c9-0a20-3661-af35-6ffbb910976d | -12.80604 | -46.45798 | 2026-08-30 04:14:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 908e4115-4bcc-3f1b-9e2f-e0784fc45f27 | -11.34118 | -45.16336 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3805b188-4aa4-34bb-acf2-49da867123d5 | -7.09703 | -45.76905 | 2026-08-30 04:14:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6ade6cb-4627-38d7-85c8-f283b870bd24 | -11.25846 | -45.06109 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 042a4881-0e9d-3ad7-ac2a-7abbbcb4a62d | -9.12418 | -50.59172 | 2026-08-30 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5222b98-28e4-3805-b96a-786dab652680 | -7.37776 | -45.10316 | 2026-08-30 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7706d13c-fb1e-341a-9c37-1f423e9afc16 | -7.4874 | -45.38964 | 2026-08-30 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2900ac00-6cf3-36f8-8ec9-5ee3762b7ae8 | -11.82039 | -51.0433 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 48ef1bb4-0f1f-3498-80a1-b5f89522373f | -12.89779 | -45.8811 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b4e2a7c-0f22-38c4-bd0b-a9196f9d972f | -6.12175 | -53.55922 | 2026-08-30 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0257f6d4-7f33-3bc2-8b2d-a7400487903b | -12.42828 | -42.88295 | 2026-08-30 04:14:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7774cb33-1b59-3df8-a5ed-7e9df6906176 | -7.10267 | -42.21732 | 2026-08-30 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00a3afd4-8767-3dff-8f05-7380f01bcf06 | -9.42351 | -51.5845 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4da447c0-7fca-39ad-b32c-77cdf70b4a98 | -7.11279 | -42.8457 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3232ddab-3e2a-3127-8702-7a6205191126 | -7.32087 | -45.34231 | 2026-08-30 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c1c5f12-6a2d-3720-84c8-05b528fb5e1b | -12.08323 | -47.19613 | 2026-08-30 04:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6989e1f7-1160-3e11-911f-14ba5296a5a4 | -12.91099 | -45.87365 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66e18fb0-6e7a-3d6c-8f6e-7bb3b1ecbe5a | -11.81969 | -51.04693 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cbc86380-eacd-3c9d-93b4-e6822e72c1f9 | -11.22276 | -45.0881 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 822a95c1-11bc-3685-be18-a3271905565d | -11.27231 | -45.3232 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ae45823-b7be-3611-b119-15245454cbc0 | -11.37221 | -45.42887 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d1ebce5b-d6e4-396c-b45e-86eda1665ebf | -7.63306 | -44.82283 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf69f1bb-905f-32c8-a4ab-3ca52e83e5d8 | -11.15907 | -50.58867 | 2026-08-30 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e9db5e5-e39b-3e3e-8bef-4fe9b7d0fd02 | -11.16142 | -51.29462 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95186e15-70cf-3963-836d-f2ee277e02dd | -8.61514 | -54.77711 | 2026-08-30 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c508b70c-72be-370f-93a2-63c98634d9b5 | -12.93729 | -45.91056 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aad9f7cf-1491-3555-8a2e-0da6feebe568 | -9.31363 | -40.22026 | 2026-08-30 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e2f5370f-7d09-33fb-b26a-1f819496ac09 | -10.76444 | -44.87139 | 2026-08-30 04:14:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 75a5aa0b-399e-3b28-9e18-ea892c8ee277 | -12.43043 | -40.07769 | 2026-08-30 04:14:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e9112ce-160a-3d7a-a237-0a9ed40ebff4 | -12.89863 | -45.87623 | 2026-08-30 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee0ebb64-6868-3c4d-ab72-aaf869731623 | -13.20104 | -44.07047 | 2026-08-30 04:14:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8dbc5a9-a7b3-3b72-b10e-1e6ca7bee530 | -11.29325 | -54.04372 | 2026-08-30 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 484329dd-44cd-3ef1-9229-c83b8f88a98f | -11.23626 | -45.09987 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80152d90-93ba-3847-a2a4-53828b0358b3 | -11.21014 | -45.07144 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8646746-eb97-32a6-bb80-d1504abd7127 | -12.43108 | -42.8871 | 2026-08-30 04:14:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 267b45ea-1447-3a38-8534-da1dd3d27acb | -10.12835 | -45.69752 | 2026-08-30 04:14:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db98abec-606d-32a0-a084-2a12d55e3d79 | -11.26991 | -45.33735 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 81efb7ad-a788-317b-89fd-6ab5561763a1 | -12.38582 | -48.17913 | 2026-08-30 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69d17f30-6fd3-3730-82dd-c22058f50a84 | -12.38135 | -48.17817 | 2026-08-30 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1475c816-40ce-3d48-b05e-f95fd062c3cb | -11.82447 | -51.0517 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 22087a86-cea0-3660-b171-993412db0300 | -9.66382 | -55.10844 | 2026-08-30 04:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0837e39b-078d-3b90-8a53-09ac6f0921c3 | -11.23978 | -54.00136 | 2026-08-30 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7c857263-9d4c-3f08-b3bd-6a9f899e57d6 | -11.26143 | -45.06635 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b327e21e-27ce-3a6c-9094-190b4ab098f9 | -11.82656 | -51.0408 | 2026-08-30 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0fb51212-1202-395f-b730-7c76d41ddd41 | -7.60806 | -45.84311 | 2026-08-30 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6dde637-90e8-38a0-9546-262f3c5b28cd | -9.31751 | -40.21729 | 2026-08-30 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 84fda599-ae37-3e74-bfa6-7b6d86d30928 | -11.34576 | -45.15938 | 2026-08-30 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd096022-51ba-33df-ac83-a419373f2c6c | -11.16256 | -51.30205 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eb81f43-094e-3c7f-b58f-4ba552478d3d | -13.35752 | -46.92382 | 2026-08-30 04:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e45b36c9-9e83-3f65-ac89-d091c6f5c0f9 | -7.12282 | -42.76183 | 2026-08-30 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3a34391-8b62-361d-8068-35058e6a3134 | -7.49208 | -45.38678 | 2026-08-30 04:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8b1acd61-692f-360f-a601-1b47192b402d | -7.61721 | -44.84524 | 2026-08-30 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72a4ffe5-8064-3168-8fb0-ec7b7917d9ea | -11.1618 | -51.30593 | 2026-08-30 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a351ac1-82ec-3063-890e-f1c0b1ff305d | -13.93969 | -43.99635 | 2026-08-30 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b484b08c-0fc8-3348-be76-28d43fa1ca94 | -9.76506 | -48.16796 | 2026-08-30 04:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README29.md)
