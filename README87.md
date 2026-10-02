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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2f32263-6356-3560-af96-7cd75f17601d | -11.7379 | -43.4118 | 2026-10-02 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a404120d-4021-38e1-8d16-bec70fccd9b9 | -11.2438 | -44.2626 | 2026-10-02 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 8196a33d-a6f5-3a0b-89f2-9342aee3ffc4 | -11.2434 | -44.286 | 2026-10-02 13:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 224.5 |
| b12f294d-84ee-3f32-b1f1-a3bfd843d4b8 | -11.1615 | -44.6002 | 2026-10-02 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 404.3 |
| 634cbae0-705f-3c2a-bd82-9fa1880e3b3b | -11.7187 | -43.4148 | 2026-10-02 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.8 |
| cc89f231-e85c-3178-b4ff-36701445d1a8 | -11.1424 | -44.6029 | 2026-10-02 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 288bea4e-6872-3cd4-80fe-90cc5f801cf6 | -12.4737 | -44.1435 | 2026-10-02 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 478.6 |
| c14ad2e3-a01d-395f-ba90-8a3edb2246de | -12.9036 | -44.8217 | 2026-10-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 1f4a7c77-9b37-348f-afec-6d5894506976 | -11.2753 | -43.5539 | 2026-10-02 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| af0be683-6669-36fd-add9-3a57ec5488dd | -12.7619 | -45.1696 | 2026-10-02 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 936a99a8-7d8d-3f71-a555-0fa7c968fcb9 | -12.4737 | -44.1435 | 2026-10-02 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 5415b692-5be8-3171-aefd-112dbbe3ea59 | -11.2438 | -44.2626 | 2026-10-02 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 08cc68ab-52f9-328d-aaa1-e642be4f0726 | -12.9229 | -44.8186 | 2026-10-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 267.6 |
| b8738d3e-7cd6-3600-892e-22bf8de76083 | -11.7353 | -43.5542 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 0b18de5a-18c1-3988-9d6c-136d7abea98f | -11.2566 | -43.5331 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 72b31d18-5ec7-36d3-af0b-7c9e4f60c741 | -12.5522 | -43.0877 | 2026-10-02 13:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 285.8 |
| 4e7133b0-32a0-3db4-a665-57d7f7f00043 | -9.7877 | -44.8058 | 2026-10-02 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 283.3 |
| 3cad6b04-8bf8-3a9c-8700-96b71e256464 | -10.9262 | -43.8406 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| fe7bc91e-4ad7-3688-8e2e-01227486d770 | -11.7545 | -43.5512 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 1bc5eff9-6aa2-39d5-bb5c-d30b84aa909b | -12.9036 | -44.8217 | 2026-10-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.5 |
| dd750651-8fda-3e19-a931-e5b94aa482f2 | -11.7379 | -43.4118 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 5af24b04-842b-30d3-8f75-2c96800e0a84 | -9.7687 | -44.8082 | 2026-10-02 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 7ba8d496-a6a9-3b7b-b709-6c9c458ae54f | -12.7808 | -45.1897 | 2026-10-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 503.6 |
| 37cfc2a9-4c0a-315a-a559-2ed232b85528 | -12.7812 | -45.1665 | 2026-10-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 742.0 |
| 23349af4-195e-3ecc-a2e0-9392a0a085f8 | -12.8667 | -44.7346 | 2026-10-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 4990e1b2-1d12-33a2-9340-9c3959917767 | -11.2753 | -43.5539 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 3e4fdc54-9ce9-3e08-bafe-c5305492e041 | -11.142 | -44.6261 | 2026-10-02 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 98c1b490-d3fb-370e-af4d-099a5eb03c3a | -11.2282 | -45.1682 | 2026-10-02 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 31354219-baad-32da-b52b-7f4052318925 | -11.2434 | -44.286 | 2026-10-02 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 329.8 |
| 6777a708-b200-34c3-8980-0bfaa38f6949 | -11.7187 | -43.4148 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 4afd4e6e-e228-36a4-8519-1002d8c9bd18 | -12.7804 | -45.2129 | 2026-10-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 244.3 |
| b363d7a4-d28f-3cc3-85df-318bc1771c1a | -11.257 | -43.5095 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| dc9ba3f9-4949-345f-8cde-2b900708ad6e | -10.303 | -44.648 | 2026-10-02 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 270.1 |
| b7dc8f8b-52f4-397d-a6a6-c516f4f8b94e | -11.7169 | -43.5098 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| ef6775fb-7c8d-38e2-92b0-2830f3f8f449 | -11.1615 | -44.6002 | 2026-10-02 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 563.2 |
| e3af9073-be20-3c74-b4e5-26452094de2e | -10.907 | -43.8433 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 196aa784-f8ac-390e-85c1-e283be24323c | -11.716 | -43.5573 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.1 |
| b7d3e3d0-8fc6-3fd4-977a-d0abfe2b2436 | -12.5329 | -43.091 | 2026-10-02 13:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 353.4 |
| 1c22bd35-07cc-3e34-a46f-d671beca5272 | -12.886 | -44.7314 | 2026-10-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 314.1 |
| 4fb5b128-b1d7-3919-bb0a-0760dead4e14 | -11.2629 | -44.2598 | 2026-10-02 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 526.6 |
| a171bdef-fef9-3f1e-8189-39625268768b | -12.5334 | -43.067 | 2026-10-02 13:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 308.7 |
| 7ec9d3df-0e65-36b5-bd4f-79d20f4879ef | -11.755 | -43.5275 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 7250a872-732d-399b-9d7f-470215bad3b2 | -10.3034 | -44.6249 | 2026-10-02 13:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 9a75e058-e5f6-399d-adf1-55f080e6e945 | -11.2442 | -44.2392 | 2026-10-02 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.3 |
| cc44934a-a133-309b-8a5b-ce1d51157651 | -11.1424 | -44.6029 | 2026-10-02 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| f7fb31a7-2eab-39d9-a6d4-84be60041ea2 | -11.7362 | -43.5068 | 2026-10-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| dc622be4-9860-3049-9532-19a0b872de4a | -10.303 | -44.648 | 2026-10-02 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 227.5 |
| 6df6de2a-4c0a-3121-8042-3384fc65ee6c | -11.2434 | -44.286 | 2026-10-02 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 2735a667-127e-3d56-a0e8-20249889333e | -12.5329 | -43.091 | 2026-10-02 13:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 348.3 |
| fff9b54b-d8d1-3c02-bda7-d77ac012f593 | -9.8067 | -44.8035 | 2026-10-02 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 138.2 |
| be9a999f-a765-305c-a7f8-c71897e119ce | 1.7399 | -50.8235 | 2026-10-02 13:50:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 2d0072a6-7907-3bab-9cef-636d37972d58 | -12.5334 | -43.067 | 2026-10-02 13:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 275.8 |
| f21928ea-9a24-36d6-bad1-2d3cee40e9af | -12.4737 | -44.1435 | 2026-10-02 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 448.0 |
| f49a6b42-3ebc-3aaa-8c48-38d0337dde8e | -11.2753 | -43.5539 | 2026-10-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 3182c71f-22ba-3306-8806-d5a4a7a1e05d | -11.2749 | -43.5776 | 2026-10-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 6c1b7ed8-92be-38e7-bb6d-80b4a483f78c | -11.2442 | -44.2392 | 2026-10-02 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 05b9320c-057e-311a-96c2-3897c6156a91 | -11.142 | -44.6261 | 2026-10-02 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| b167654c-6817-3bf5-9927-645540df07c9 | -12.4732 | -44.167 | 2026-10-02 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 25d81dc9-973c-3573-87da-2b2f42b93c68 | -11.2629 | -44.2598 | 2026-10-02 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 327.3 |
| f711e15e-d7fb-31cf-88cf-6bbf90883f88 | -7.3842 | -42.1039 | 2026-10-02 13:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 2e34a114-20c7-3322-9106-6b06f8817b0a | -12.4544 | -44.1466 | 2026-10-02 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 3259f5be-ffa2-3150-b4da-7ca37b4e2409 | -7.3467 | -42.0839 | 2026-10-02 13:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 622a8355-e9d6-354a-9a45-ba2385ace371 | -9.7874 | -44.8289 | 2026-10-02 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 684f248e-b64f-36b8-9f4c-39aa4e64cc0b | -11.2242 | -44.2888 | 2026-10-02 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 158.4 |
| dd6331da-9fa3-3253-8571-c0ace224f11d | -11.2438 | -44.2626 | 2026-10-02 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| c51b9a91-6fa8-3fac-a9af-71a4f478bd54 | -10.9262 | -43.8406 | 2026-10-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 0b81dde9-414b-399c-be86-bdf61588b324 | -12.886 | -44.7314 | 2026-10-02 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 685.8 |
| 28dbbb49-dec8-3689-9709-70b91410f9d3 | -11.1424 | -44.6029 | 2026-10-02 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 228.4 |
| f63316cb-cdd4-3e84-bfa4-eb70c27b74d3 | -11.257 | -43.5095 | 2026-10-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 3272cec9-58ec-3c09-8316-c3e07fddba8c | -12.8667 | -44.7346 | 2026-10-02 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| f21250e7-bc48-366e-83d7-c16f52e0b18f | -9.7877 | -44.8058 | 2026-10-02 13:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 331.5 |
| 43ecfa71-0942-3be4-a2c3-dc77e9ac482d | -11.2762 | -43.5066 | 2026-10-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 639f0fae-31b5-367a-842a-ec4eda311f8a | -10.907 | -43.8433 | 2026-10-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e5a61805-fd99-3075-b479-abe15d685992 | -10.3034 | -44.6249 | 2026-10-02 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 254.6 |
| a61ce868-6c87-350a-adba-bac152e616c7 | -10.2473 | -44.5628 | 2026-10-02 13:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 88b33861-75a4-3989-a38a-cef3fd68cda1 | -12.8856 | -44.7548 | 2026-10-02 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| e009370c-7a18-3f39-a660-d4b369eddf6f | -14.2531 | -41.6256 | 2026-10-02 13:50:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 121.8 |
| f5ef9c13-ce53-3d57-8350-1e1d930e91e8 | -11.7379 | -43.4118 | 2026-10-02 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| a8f018a6-9cae-32b1-b378-7830ce759c03 | -7.0451 | -42.0666 | 2026-10-02 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| de6df63f-8d2a-308d-95ff-7ef7f9e98fa3 | 1.7399 | -50.8235 | 2026-10-02 14:00:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 1f1265b7-f580-3038-9dd8-23001c3163c5 | -10.303 | -44.648 | 2026-10-02 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 267.6 |
| 03396d9a-b4a0-3da9-acd8-9f1322e609fe | -12.8856 | -44.7548 | 2026-10-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 5e28a6fd-a11c-3052-8ae1-2b320b264334 | -11.2566 | -43.5331 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 9672f970-36b5-374d-85f7-0716841e4a54 | -11.2629 | -44.2598 | 2026-10-02 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 358.0 |
| a2d97428-92d2-3bb7-b0de-87be38418073 | -11.4123 | -43.3913 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.4 |
| e1695b92-14d7-3f06-b6de-c4f4ded29aa9 | -11.2749 | -43.5776 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 4b749d3c-5361-3945-92ca-22b8323fa3a8 | -11.2438 | -44.2626 | 2026-10-02 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 15e31a79-885d-3e02-affa-9c3311a4fac3 | -12.9229 | -44.8186 | 2026-10-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 297.1 |
| 7bdc2282-82e9-333f-8c36-8128ccaada30 | -10.3034 | -44.6249 | 2026-10-02 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 255.9 |
| 4f9b815e-72a3-36f4-b903-f93d35755583 | -9.682 | -45.5507 | 2026-10-02 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ea3f183e-db61-3162-a8d8-cb676dfc2602 | -12.4737 | -44.1435 | 2026-10-02 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 279.2 |
| f3751163-4925-3759-8332-42939007e8a3 | -9.663 | -45.5529 | 2026-10-02 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 07fb6abe-1891-3985-be2c-1dc91fb233f5 | -7.064 | -42.0648 | 2026-10-02 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| c34b9e11-8517-38d6-b4bf-dc218b351eb6 | -11.2434 | -44.286 | 2026-10-02 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 463.5 |
| 777d0d39-a427-3b4d-9736-4d338924740b | -12.4544 | -44.1466 | 2026-10-02 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| c088cf66-252b-344a-81e3-23dd9cda3f07 | -11.142 | -44.6261 | 2026-10-02 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 144.5 |
| d6bac7a0-73a4-376f-a118-2ac6aac2fcc0 | -11.257 | -43.5095 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 387623dd-d0c2-36f2-8a47-d1c0296840f4 | -11.3927 | -43.418 | 2026-10-02 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| a3503c89-7aa1-3a1b-bad3-ecbf70cbb7f5 | -11.2466 | -45.2116 | 2026-10-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 5ab19add-abd9-3541-adc4-b5c91f0378e7 | -7.0448 | -42.0906 | 2026-10-02 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |


[Clique aqui para ver as próximas entradas](README88.md)
