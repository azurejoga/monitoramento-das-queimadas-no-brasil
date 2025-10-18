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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8e1d1d7-3a45-3752-a0ae-bf6235fd60b7 | -13.46637 | -48.11251 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ba314b8-2409-3fe2-a591-1257277ee051 | -15.7927 | -43.64556 | 2025-10-18 04:32:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d047b058-047c-3276-a585-a52f391f2b8b | -13.42595 | -48.0876 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edf0a15d-5fc8-33cb-9380-ce8fe5e2e5e4 | -12.17748 | -45.07948 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c4432a8-a1b5-34e3-b713-c1ca67a96db0 | -15.51542 | -50.38425 | 2025-10-18 04:32:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0030a2f2-df30-30fb-abb2-18cbd4d1a342 | -13.46332 | -47.98091 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c38b96e-bd73-357d-b28e-6fff8be10bd7 | -13.22904 | -43.98182 | 2025-10-18 04:32:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a5616c6-b394-3dff-9e26-e1dc55a03334 | -13.43645 | -48.57886 | 2025-10-18 04:32:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f867ba86-4785-36ba-9db9-3b77e1f4e71c | -11.53952 | -49.92477 | 2025-10-18 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca5ff98c-1449-313c-a32a-0e7856b4b65d | -13.17981 | -46.43311 | 2025-10-18 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b3946d9-1b5a-351b-bf57-79b3eec38726 | -12.15574 | -45.08028 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3a5aa6c6-6cb3-315a-9757-f6c39fc6e66a | -14.92185 | -46.71998 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab496713-c65f-3933-9d50-76c4adde8a3e | -13.19938 | -48.32059 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a1d444d-c973-32e8-9e2a-fe759dc18f32 | -18.40476 | -41.82453 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 17a7d82f-90a0-341b-95d6-d56a744afef5 | -10.98118 | -47.93072 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62f62aa6-e27b-30b6-a56f-71667625280b | -12.9955 | -47.29639 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc0bff71-ba23-3561-aa5f-956c7830e91b | -12.34194 | -46.73856 | 2025-10-18 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22122bf8-17b3-3d10-aeae-12662da9b1f9 | -13.20578 | -46.42219 | 2025-10-18 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b12a8c2-8961-3087-bc38-48285cd77a4c | -15.59943 | -42.39186 | 2025-10-18 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dedb13e-d06f-3cb9-ae55-10356baf7936 | -11.20088 | -47.82565 | 2025-10-18 04:32:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec8e9274-51e7-3b7f-99a1-774bc8bda734 | -18.40362 | -41.83427 | 2025-10-18 04:32:00 | NPP-375D | JAMPRUCA | MINAS GERAIS | Brasil | 3135076 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1bf0a0fa-6d63-3433-81c0-f5ad702ecf53 | -17.96248 | -46.74902 | 2025-10-18 04:32:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2456032b-277e-3830-bc20-873cfb73c5aa | -11.61196 | -44.09186 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4cd6f000-000c-35aa-a259-8f19dd5ef8da | -13.46331 | -43.76604 | 2025-10-18 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65305b08-892d-342f-9385-c2964884edb5 | -13.63617 | -44.42085 | 2025-10-18 04:32:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89f0a16d-fd70-3e02-a56e-cc9cc575d897 | -11.00068 | -47.91579 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7296e137-8d5b-3e30-a94a-eda29cdf9806 | -14.92172 | -46.71984 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce96b9fd-cc4e-3946-860b-ba2715fb8cae | -14.50146 | -45.61045 | 2025-10-18 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ef71cd0-1d29-38cf-abf2-1fb0697ab785 | -13.04039 | -46.97419 | 2025-10-18 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15352bda-3b91-3d7a-8585-81e95ff3ac91 | -13.42649 | -47.97903 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dfd9fc0-ec97-38ff-a2b3-80f4373d9186 | -12.49201 | -45.4994 | 2025-10-18 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efb22172-842e-3c6b-a76b-b1e5ba1ad188 | -13.42204 | -47.98558 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d93f333c-e6f8-3ecc-9005-88af9e76f973 | -12.15165 | -45.08362 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bb61b8cb-479e-3d73-8494-541f08d81d70 | -17.50189 | -43.45994 | 2025-10-18 04:32:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e172cc2-bb12-3c18-b47c-4c95b242b08d | -15.08283 | -48.45664 | 2025-10-18 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69baf364-35e1-3e72-9ea1-0236b8dce465 | -13.77091 | -48.23605 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6af3fc8-31a5-322d-8c25-9fba1ec2e4e6 | -13.50877 | -47.99568 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d89374fe-8c22-3822-8faf-a7b641e003e2 | -12.39162 | -47.20359 | 2025-10-18 04:32:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 37d8f520-7d2a-3044-af9d-d5fb1f783963 | -12.60174 | -52.81258 | 2025-10-18 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b75d6987-a8db-3f88-a97d-a9a2767f49d9 | -12.16513 | -45.08992 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ee6c48c-4f37-3e51-a045-1490bb6bcf0d | -12.78739 | -48.62882 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b6dba65-d70d-360e-97af-a9055eca2b4a | -12.80119 | -48.64971 | 2025-10-18 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ec0a988-ead5-3edb-9343-0ec3b71bb148 | -15.05577 | -48.74947 | 2025-10-18 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bb46412-968b-36b4-a8f6-e774429fe549 | -13.62015 | -43.9593 | 2025-10-18 04:32:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b96cfe5f-7eb0-3155-a23b-67b728e8c365 | -16.64722 | -52.5223 | 2025-10-18 04:32:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e931dd2-d7c9-31ff-927d-02a9b2ef06ce | -13.40709 | -47.97217 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e1ee471-f182-38c1-bbab-3c4395832771 | -11.13789 | -45.07806 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c489c0f6-72e7-3f6c-80a6-d7850ce954fd | -13.42593 | -47.98258 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74c33361-93de-3cca-8139-5b3faae63410 | -13.44512 | -47.92327 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3aea996e-53eb-3bdd-987b-f69c3d5aae1c | -14.90467 | -52.38663 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b01093f3-1727-379a-abc5-8777adf6ff85 | -14.90681 | -52.39669 | 2025-10-18 04:32:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d17320b-7182-32e5-8754-3ebbe01896a6 | -11.35431 | -44.27628 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e81610e0-18dd-367b-b4ae-e31422b0ce36 | -11.3712 | -44.28748 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d184b5a-9d83-34fd-ad9b-4dca2130e136 | -12.98542 | -48.45616 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 020a079a-2687-39b4-8338-5e94cdc10165 | -14.48172 | -48.60814 | 2025-10-18 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f192b6c-173b-3427-bb4e-37a242c8f76b | -13.48389 | -47.95881 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a87be7cb-bff3-33e9-84a6-dff78bc1f6e7 | -13.73625 | -48.32513 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17dcf2fa-d80a-3d3e-a97d-f6346e4484fb | -11.37182 | -44.28325 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f3769d9-f5b9-3e7a-b60f-55140445d4a0 | -13.51983 | -48.01208 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 564ba18f-ee71-3da8-a037-3c21947bad6c | -13.45363 | -48.10675 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 424c8444-48f8-3ab3-8e0f-aa87d667692a | -13.45639 | -48.11086 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de93e8e8-3f0a-3ab8-a6e5-7d4eb1222110 | -11.37104 | -49.37811 | 2025-10-18 04:32:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c2b98cc-5c54-32e8-8292-ba0561aa901c | -11.54302 | -49.92538 | 2025-10-18 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b46ba754-6996-3429-bc5d-3d066a6ab117 | -15.46957 | -42.88428 | 2025-10-18 04:32:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6bc7dd83-c2ae-345d-8180-90f8ddbf45ec | -13.7483 | -49.80032 | 2025-10-18 04:32:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98ad40e0-d42e-326d-88ff-b61db4e6fcf0 | -10.95483 | -49.7696 | 2025-10-18 04:32:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91917d36-27e1-3bd7-afcc-0a4f4786bbb3 | -13.52929 | -47.99543 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 743f2d07-d8e0-3a83-847f-5dec92acd38b | -12.15223 | -45.07969 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| bc46971a-e468-3ebc-92a7-b4241d2a0ce5 | -15.60374 | -42.39237 | 2025-10-18 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c457cd31-b263-3377-a769-3e6ce17fff8a | -11.36144 | -44.30329 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ffe4463-bb1e-3a1a-97e0-2e59b02304a3 | -11.58029 | -44.05147 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef324883-39a1-308f-80c6-b2b0d4d43997 | -11.13498 | -45.07364 | 2025-10-18 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a84d7d4-3991-3068-8c81-941dd1d1f7a1 | -13.63432 | -44.42208 | 2025-10-18 04:32:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c704f4fe-0941-3fb8-ae99-23e096e27e3e | -12.98599 | -48.45262 | 2025-10-18 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f585498c-7de6-3d76-89b8-a9e213bc697a | -13.26973 | -46.43929 | 2025-10-18 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 797b4c27-3b60-326a-b2ce-b681174fdb94 | -11.38082 | -44.29759 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de86660f-17c2-3c25-a0de-69dc1e0b8cf5 | -13.0763 | -43.06408 | 2025-10-18 04:32:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b4b29bb3-0e7a-3b48-804d-859944ee31f9 | -13.69992 | -47.65574 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65a9ae6d-62ad-35a6-a778-1e3c3479d0e2 | -12.15693 | -45.07217 | 2025-10-18 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7346786-e4e4-3be0-a7df-3a07fbf83860 | -14.26345 | -51.86807 | 2025-10-18 04:32:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98205e07-a30a-31c0-9bef-e93f11273a63 | -13.70321 | -47.722 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97804930-a5fa-3623-95da-478369b30b9f | -14.93759 | -46.70687 | 2025-10-18 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d72f41b-0963-3bd1-ba76-45af9a12155c | -11.61388 | -44.07878 | 2025-10-18 04:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b1d770d0-2ab6-3ef3-9c5f-649d207c86a4 | -11.51639 | -44.0619 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b3fd1b5-2fca-3b08-b027-379b9bafc2b2 | -13.77424 | -48.23661 | 2025-10-18 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0cfab3e-ad0e-329e-a3cf-fafd28d37210 | -14.42954 | -48.06077 | 2025-10-18 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 853c620f-254b-3132-82cf-fe0682c0702d | -12.9701 | -47.93617 | 2025-10-18 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9d5625d-301a-3e62-bf18-e46028e55d0a | -11.35794 | -44.27683 | 2025-10-18 04:32:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe02577d-df46-317e-991e-d7ca4e744273 | -15.60302 | -42.65837 | 2025-10-18 04:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa7ef76c-f3f0-3a67-9830-6631444c9c06 | -11.00244 | -47.88334 | 2025-10-18 04:32:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c7fc6c6-4cd5-3576-a4e0-8d723706b170 | -10.88019 | -47.46312 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 842e9388-499c-3d4f-8671-6db865ac4448 | -16.19526 | -44.21857 | 2025-10-18 04:32:00 | NPP-375D | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bfa3fad8-9f90-3085-baf1-c3552b041c5d | -10.92926 | -47.57911 | 2025-10-18 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 185274be-e3c4-3c13-ac41-ed2d8e07ca85 | -11.36276 | -47.29946 | 2025-10-18 04:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b21fadd0-14be-3fba-bb83-eb0811c7ea8d | -11.48473 | -44.02145 | 2025-10-18 04:32:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78e0ff80-312e-33da-9e1f-f19b21ad17b6 | -13.42705 | -47.97548 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79ba4e12-5de1-337c-b6d9-855665dd3c59 | -13.73607 | -44.22503 | 2025-10-18 04:32:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 371978c0-37f8-3c33-9bad-085000412dd4 | -13.93109 | -48.6758 | 2025-10-18 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c558cf2-1a65-315d-9e7e-6fbb61ecc323 | -13.45566 | -43.7649 | 2025-10-18 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7df9430f-890a-3c16-9b50-9346b7b469e8 | -13.48112 | -47.95471 | 2025-10-18 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README62.md)
