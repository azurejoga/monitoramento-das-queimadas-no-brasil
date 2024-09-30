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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de6517a9-9506-36e1-b601-478fb947ab50 | -11.21064 | -45.72086 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d7bbc8de-2d4d-3141-af29-c5862af4a076 | -11.2093 | -45.72999 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 45f3bb50-8b61-320b-b3ab-d9f105eb5fed | -11.19007 | -45.73639 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| bf09f314-9ece-3a7e-b52f-1163a09182c4 | -11.17977 | -45.74421 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1821d3e2-4020-3165-b8bb-c032443c2d4b | -11.17082 | -45.74288 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 27d92ec7-da8a-335b-b6d9-9b3059bfed5e | -11.16946 | -45.75203 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 49046ef0-a293-3753-84a1-8acefe34a22a | -11.16058 | -45.74463 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| d799ad53-aee6-3e88-8066-81a13f410ea5 | -11.15924 | -45.75379 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b7d28684-d295-3720-aea5-28617bd27b43 | -11.15592 | -45.96637 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4f3d6ffc-c8cc-3738-bd2a-4443fcd97796 | -11.15297 | -45.73416 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| c5e9d899-6c11-3854-b20b-acb4138355aa | -11.15163 | -45.74331 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| e4229ed8-f05a-372c-b25e-af5f2cbd9565 | -11.14537 | -45.7237 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 9298aff7-5ff7-34b0-8dc0-a3aa4ece8915 | -11.14403 | -45.73284 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ba723473-f807-339b-971b-38cfb6c93f57 | -11.14268 | -45.74199 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 78bad781-edbe-3262-9e85-3fa5ab1314c3 | -11.13508 | -45.73153 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 58279335-b7d3-3dea-812e-5b9138108bbb | -11.13373 | -45.74068 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| fedf51c2-185d-3446-895f-4d43fce3cd17 | -11.13238 | -45.74983 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 680f54ad-7050-3be3-b146-58da48c0a0bd | -11.07591 | -45.76046 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 593fb98f-9682-3615-b179-9db9e5d8ef70 | -11.06229 | -45.85204 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 58a324a5-8740-366b-8975-b5e50d94ab4c | -11.06092 | -45.86124 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a6372cd8-bfd3-3770-b076-b908e1f10aa7 | -11.05248 | -45.85357 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a75265c2-4cf3-34f3-91f7-72eb90607cc2 | -10.88795 | -46.03136 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8f0b4313-21c8-3413-a3cb-8aad74883fdd | -10.88656 | -46.04071 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c468d82c-be33-36d7-85e2-761f13b9f469 | -10.88517 | -46.05006 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 31a66b98-a00b-332f-b347-08bac4af0dcd | -10.87546 | -45.99142 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 4e5a7500-51e8-348b-bd8a-e37d0646c733 | -10.86783 | -45.98079 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a4515d14-c288-3028-8f7f-8d450f4097b0 | -10.8602 | -45.97018 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d422947d-58fd-3483-b8f2-d260e4b9db5e | -10.85207 | -45.96252 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 025a061f-2a5c-3488-a890-f6f8002da094 | -10.84305 | -45.96121 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c471005a-aa1b-3b3f-a850-64726dac8815 | -13.20697 | -46.31404 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3903a366-232e-3249-bd3a-0fd81a1f0b94 | -13.20554 | -46.32354 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 00f047d7-dabc-355a-b417-74a733900154 | -13.20136 | -46.35147 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9623005d-9e00-31e9-b50d-fa74d9fe4048 | -13.19853 | -46.30613 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 48562e66-8572-31dc-bc89-f289cbefa401 | -13.19713 | -46.31569 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 3c667078-3b17-321f-8a6f-ca746cadf3c6 | -13.19576 | -46.32504 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| bab8e62d-f8d1-3fa7-b392-5031681da872 | -13.18956 | -46.30475 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 14ce183e-57de-3308-8249-5ebbb1bd9369 | -13.18817 | -46.31419 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 3eecc3e9-367f-3be1-9ab8-df60709a4ac2 | -13.18541 | -46.33289 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 132.8 |
| e0ff049a-5b45-375c-ad54-740e5c1cefc5 | -13.18403 | -46.34223 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ff99692e-b1af-318d-800c-1d4ea4a7fe39 | -13.18265 | -46.35158 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| e5a10e83-bf47-3925-ad46-546a2614b6fe | -13.18128 | -46.36089 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| f726161f-259a-3156-b272-a586accf5dc1 | -13.17505 | -46.34089 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 30fb2fea-0009-3cb0-aca9-6140d1190d4f | -13.17367 | -46.3502 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 034fdee7-a475-3d62-b133-0a074e7068c8 | -13.17229 | -46.3595 | 2024-09-30 12:34:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 5059de68-8ced-3abe-a30a-36d433fc214b | -12.72976 | -46.42049 | 2024-09-30 12:34:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 0c3ff53e-fd76-3ade-af0a-f43443283ed6 | -12.72836 | -46.42984 | 2024-09-30 12:34:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| a17509ac-360d-3877-87cf-b2edf81e49d2 | -12.72028 | -46.42264 | 2024-09-30 12:34:00 | TERRA_M-T | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d9586ec1-ee64-30eb-a8d8-7a076db7c4ba | -14.54971 | -45.39152 | 2024-09-30 12:34:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 675e2990-28cb-31cd-986b-95ec561c6201 | -14.18243 | -46.44925 | 2024-09-30 12:34:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a03e73f9-ccb6-3e64-b1eb-ccd712431f03 | -14.18105 | -46.45862 | 2024-09-30 12:34:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| b56d7ff1-0f0e-3996-ad80-71aaffca02f3 | -14.17209 | -46.45719 | 2024-09-30 12:34:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 44ead67c-ea20-3d97-9836-a2ef6ccca3ac | -14.17071 | -46.4665 | 2024-09-30 12:34:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46ad800e-1412-3b32-8bb0-2e24ca94b631 | -15.4184 | -46.94423 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e4ced172-0699-312a-81e6-0d438faa964d | -15.20153 | -46.22969 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 90108454-7b43-379e-8b7e-3c3a36b3dafb | -9.26259 | -45.73591 | 2024-09-30 12:34:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5ebaacbd-50b2-344d-8a75-7ec597ff991d | -10.86461 | -46.37529 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0e2612b7-af04-3d2c-9080-c2eb9339a436 | -10.57628 | -46.39141 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 87b80853-4f78-3be5-a82e-05a05c9ef76c | -10.49695 | -46.30461 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8613c7e1-2784-36dc-9b15-28732e3e441c | -10.49552 | -46.31424 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 49ec2ed6-937a-304e-8978-749a03174c21 | -10.27092 | -46.87733 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d16c049b-775f-3100-83a8-4b4047e39e89 | -10.26308 | -46.86575 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c36295a8-507c-35ac-9bae-ce22e52417e7 | -10.26152 | -46.87589 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e57372ad-f59f-3b55-a7fd-fbb8a2c069cc | -10.25673 | -46.86907 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 99b76c5a-299c-3baf-b177-4ffb8343835d | -10.22829 | -46.80282 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 706748a7-3832-3166-af5b-390e653fc2c4 | -10.19725 | -46.88094 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 39bdbfab-67f0-3acb-b574-2c9f400bc855 | -10.1957 | -46.89115 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| ebc7088b-ca14-3959-9286-a1eceb6456d1 | -10.11479 | -46.3306 | 2024-09-30 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2c4d444a-3109-38ef-9777-1fd6ff1f13d6 | -10.11335 | -46.34019 | 2024-09-30 12:34:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 77b08a0f-df1d-3909-91f0-a2ccf751e46f | -9.53757 | -46.61731 | 2024-09-30 12:34:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d0a4ce04-8f7f-34ab-9256-f1083365d02c | -10.67937 | -46.13128 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| eb4bb280-a64e-3259-945e-78a050b18303 | -10.67797 | -46.14064 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 06a19d08-3add-3a60-abe1-75f58456793f | -10.67657 | -46.15 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3d20e393-3e72-33b1-bcac-50b4647cbef9 | -10.67517 | -46.15936 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 8d67261c-efe4-374b-90e5-56646ffc8c5d | -10.67171 | -46.12056 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 42da284d-fee5-385a-9662-8a72b20e0770 | -10.6703 | -46.12992 | 2024-09-30 12:34:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| fa221895-75b6-36ea-9cd3-102792ae0b54 | -12.00508 | -47.31425 | 2024-09-30 12:34:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 42138ffc-1425-33df-a1d0-49be17ca7d87 | -12.00353 | -47.3245 | 2024-09-30 12:34:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e93c8bcd-6cea-34f9-ba87-bf182a17c049 | -11.99878 | -47.29229 | 2024-09-30 12:34:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cfd4104c-ecf3-30fb-bf82-fc88d88553f4 | -11.99722 | -47.30253 | 2024-09-30 12:34:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| f177d044-1307-307a-b8cb-7eb79c011cc2 | -11.99566 | -47.31276 | 2024-09-30 12:34:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 6d6ded89-0574-34c9-84ca-bbfe7dff6768 | -11.9941 | -47.323 | 2024-09-30 12:34:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 31ce92a5-2e09-388b-9b20-eaebc8ec2f80 | -11.98781 | -47.30103 | 2024-09-30 12:34:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 3be4efb3-3d3d-31b1-bae8-0689de21481f | -11.98625 | -47.31128 | 2024-09-30 12:34:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| dcf657c1-5c0d-3a74-8d70-80de38c02f4f | -11.85033 | -47.30912 | 2024-09-30 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 22fa534c-5153-3fd0-8707-bdc0e796bfe3 | -11.84878 | -47.31937 | 2024-09-30 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ba609e9a-716d-30b3-9583-1e8fa060b82b | -11.82669 | -47.6221 | 2024-09-30 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| dfd323dd-1801-3fc8-9fb6-b3c8b64194e2 | -11.766 | -47.67213 | 2024-09-30 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 111ef56a-4b70-3580-9ed1-f8c7adbe4c9f | -11.76436 | -47.68285 | 2024-09-30 12:34:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 5a82bb1c-1e4a-3034-ac97-f928e4683458 | -11.4931 | -47.33003 | 2024-09-30 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f9145cd1-1d92-34a8-91ef-8d77a2729a2d | -11.4915 | -47.34037 | 2024-09-30 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 97271a8d-88eb-3a57-9198-10c616e40d39 | -11.44772 | -46.96276 | 2024-09-30 12:34:00 | TERRA_M-T | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 905a29b2-1457-3788-bca2-8e359b967921 | -11.40707 | -47.22624 | 2024-09-30 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9de49efd-46ba-3993-bf2e-fac63e31b00e | -11.403 | -47.21905 | 2024-09-30 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 15375402-f76b-30a3-b1fa-9828eadab0ee | -11.40146 | -47.22932 | 2024-09-30 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 187ff325-b94b-361f-9423-af899d73245d | -10.99507 | -46.48577 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7b4f2252-a78b-3a3d-860a-b08df7c2b0ba | -10.99361 | -46.49546 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d667aabd-cb54-33a0-937d-06f8382d1159 | -10.99215 | -46.50512 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 243.4 |
| 9fc42399-3bd5-3572-a5b0-a08f13561f38 | -10.9907 | -46.51475 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 3c3b2fd6-1b42-319f-a73b-422b13ecb99a | -10.99034 | -46.45505 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2212cf87-7885-38b7-8532-dba31edebf34 | -10.98885 | -46.46488 | 2024-09-30 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |


[Clique aqui para ver as próximas entradas](README74.md)
