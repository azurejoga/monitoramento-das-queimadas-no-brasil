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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f69cf6a5-dcad-39f8-9986-662f29471d91 | -20.87962 | -50.07338 | 2025-12-23 05:08:00 | NOAA-21 | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5fbacea2-ef4f-39db-9e55-18b31c36893c | -20.69029 | -48.79815 | 2025-12-23 05:08:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d3ee7a2c-032f-39de-8cc6-e141ee6ff983 | -21.04877 | -49.59238 | 2025-12-23 05:08:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e7d4f8f1-0a0b-38d7-a067-d09d6c04257b | -20.85636 | -49.09073 | 2025-12-23 05:08:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 74d30fe1-7160-3914-9f2c-9b94d1ea003e | -21.55189 | -49.6251 | 2025-12-23 05:08:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4aae29d4-10b8-3a12-835a-b57fc751dd73 | -21.0491 | -49.58895 | 2025-12-23 05:08:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a4b22961-6f20-33a0-bccc-9d5507c18544 | -21.02302 | -48.67121 | 2025-12-23 05:08:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ed4c28cd-6d45-3805-83d2-1ed331fe2f79 | -21.04373 | -49.58833 | 2025-12-23 05:08:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 51efd08d-6614-3eda-980e-155c8fffaf30 | -21.02091 | -48.66964 | 2025-12-23 05:08:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0089b98a-50d2-30aa-b38a-1b5647c9ae63 | -9.7254 | -60.2071 | 2025-12-23 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 89aa6f7f-e1f9-31ef-8671-d1978e120d66 | -24.5743 | -51.82343 | 2025-12-23 05:10:00 | NOAA-21 | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f32daefa-9bd5-3663-9203-61344cd0d6f4 | -26.43845 | -51.04214 | 2025-12-23 05:10:00 | NOAA-21 | MATOS COSTA | SANTA CATARINA | Brasil | 4210704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4bb62e45-2f3f-322e-8c6b-4ef5a1e5d8b2 | -25.60037 | -50.26466 | 2025-12-23 05:10:00 | NOAA-21 | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ed517477-fa5c-3b49-adbc-ba34697d8125 | 4.01043 | -59.98853 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d288104-ac74-3849-974f-e7417abdd8f4 | 3.26364 | -60.10273 | 2025-12-23 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a7d019a-5f58-39fd-a95f-c41f7b4a011b | 3.08471 | -60.42726 | 2025-12-23 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 795ecd6a-28f9-3065-8a21-2cc9a6645ef0 | 3.50332 | -60.89181 | 2025-12-23 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1498e5c-d518-3f72-a832-c272def8173a | 3.26032 | -60.10325 | 2025-12-23 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ee45d50a-aec5-380a-9ee4-3edf78310c5e | 3.86597 | -60.51026 | 2025-12-23 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3ab0860-d500-3110-9245-3fac75cd0e00 | 3.50666 | -60.89128 | 2025-12-23 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f17ed3cb-6a4e-3ada-92c7-36a891732f3c | 4.36881 | -60.34925 | 2025-12-23 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32dedb64-4113-34ca-8796-700ac8f0c47b | 0.46609 | -60.41516 | 2025-12-23 05:31:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a14f258-e1bb-3579-9590-a4052eef90db | 0.46277 | -60.41568 | 2025-12-23 05:31:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5f8a260-157a-3a4f-be82-d04b447fe55c | 3.262 | -60.09239 | 2025-12-23 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8d8973e-3540-3a04-88ea-f3050fb8dff1 | 3.51 | -60.89077 | 2025-12-23 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70e653f5-0cd4-3e12-81ac-cd63a3b2b890 | 4.0066 | -59.98566 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 210c94b9-b078-3106-90f6-9653bbf9716d | 3.98072 | -59.95087 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0256ac37-0231-35fe-b234-425b8a28cbdd | 3.98521 | -59.91485 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5c9a01f-1aef-3e94-ab13-51a3d1fe5360 | 3.50779 | -60.87678 | 2025-12-23 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b685d9a-e7bb-37dd-b4f7-2081fe773229 | 3.96201 | -59.91849 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2bb9a52-9423-3a92-a8a0-6557842f6a40 | 3.86929 | -60.50974 | 2025-12-23 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76cd5ffc-4b40-37d8-9087-269ddcb849b6 | 3.97858 | -59.91589 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 684615b4-a6a9-3d66-8262-e5a623560114 | 3.26087 | -60.10669 | 2025-12-23 05:31:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ea71eb0-dcde-37f7-b070-c8d3c6e8bea7 | 3.86874 | -60.50628 | 2025-12-23 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65c0a692-9047-3fa6-b2e8-b85c956edca0 | 0.46663 | -60.41861 | 2025-12-23 05:31:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00931026-c53b-36f6-a815-bdd884406368 | 0.93722 | -60.16461 | 2025-12-23 05:31:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37f8b5ee-729f-3783-aab8-8b47a103a550 | 3.97795 | -59.95483 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ee2ecb1-86f5-3a43-a151-5a7111eba501 | 3.9819 | -59.91537 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffd4018f-7477-3818-a189-b408ed2bb621 | 3.96256 | -59.92194 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4456ab06-7cac-37c1-a023-36bc66cf1f55 | 3.24563 | -60.95721 | 2025-12-23 05:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 500b2c0f-9884-3079-b87f-f5a663101938 | 4.00992 | -59.98514 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9c019e4-ebac-3544-bad0-93719302a694 | 3.97741 | -59.95139 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 460e9b39-c226-3ef5-be2c-008ffbc535d8 | 3.36867 | -61.04956 | 2025-12-23 05:31:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7fa4db4-ac7a-3c8d-9d51-0ec701164691 | 0.93675 | -60.4794 | 2025-12-23 05:31:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b0f98590-a596-33fb-b89d-c6b9dc91c136 | 4.00937 | -59.98169 | 2025-12-23 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9049bf7-2c38-3674-8e05-af692b35a17a | -9.72095 | -60.20092 | 2025-12-23 05:35:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34e0a3c9-e76d-35ce-b16d-7edfbd6c135e | 3.98043 | -59.95265 | 2025-12-23 05:52:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bdd598b-86ed-3297-a78d-2681ee3f54cb | 4.00798 | -59.98362 | 2025-12-23 05:52:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e665b5df-98df-3ca4-9243-95ba997d2f0f | 4.00873 | -59.98442 | 2025-12-23 05:52:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 988ee838-3288-3dc2-94f8-03cc7f42b01a | 3.24756 | -60.9562 | 2025-12-23 05:52:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9786cdc3-d2cd-3e81-90c9-3799dacc29cc | -12.27073 | -43.55116 | 2025-12-23 06:07:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 26ce2e25-ac90-3fcd-8382-b793b00e8926 | -21.49466 | -48.64837 | 2025-12-23 06:09:00 | AQUA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aecffb42-3fff-3518-952a-40e434cefc17 | -2.44034 | -46.90488 | 2025-12-23 12:14:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0db48979-e7d1-3b9c-bb7a-30dfe2e30e8b | -14.73513 | -42.66947 | 2025-12-23 12:16:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 540f0a07-b70a-3962-8f8d-ca10328dda40 | -11.46186 | -48.50098 | 2025-12-23 12:16:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 10e7eb49-56c0-3768-9aec-ab05896c0c97 | -10.2303 | -47.75344 | 2025-12-23 12:16:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cd05281e-b59e-3d80-8c78-a151899976ac | -21.02575 | -47.3731 | 2025-12-23 12:18:00 | TERRA_M-T | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 584efef6-cb4f-328f-a1c5-b506055b1e18 | -21.12759 | -44.23821 | 2025-12-23 12:18:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| ef2ebfaf-b6bc-32a2-a1f1-91de5242e0a5 | -20.44209 | -48.95354 | 2025-12-23 12:18:00 | TERRA_M-T | GUARACI | SÃO PAULO | Brasil | 3517901 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 063c075e-4dc2-3f7c-91e0-8a197d232954 | -19.44384 | -45.04399 | 2025-12-23 12:18:00 | TERRA_M-T | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9fd5d777-39da-35ef-814f-6a8dc7fa23cd | -20.67242 | -49.99352 | 2025-12-23 12:18:00 | TERRA_M-T | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| dedaabc3-3fb4-3a76-9808-becc6646ed2b | -21.5857 | -45.44191 | 2025-12-23 12:18:00 | TERRA_M-T | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 5872ac97-aa11-38a7-b61a-ff8b55d19999 | -17.12975 | -47.74453 | 2025-12-23 12:18:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4fa82cd4-8191-3046-b66c-cc9d71d0e6e2 | -16.1823 | -47.0252 | 2025-12-23 12:18:00 | TERRA_M-T | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 56e25e2c-df0d-3da1-838d-3d5934c378b3 | -22.96109 | -48.69032 | 2025-12-23 12:18:00 | TERRA_M-T | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| aaa61b7f-6043-3472-9fbd-0ef066f77ff2 | -21.94305 | -49.00414 | 2025-12-23 12:18:00 | TERRA_M-T | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| b0e6171f-1fec-3b89-9218-6e47e2ce9a20 | -22.42802 | -45.45562 | 2025-12-23 12:18:00 | TERRA_M-T | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 132b6b36-7c07-35e9-bb6f-9504d8d5c215 | -18.88556 | -44.78157 | 2025-12-23 12:18:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cf39a18a-e567-31ba-a295-93c9fc6d0a88 | -20.88815 | -45.27294 | 2025-12-23 12:18:00 | TERRA_M-T | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 9aa2e735-1260-32db-a9cb-221a8d5f99f3 | -20.40732 | -47.42068 | 2025-12-23 12:18:00 | TERRA_M-T | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c117186e-dc1c-33c0-a336-7bae2a453304 | -21.12287 | -44.24331 | 2025-12-23 12:18:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| d4b39d6d-9b35-303e-9b61-d55fd183578a | -17.24603 | -48.11074 | 2025-12-23 12:18:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 777d6843-e68d-3fec-a552-ecb108371810 | -20.67376 | -49.98359 | 2025-12-23 12:18:00 | TERRA_M-T | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 18d15882-46ed-3b3a-81e9-74c574d60ffe | -22.58539 | -48.01436 | 2025-12-23 12:18:00 | TERRA_M-T | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 598c16c4-b4f3-3142-8cf8-1922cb0c2a49 | -21.21061 | -43.76485 | 2025-12-23 12:18:00 | TERRA_M-T | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 470fa5c2-6318-3e6c-b4dd-c33695ce6091 | -23.10319 | -48.61022 | 2025-12-23 12:18:00 | TERRA_M-T | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 8.1 |
| faadf702-6730-33ac-89fb-94d87ecede78 | -21.6699 | -47.15384 | 2025-12-23 12:18:00 | TERRA_M-T | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 6760475b-4082-3e0f-bfa4-468fe89c903e | -16.17772 | -47.06147 | 2025-12-23 12:18:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a4dfe58-63ad-3212-b1bf-ee103672e4aa | -21.94693 | -48.99964 | 2025-12-23 12:18:00 | TERRA_M-T | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.1 |
| 2dc079a0-4746-3f0a-80a4-ed09e71a4fc9 | -18.77763 | -46.40007 | 2025-12-23 12:18:00 | TERRA_M-T | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bde302c7-d6bb-3719-8b90-0b9bf3f05a7a | -16.36082 | -46.89872 | 2025-12-23 12:18:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| add4c999-9f40-391d-a7a3-39ce3aea30cd | -22.58698 | -48.00108 | 2025-12-23 12:18:00 | TERRA_M-T | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4b1fd948-78a8-3f36-b24a-d92d2202c846 | -21.94449 | -48.99292 | 2025-12-23 12:18:00 | TERRA_M-T | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| a015c08a-a1db-397b-9ab8-b4fc2786c198 | -25.04259 | -50.58335 | 2025-12-23 12:18:00 | TERRA_M-T | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| be64594a-feba-37b2-9a5e-7a3572b494d3 | -19.58563 | -48.96349 | 2025-12-23 12:18:00 | TERRA_M-T | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 80d645b0-729c-3b05-81a2-7d3973feeff8 | -16.59782 | -45.88189 | 2025-12-23 12:18:00 | TERRA_M-T | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 456a6af9-e5b6-3b4a-ab3e-06ac7557d7b2 | -20.90051 | -45.27443 | 2025-12-23 12:18:00 | TERRA_M-T | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| ca7ba3b6-fa78-3178-92b7-e4adc794bcfe | -20.44815 | -44.76872 | 2025-12-23 12:18:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 9845d1d5-cb46-3add-bb7f-5d215f76ef3f | -23.20488 | -46.58855 | 2025-12-23 12:18:00 | TERRA_M-T | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 3058163d-b6fb-3674-aef9-73c70ae0aa3e | -21.94553 | -49.01097 | 2025-12-23 12:18:00 | TERRA_M-T | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.8 |
| 3455d9c5-fa91-3099-b398-7455e215f8c1 | -27.41382 | -50.62804 | 2025-12-23 12:21:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| b35d4112-1b5c-3fb5-b057-f9c5a237c547 | -27.40437 | -50.62664 | 2025-12-23 12:21:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| eb954316-4ae0-3f87-b9e4-301755392339 | -25.59672 | -50.26341 | 2025-12-23 12:21:00 | TERRA_M-T | SÃO JOÃO DO TRIUNFO | PARANÁ | Brasil | 4125100 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 25102d9c-5cd0-3e2b-867f-a8cee9f4d819 | -25.60929 | -49.16916 | 2025-12-23 12:21:00 | TERRA_M-T | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |


