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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cee6573c-5089-3a51-a728-d815da0864df | -7.2901 | -45.3683 | 2026-08-25 11:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8d20e3df-bb35-3302-bec3-f4a4728a59b4 | -6.9873 | -59.2389 | 2026-08-25 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7f488f51-2eb2-342d-9330-b1cac4259b31 | -8.658 | -47.3193 | 2026-08-25 11:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| b44b843b-01fa-3c75-aec1-6ac9c2cd0a0c | -6.6357 | -45.1752 | 2026-08-25 11:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| df8f5c32-5bf3-3c4c-99b0-bf3316cff992 | -13.3402 | -48.2079 | 2026-08-25 11:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 65264fdf-20e8-3cc0-8bb2-da10f8adac99 | -11.4494 | -44.5353 | 2026-08-25 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| c5200079-1e7b-3f68-8cf9-041011a75fa2 | -7.2903 | -45.3456 | 2026-08-25 11:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 764076d5-b3f0-33b7-8dc2-037bae7076f3 | -6.64713 | -45.1746 | 2026-08-25 11:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 93718294-655e-3c66-98d0-b35563e3b118 | -5.79877 | -43.64548 | 2026-08-25 11:32:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| be45384e-3257-3a84-8c10-e0814f1f3bb8 | -5.05689 | -42.63328 | 2026-08-25 11:32:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c4761abf-79ed-3a42-a3bc-f9f142776880 | -6.31917 | -45.70381 | 2026-08-25 11:32:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6c0dda18-598a-3f1e-814a-f04d13e521e1 | -6.44811 | -43.09765 | 2026-08-25 11:32:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 56b70ec8-fbae-3dcc-b253-d058f57bea09 | -6.45697 | -43.09888 | 2026-08-25 11:32:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cac2c9fb-97f1-3559-9783-61978ad8aa19 | -6.68037 | -43.41041 | 2026-08-25 11:32:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 979c9303-43b4-3cd6-aefd-a1c780af4d2a | -3.42049 | -39.2716 | 2026-08-25 11:32:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 7d07dcad-5b79-39bb-877e-dbd13e34ec72 | -6.67911 | -43.41926 | 2026-08-25 11:32:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 69bc4276-0dfa-3cad-9ba3-de068f1b38e9 | -6.64848 | -45.16525 | 2026-08-25 11:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d420d4b8-891a-3216-ba10-4411979453d6 | -6.64213 | -45.14528 | 2026-08-25 11:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9ac1d7aa-d0c8-3bb3-986c-aed280cb0a94 | -6.62124 | -41.72467 | 2026-08-25 11:32:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1f7f2767-299d-30f5-a880-3efecd1d322d | -6.63942 | -45.1639 | 2026-08-25 11:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 5603cc55-0892-37c3-8e05-b1b521e04caf | -4.82338 | -42.78815 | 2026-08-25 11:32:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 18b6d37a-3ebe-3fab-8f62-2a32274f615c | -6.63806 | -45.17325 | 2026-08-25 11:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 3580cd67-bf68-3743-8edd-73c3dc1f1efb | -3.91215 | -38.62224 | 2026-08-25 11:32:00 | TERRA_M-M | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| ce811098-dc42-3303-8e6d-e5eaa5285eb1 | -6.62259 | -41.71486 | 2026-08-25 11:32:00 | TERRA_M-M | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9972bae4-fb37-34b2-a31f-a5bfc1aefe7e | -7.28457 | -45.35835 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| d54bd1a0-f9a8-38f2-90a4-bee56167fc84 | -7.27672 | -44.0691 | 2026-08-25 11:34:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ac1f76de-b5dd-3e0b-a6ef-ab69a16539fd | -8.10223 | -47.46827 | 2026-08-25 11:34:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ea7210db-e487-33f7-b43a-d6aa472e6ed8 | -14.99561 | -44.43262 | 2026-08-25 11:34:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d43b36ef-f985-3e72-8fdc-c45633b57be4 | -7.01818 | -42.7832 | 2026-08-25 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 1e245a03-b690-3ad9-8974-374eee624232 | -8.16584 | -46.70184 | 2026-08-25 11:34:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| d19dc6f4-6ad2-314d-baff-1a1ff0dfa80a | -11.88454 | -43.82227 | 2026-08-25 11:34:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31d598eb-da36-3580-be0a-02626d808f10 | -12.73856 | -46.4746 | 2026-08-25 11:34:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5d55f3b1-88c6-3cbf-92b5-332d2dfa2b83 | -9.97846 | -48.32149 | 2026-08-25 11:34:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 880aeefc-ebb0-37c7-a3ae-50734b323fc3 | -10.05494 | -48.45231 | 2026-08-25 11:34:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ec286b6f-d031-38d5-9e23-91ae152bfe43 | -7.29228 | -45.36548 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 7385f6f9-1c0d-3b15-bac5-d084fb439cb2 | -8.08287 | -47.5267 | 2026-08-25 11:34:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 7dd5b419-3081-3cf9-86b6-c10c05e6ac89 | -7.24756 | -44.20954 | 2026-08-25 11:34:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 66c044e8-1e4d-3f59-9e18-2d863fb3378a | -10.37055 | -45.06432 | 2026-08-25 11:34:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5ce3c6c6-9b6a-3098-833a-3f33e97557d3 | -12.7595 | -46.45499 | 2026-08-25 11:34:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bcc5c734-0324-3103-9f3c-24649de1c589 | -8.93572 | -45.73492 | 2026-08-25 11:34:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8bcc9023-b04b-33b7-80ea-e2c372490e6c | -14.63595 | -41.96216 | 2026-08-25 11:34:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 45.9 |
| 37334640-757e-3c7d-afa6-556822d1bc48 | -11.04876 | -47.09781 | 2026-08-25 11:34:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d01b3ece-36e1-3fd9-a2b1-933b04b08368 | -8.081 | -47.53881 | 2026-08-25 11:34:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 6e9ab6cc-f96e-38b6-92cc-8eb79afc341a | -11.78171 | -39.99089 | 2026-08-25 11:34:00 | TERRA_M-M | PINTADAS | BAHIA | Brasil | 2924652 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 61f758ba-588a-3f9e-afd0-f862d706357b | -12.00574 | -45.94015 | 2026-08-25 11:34:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aecb5db6-b8d7-3ef6-84de-89bae4afcfc1 | -15.26873 | -52.77357 | 2026-08-25 11:34:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| d94714a8-b1c1-334c-80ff-097c0e83d8c4 | -7.28428 | -44.07918 | 2026-08-25 11:34:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 64cfb768-994c-39de-ac98-ec553012e9d1 | -13.82393 | -42.17439 | 2026-08-25 11:34:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ff900961-9c29-3a57-9b00-8c8593a3ccf2 | -15.26464 | -52.7966 | 2026-08-25 11:34:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 75ab091a-8691-3bc2-8fcc-d299e674a14c | -11.27924 | -47.04941 | 2026-08-25 11:34:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e1c4941c-b1ee-3c28-a55d-ab383a27db3d | -7.02712 | -42.78443 | 2026-08-25 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 41ce22ee-eab7-3acf-89d4-7ad2ae48a751 | -7.15255 | -42.74268 | 2026-08-25 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 49727690-dd83-3529-b7c7-32a472341bd3 | -12.84389 | -48.49851 | 2026-08-25 11:34:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 43502d4e-6e07-38bd-a7a0-2f21360f946c | -11.04085 | -47.08587 | 2026-08-25 11:34:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 7dcc7123-c281-3eb5-9c56-d3934175d746 | -12.87421 | -48.50327 | 2026-08-25 11:34:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b6cb4872-222b-3213-b94b-ee1c931d232d | -11.81626 | -47.64467 | 2026-08-25 11:34:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| ca1c0f01-9633-3476-a642-beea7e6aa2c8 | -15.11471 | -48.02036 | 2026-08-25 11:34:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| df22ac88-54b7-3fd1-9a92-9e3da1c5894b | -11.99692 | -45.93277 | 2026-08-25 11:34:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 211686ec-3e4e-3365-a013-ca21c6938977 | -10.57538 | -46.31051 | 2026-08-25 11:34:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 88ac6410-fc60-34b3-b7d3-f29de88d00ab | -11.94554 | -41.31661 | 2026-08-25 11:34:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 0cb3a689-6dca-30d7-ab51-5c8842197345 | -7.90826 | -46.37729 | 2026-08-25 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 7a1632b6-35f0-3e8d-a115-f79a12da3a5b | -8.08472 | -47.51468 | 2026-08-25 11:34:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6724ba74-1ae9-3884-bb99-e474babc648a | -12.00437 | -45.94941 | 2026-08-25 11:34:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ecb25601-3098-3879-b84b-5eb68d110838 | -11.09743 | -46.15425 | 2026-08-25 11:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6cc65ebd-05b5-3ebc-8c96-c9fbaf39e6c6 | -7.2579 | -45.85164 | 2026-08-25 11:34:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| fd81234e-9d12-3780-8d09-ecf84235adbd | -13.35972 | -48.21568 | 2026-08-25 11:34:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 9757ee21-93a6-370d-bf25-0de179a49dc5 | -13.6645 | -51.85014 | 2026-08-25 11:34:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 083c8644-c0e7-3559-b667-5a4514c6aa2c | -14.43667 | -43.73702 | 2026-08-25 11:34:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 54e627c3-b093-3f09-9c14-b4bc7b2b493d | -13.34793 | -48.22655 | 2026-08-25 11:34:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 25.6 |
| d9dfa38a-1a6b-3a26-9e07-d72714fa59e0 | -12.71874 | -48.38047 | 2026-08-25 11:34:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4a503a4d-0503-33b8-b56f-aa0405d344a2 | -7.89885 | -46.3755 | 2026-08-25 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d1e76b84-1bb4-3504-a64a-0459f5bc767c | -8.59823 | -47.44217 | 2026-08-25 11:34:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0a1721a3-7fc2-360f-a368-17236ce8549d | -8.93432 | -45.74443 | 2026-08-25 11:34:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 477de4e5-52ec-325f-a58d-bcf242bf4209 | -7.29367 | -45.35607 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| bc2c4127-216f-37c4-ac27-1f3c4fbf1511 | -11.42954 | -44.56368 | 2026-08-25 11:34:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 6e9557e8-c785-31fa-907a-bc60dd128b26 | -13.33994 | -48.21319 | 2026-08-25 11:34:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7e69efdc-747c-3fbd-a69a-a1174dcbad4c | -7.44075 | -43.12086 | 2026-08-25 11:34:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 90fb4dc0-4bbe-32c7-8a72-260c46b6daf2 | -11.13851 | -44.47586 | 2026-08-25 11:34:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 0c95d400-e296-311a-82c5-25b71d5579ca | -7.24883 | -44.20069 | 2026-08-25 11:34:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3a164ea9-2ed8-3771-b8e2-34b1be0741c4 | -8.92801 | -45.72421 | 2026-08-25 11:34:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cc8f9b40-378e-3244-a66b-91e4f3b39f78 | -11.43464 | -44.52787 | 2026-08-25 11:34:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d3b43295-632a-3429-a06e-4a0745c447c1 | -13.35151 | -48.20367 | 2026-08-25 11:34:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9812233d-a802-3ece-9370-9023abfa3b68 | -7.26501 | -45.36514 | 2026-08-25 11:34:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| feb5d599-d6a9-3806-8a57-1e42c44da072 | -7.44328 | -43.10291 | 2026-08-25 11:34:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 754f3048-c49a-3273-8e10-4f205225ca55 | -11.42198 | -44.55347 | 2026-08-25 11:34:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 5da32f2c-079a-36d4-8ba0-7f235bbffa47 | -11.43081 | -44.55473 | 2026-08-25 11:34:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1031.7 |
| 7ec2b5b0-27ee-303d-ab8a-8dd8925e7aa0 | -12.78325 | -48.36095 | 2026-08-25 11:34:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3162a906-76e1-33d5-90e6-c2d5d2b2fbfd | -14.38984 | -51.76247 | 2026-08-25 11:34:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c390ee75-7ba5-3766-8324-bf33d51e71cf | -13.66333 | -51.85562 | 2026-08-25 11:34:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| f79e3bc5-d9f2-3c61-ab8f-69f70e40efe3 | -11.43837 | -44.56495 | 2026-08-25 11:34:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| c033dded-1459-357c-9e32-1cd56aa24d25 | -11.99066 | -45.91294 | 2026-08-25 11:34:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 41.3 |
| bce51db3-043c-3e2f-9fd9-62b659f3adc6 | -7.9019 | -46.35516 | 2026-08-25 11:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fd456a92-6451-347a-9cb3-1fbaca849d4e | -7.01691 | -42.79227 | 2026-08-25 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 75a3e063-b92d-32ba-a458-28e1cd403fdf | -17.42539 | -43.81033 | 2026-08-25 11:34:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8cb3e99c-950b-3494-8246-1c6687fd4140 | -14.31557 | -42.15389 | 2026-08-25 11:34:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fb8640e4-35d9-3c5f-b575-47fc8e3f4ca6 | -10.37185 | -45.05534 | 2026-08-25 11:34:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 05ba2d3d-c0f8-39ff-854e-1f17e6efbbf3 | -11.03927 | -47.09629 | 2026-08-25 11:34:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 53b197d5-0500-3e2d-a212-425c68825eb3 | -14.32189 | -47.23468 | 2026-08-25 11:34:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c2ce6658-3d13-3ffe-b5ca-acbb7b1b090e | -8.15622 | -46.70034 | 2026-08-25 11:34:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| abb714a2-520a-3357-acfc-4e6aaa30f5d2 | -10.58311 | -46.32156 | 2026-08-25 11:34:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README71.md)
