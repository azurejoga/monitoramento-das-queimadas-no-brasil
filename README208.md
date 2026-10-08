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

## Dados Diários - Página 208

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8293b9d-66d7-309d-8e4c-0b46cdc41a71 | -4.43121 | -55.15824 | 2026-10-08 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd25680b-81ea-3077-bed4-d510b3299b89 | -6.44541 | -52.70448 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| eff70bb0-fdb9-3b6e-9e4e-aae48de74300 | -6.85482 | -55.77506 | 2026-10-08 12:19:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7f929ff-b8e1-3565-b592-11f0b7cfc231 | -1.90933 | -55.5116 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2b1ffa6f-b5aa-3936-b907-4322680bbff2 | -5.7388 | -53.45306 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 90dfc763-f741-3631-b34b-29d3b5481312 | -3.59294 | -54.56477 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6c49bac6-56e5-3c3f-bfc0-994493cc84ee | -4.05848 | -55.32455 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b0e9b205-2221-306a-922c-a20d2d105f81 | -7.88289 | -55.00658 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6f8fc847-8b68-35ac-b727-1fb7ecb6e41f | -2.71694 | -57.46707 | 2026-10-08 12:19:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| c9fdeec8-25ee-3e74-94f8-4d475b4d3130 | -2.93685 | -54.05461 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 29c8a394-db16-3c3a-8a80-38bfc79769c6 | -3.31392 | -53.86636 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 736c63c3-cea6-3fc0-94d2-0832aa7bd24d | -3.71132 | -57.22771 | 2026-10-08 12:19:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 7ce8279a-fef7-3c23-955d-b3fdcca36322 | -1.48001 | -54.63606 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 940704e5-1983-39eb-b01f-50a8ca529cf7 | -2.50314 | -56.06498 | 2026-10-08 12:19:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 49ae416e-4c08-3a47-b441-d4a800414af3 | -3.09713 | -53.96233 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 579a8751-fd7f-35ea-b2e7-565e077fa4ba | -6.23349 | -52.67703 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c5e13e05-4f56-330b-9116-167030f6b9df | -4.74937 | -55.6588 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8a11ad17-f99d-3988-bc0b-d2d151cf2a39 | -2.46515 | -56.06217 | 2026-10-08 12:19:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 826226f5-b921-38a2-b794-dbf259c4a6f4 | -6.26705 | -52.87592 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 2e791897-c139-33b6-bc12-e4e890ada271 | -4.98237 | -56.21941 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1a739240-1b30-3301-b1e5-b2f425854423 | -2.72743 | -57.45884 | 2026-10-08 12:19:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 73881bea-f8b0-31e2-bae5-e7a3251e99a2 | -5.86053 | -53.45424 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 924b8d79-054a-36dc-9937-c16ed8decf82 | -3.44824 | -56.93419 | 2026-10-08 12:19:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d1b7be77-cde5-398f-8b6e-0b7c52279823 | -3.09529 | -59.19281 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 90ef570c-da3d-3882-b5be-4aebe8da7bdd | -3.60194 | -54.56604 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a7ee4307-2371-3cdb-be27-76638675297a | -3.12037 | -53.79763 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| d6a9aaa4-bd47-335c-8169-4d6f03bc60a0 | -2.84278 | -54.12841 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d9db4e1f-512b-3e28-8169-19b509ae86b1 | -6.11645 | -55.69949 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2e5fa4e0-045f-33c9-960d-edb21ba27304 | -3.01359 | -54.74498 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3a013763-a406-347a-9e91-757c334b929e | -4.93133 | -55.86681 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9d1fe049-dc57-364b-883f-5c92295f38f6 | -1.82755 | -55.04193 | 2026-10-08 12:19:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2f9d8248-692b-39e3-b9b3-063bfb5ef16d | -3.61309 | -55.4659 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| af8033fb-6e37-373e-a974-256938d32f85 | -2.92738 | -54.12078 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 25e6e8bc-c960-3fd9-8f3f-204915edfd60 | -3.17627 | -58.6328 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| dfd6bfc4-18a8-3b28-bf10-539c9d86c779 | -3.68166 | -55.94597 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5efcfde1-0f6d-3583-91c8-b6771b01d63c | -3.57598 | -54.68384 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 10bda4ae-43f6-30d3-af6c-f68a1aed5d6b | -3.50206 | -59.28234 | 2026-10-08 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b0d5ed69-8ce4-368a-ba51-bbed00dfee0d | -11.86343 | -48.00677 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1fab5a6c-7130-3b71-93e6-f830318c558e | -6.00898 | -53.49726 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 45f5c634-faef-3fdd-b17e-040c079677e9 | -1.48283 | -54.53962 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3cd2f249-84d1-3ffb-9280-aa8a703b4fd3 | -3.0801 | -53.95024 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| bf7a2edd-3102-3a0c-a37e-80abb4992e53 | -2.8843 | -54.87675 | 2026-10-08 12:19:00 | TERRA_M-T | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f0eb795d-be0a-3cca-91cf-545a27e82b2c | -5.9129 | -53.87949 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7cbaf19c-565e-3005-996a-eb1a18f703a1 | -2.84263 | -57.48751 | 2026-10-08 12:19:00 | TERRA_M-T | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dcfe7dce-db96-39c3-9e8b-ad1f92e4aefc | -11.85968 | -48.04245 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 8a52da7c-c42e-3e0c-88fd-cb02b9c3f44f | -3.54908 | -54.68015 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c22db3a9-f83c-3753-9692-0ef2c8bd67e1 | -1.32176 | -53.1345 | 2026-10-08 12:19:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4e80ae9c-3513-3fd3-ae7a-061cb187e9b7 | -3.07875 | -53.95989 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| e0fa5f6a-eb66-391b-8f4f-77cf0b0f735b | -6.38844 | -52.73512 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 2dcbda95-2faa-3384-b03e-fe44bf067a05 | -2.49994 | -58.07131 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 85567d63-1fb1-3486-8a11-878483cc9468 | -5.69977 | -53.44785 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c778f36f-f4ed-3c12-a1f0-08976a80c680 | -1.32811 | -55.43261 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 248ec3a3-8e18-381c-8403-05bf36dc5aac | -2.999 | -54.06946 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6e27cb64-007d-3694-bf32-34ca2e2acf91 | -6.24383 | -52.67859 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8567ecf7-5ac8-39fa-b71e-dd45aedec4fa | -4.94008 | -55.80529 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2cf197be-7eea-3ddd-8566-443019d855ea | -7.87031 | -54.69988 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 86747372-4e28-331a-9fbb-4994d470c2a0 | -1.44862 | -54.46167 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2297f67a-e4b0-31cf-8c0c-3f9674c150c8 | -10.4239 | -47.25715 | 2026-10-08 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ca980727-929e-3141-a006-7a44dff7b03f | -2.98318 | -54.11551 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 256b3d48-77de-3c70-8713-b5d698995478 | -3.8691 | -56.00822 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8cbe4fd-f3fc-3743-b2b8-9ac0a57d891e | -1.72306 | -55.44075 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| dfddbddc-e991-31f4-b1be-c2d54b4ca37d | -3.94817 | -56.01915 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 913ff991-8c7d-39dd-9d2e-c3137a2f01da | -3.10632 | -53.9636 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 874e79bb-94f9-35e9-9f60-a96dbca0084c | -3.48005 | -59.57225 | 2026-10-08 12:19:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cc7e998f-aef4-3da9-afa3-e5a3ed56a0dc | -3.91294 | -55.88948 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f35d6dc-4f3b-3d65-9b0f-c10d9b6e33c4 | -3.14107 | -54.36875 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 402ce4a3-7da8-35cb-bad0-45e6a2ddffc8 | -6.63459 | -50.0665 | 2026-10-08 12:19:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 78728713-dcdd-3255-a5de-2fee32947877 | -2.3948 | -57.89611 | 2026-10-08 12:19:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 84227af5-e9f3-3511-b483-bf331c7f3401 | -5.29714 | -60.09232 | 2026-10-08 12:19:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e5939bb8-1bd7-3b6a-bb17-89d0a6aa31b3 | -2.90433 | -54.02113 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3692ce57-0aa9-33a3-bcd1-3213ea71fe09 | -6.1994 | -53.14975 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 349858e4-58fd-3024-bda4-17920c6f840a | -3.12204 | -54.17569 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 201f2a9d-0e53-3244-8efa-7a0a2de0a788 | -3.17782 | -58.62205 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8f77da12-55a4-36af-ae88-c93b76586224 | -3.84462 | -55.97205 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f8365461-6f84-3879-b3f6-b97dc092b293 | -3.68041 | -55.95471 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6091d6a2-84ac-3e8c-b70c-fc41dadf1c48 | -3.00679 | -54.08019 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 32d06a8e-51dd-3687-b3ed-fa618de2e116 | -1.42696 | -54.61398 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5392a012-6498-30be-bad2-3369fea03094 | -3.55681 | -59.46555 | 2026-10-08 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7a2e4a58-5e25-3fc3-b885-d9c17bf2a0d9 | -3.58364 | -54.69419 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 97d38e51-befb-3bb3-bbe8-37ff716e443d | -3.40536 | -57.99502 | 2026-10-08 12:19:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8a1914a8-ac69-30ef-b210-1650d38fa831 | -3.4541 | -58.05237 | 2026-10-08 12:19:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb736517-484a-3633-bb50-360806494091 | -6.04135 | -53.47897 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c6915b5a-8e97-3ac0-a980-2ffc2fc2ad90 | -3.56701 | -59.46699 | 2026-10-08 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e0ca6eab-a559-3b2a-a772-91d5bec0c7b8 | -6.15602 | -52.64814 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f53f9d6a-3a3d-347d-a28d-e1017749684f | -6.58547 | -53.02177 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 09e1a2e3-6c45-3d6a-a727-78c65c4c4778 | -6.11772 | -55.69057 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dc7a3283-adba-3c7b-ae12-0f65e17493a8 | -4.92378 | -55.85685 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ba62dffc-c198-37a7-aa87-741fe100e11a | -6.14338 | -47.93693 | 2026-10-08 12:19:00 | TERRA_M-T | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c21a0b0d-2256-3482-838f-89f1ec821e9d | -0.99801 | -53.73691 | 2026-10-08 12:19:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dae2e0d3-dd51-3cfc-911f-fca0adfb1ed6 | -2.50015 | -56.60267 | 2026-10-08 12:19:00 | TERRA_M-T | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1bfafd93-6c08-37d1-acdd-144af7b8c39e | -1.53706 | -54.55288 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 33465247-a04b-3a1a-ac7d-846037c46d7d | -3.05119 | -53.95612 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 39e61b76-c4ca-3b35-b278-3b6ff756eebf | -4.57229 | -54.95096 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 459b6150-c7bc-3658-90a1-52055c052289 | -3.62175 | -55.27832 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ee9fce36-b8f2-3334-a2e5-017c45bef0a7 | -6.14104 | -47.94312 | 2026-10-08 12:19:00 | TERRA_M-T | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 1a116baf-aeba-346c-b941-52c5382d17f6 | -3.32842 | -58.1513 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4e8eeeb5-fee8-3c5e-8a16-a94c361e8e6a | -3.06311 | -59.27224 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 163877ae-6f26-3c9f-b97d-addb3dc9830b | -3.092 | -53.9323 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 1c68a6e9-01ba-3797-a413-bf1208075a64 | -3.55037 | -54.67104 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| c2f9934c-89ba-3d7c-abc8-9117e9ec956d | -7.75222 | -54.95671 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README209.md)
